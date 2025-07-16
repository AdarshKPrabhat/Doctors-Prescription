from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('showRecords/',views.showRecords,name="showRecords"),
    path('showPrescription/',views.showPrescription,name="showpres"),
    path('recordAudio/',views.record,name="recordAudio"),
    path('logout/',views.logout,name='logout'),
]