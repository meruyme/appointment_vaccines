from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from appointments.forms import UserAdminCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from appointments.models import VaccineLocation, Vaccine, ServiceGroup, Appointments, AvailableAppointments, \
    VaccinationRoom, AppointmentRoom

User = get_user_model()

admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserAdminCreationForm
    list_display = ('name', 'email', 'date_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('name', 'email', 'date_birth', 'password')}),
        ('Permissões', {'fields': ('is_admin',)})
    )
    add_fieldsets = (
        (None,
         {'fields': ('name', 'email', 'date_birth', 'password', 'password2'),
          'classes': ('wide',)}),
        ('Permissões', {'fields': ('is_admin',)})
    )
    search_fields = ['email', 'name']
    filter_horizontal = ()
    ordering = ['name']


class VaccinationRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_location')


class VaccineLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'neighborhood', 'city')


class VaccineAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer')


admin.site.site_header = 'Administração do site de vacinas'
admin.site.site_title = 'Administração do site de vacinas'

admin.site.register(User, UserAdmin)
admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(VaccineLocation, VaccineLocationAdmin)
admin.site.register(ServiceGroup)
admin.site.register(AvailableAppointments)
admin.site.register(VaccinationRoom, VaccinationRoomAdmin)
admin.site.register(Appointments)
admin.site.register(AppointmentRoom)
