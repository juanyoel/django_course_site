from django.contrib import admin
from . models import Meetup, Location, Participant
# Register your models here.


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('email',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('location', 'address')
    list_filter = ('location',)


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Participant)



