from django.contrib import admin
from django.db.models import Count

from myapp.models import Cake, Baker

class CakeAdmin(admin.ModelAdmin):
    def has_change_permission(self,request,obj=None):
        if obj is not None:
            if request.user == obj.baker.user:
                return True
        return False
    def has_view_permission(self, request, obj=None):
        return True
    def save_model(self, request, obj, form, change):
        # super().save_model(request, obj, form, change)
        baker_cakes = Cake.objects.filter(baker__user = request.user).all()
        if baker_cakes.count() == 10 and not change:
            #this means that there are already 10 cakes and the baker is trying to add one more cake
            return
        #We have 2 scenarios of the task "total cake price of a baker not to be over 10000"
        #The first is when we change a price of the cake
        total_price = sum(cake.price for cake in baker_cakes)
        if change:
            new_price = obj.price
            old_price = Cake.objects.filter(id = obj.id).first().price
            if total_price - old_price + new_price > 10000:
                return
        #The second is when we add a new cake
        if not change:
            if (total_price + obj.price) >10000:
                return
        cake_exist = Cake.objects.filter(name = obj.name).exists()
        if not change and cake_exist:
            return

        super().save_model(request, obj, form, change)

class BakerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(cakes_count = Count('cakes')).filter(cakes_count__lt=5)
        return qs
    def has_add_permission(self,request):
        return request.user.is_superuser
    def has_delete_permission(self,request,obj=None):
        return request.user.is_superuser
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser



admin.site.register(Cake, CakeAdmin)
admin.site.register(Baker, BakerAdmin)