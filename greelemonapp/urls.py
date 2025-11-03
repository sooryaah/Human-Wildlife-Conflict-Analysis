from django.urls import path
from . import views

urlpatterns = [
     path('', views.login_view, name='login'),
     path('superadmin/login/', views.superadmin_login, name='superadmin_login'),
     path('superadmin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
     path('analytic/', views.analytic, name='analytic'),
     path("admin_tracking/", views.admin_tracking, name="admin_tracking"),
     path('animalid1/', views.animalid1, name='animalid1'),
    path('animalid2/', views.animalid2, name='animalid2'),
    path('animalid3/', views.animalid3, name='animalid3'),
    path('animalid4/', views.animalid4, name='animalid4'),
    path('animalid5/', views.animalid5, name='animalid5'),
     path('logout/', views.logout_view, name='logout'),

]
