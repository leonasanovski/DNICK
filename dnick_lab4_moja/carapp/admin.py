from django.contrib import admin

from carapp.models import Car,Manufacturer

class ManufacturerAdmin(admin.ModelAdmin):
    exclude = ("user",)
    #Instead of the user to enter himself, automatically it assigns
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ManufacturerAdmin, self).save_model(request, obj, form, change)

admin.site.register(Car)
admin.site.register(Manufacturer,ManufacturerAdmin)

