from django.contrib import admin
from appointments.models import VaccineLocation, Vaccine, Citizen, ServiceGroup, Appointments, AvailableAppointments, \
    VaccinationRoom, AppointmentRoom

admin.site.register(Vaccine)
admin.site.register(VaccineLocation)
# admin.site.register(Citizen)
admin.site.register(ServiceGroup)
admin.site.register(AvailableAppointments)
admin.site.register(VaccinationRoom)
admin.site.register(Appointments)
admin.site.register(AppointmentRoom)
