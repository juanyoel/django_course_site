from django.urls import path
from . import views


"""urlpatterns = [
    path('meetups/', views.index, name='all-meetups'),
    path('meetups/<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
]"""

urlpatterns = [
    path('', views.index, name='all-meetups'),
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
]