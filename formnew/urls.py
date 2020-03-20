from django.urls import path
from . import views
app_name = "formnew"
urlpatterns = [
    path('enroll', views.enroll, name="enroll"),
    path('login', views.login, name="login"),
    path('register', views.registernew, name="registernew"),
    #path('form', views.form, name="form")
]
