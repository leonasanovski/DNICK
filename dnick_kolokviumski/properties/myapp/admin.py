import datetime

from django.contrib import admin
from django.db.models import Q

from myapp.models import *


class AgentInLine(admin.TabularInline):
    model = AgentRealEstate
    extra = 0


class CharacteristicInLine(admin.TabularInline):
    model = CharacteristicRealEstate
    extra = 0


class RealEstateAdmin(admin.ModelAdmin):
    inlines = [AgentInLine, CharacteristicInLine, ]
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        if change:
            old_real_estate = RealEstate.objects.get(id=obj.id)
            if old_real_estate.isSold == False and obj.isSold == True:
                agent_real_estates = AgentRealEstate.objects.filter(real_estate_id=obj.id)
                for i in agent_real_estates:
                    i.agent.sold_real_estates += 1
                    i.agent.save()
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            num_characterics = CharacteristicRealEstate.objects.filter(real_estate_id=obj.id).count()
            if num_characterics == 0:
                return True
        return False

    def has_change_permission(self, request, obj=None):
        return obj is not None and AgentRealEstate.objects.filter(
            Q(agent__user=request.user) & Q(real_estate=obj)).exists()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(publishing_date__date=datetime.date.today())
        return qs


class AgentAdmin(admin.ModelAdmin):
    exclude = ('sold_real_estates',)

    def has_add_permission(self, request):
        return request.user.is_superuser


class CharacteristicAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Agent, AgentAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(RealEstate, RealEstateAdmin)
