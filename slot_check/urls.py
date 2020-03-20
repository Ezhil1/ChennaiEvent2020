from django.urls import path
from . import views
app_name = 'slot_check'
urlpatterns = [
    path('slot_info', views.slot, name="slot_details")
]
