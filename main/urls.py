from django.urls import path

from . import views

app_name = "main"
urlpatterns = [

    path("", views.index, name="index"),
    path('add/', views.AccountAdd.as_view(), name='account_add'),
    path('add/success/', views.success, name='success'),
]
