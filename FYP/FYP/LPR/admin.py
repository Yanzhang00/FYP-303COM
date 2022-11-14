from django.contrib import admin
from .models import Owner, Vehicle, Visitor, Image, VisitorEnterDateTime, OwnerEnterDateTime
from django import forms
from django.utils.html import format_html

# Register your models here.
#admin.site.register(Owner, OwnerAdmin)

class visitorFormValidation(forms.ModelForm):
    """Custom validation for visitor number plate"""
    class Meta:
        model = Visitor
        fields = ['name', 'visitUnit', 'visitorPlateNum']

    def clean(self):
        cleaned_data = self.cleaned_data
        visitorPlateNum = cleaned_data.get('visitorPlateNum')
        
        sameCurrentPlateNum = Vehicle.objects.filter(plateNum=visitorPlateNum)
        sameVisitorPlateNum = Visitor.objects.filter(visitorPlateNum=visitorPlateNum)
        if sameCurrentPlateNum.exists():
            self.add_error('visitorPlateNum', "Same Plate Number found in owner")

        if sameVisitorPlateNum.exists():
            self.add_error('visitorPlateNum', "Same Plate Number found in visitor")

        else:
            return self.cleaned_data


class vehicleFormValidation(forms.ModelForm):
    """Custom validation for visitor number plate"""
    class Meta:
        model = Vehicle
        fields = '__all__'

    def clean(self):
        cleaned_data = self.cleaned_data
        plateNum = cleaned_data.get('plateNum')
        
        sameVisitorPlateNum = Visitor.objects.filter(visitorPlateNum=plateNum)
        samePlateNum = Vehicle.objects.filter(plateNum=plateNum)
        if sameVisitorPlateNum.exists():
            self.add_error('plateNum', "Same Plate Number found in visitor")

        if samePlateNum.exists():
            self.add_error('plateNum', "Same Plate number found in owner")

        else:
            return self.cleaned_data

@admin.register(VisitorEnterDateTime)
class VisitorEnterDateTimeAdmin(admin.ModelAdmin):
    readonly_fields = ('dateTime', 'get_visitor')

    def get_visitor(self, obj):
        return obj.visitor.visitorPlateNum

@admin.register(OwnerEnterDateTime)
class OwnerEnterDateTimeAdmin(admin.ModelAdmin):
    readonly_fields = ('dateTime', 'get_owner')

    def get_owner(self, obj):
        return obj.vehicle.plateNum


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    form = vehicleFormValidation
    list_display = ('brand', 'model', 'colour', 'plateNum', 'get_owner')

    def get_owner(self, obj):
        return obj.owner.name

    # Allow column sorting
    get_owner.admin_order_field = 'owner'
    get_owner.short_description = 'Owner Name'

# @admin.register(Visitor)
# class VisitorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'visitUnit', 'visitorPlateNum')

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    form = visitorFormValidation
    list_display = ('name', 'visitUnit', 'visitorPlateNum')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = "Image Section"

    list_display = ['image_tag']
