from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signin', views.signin, name='signin'),
    path('intel', views.intel, name='intel'),
    path('about', views.about, name='provider'),
    path('create_stock', views.create_stock, name='create_stock'),
    path('create_provider', views.create_provider, name='create_provider'),
    path('planning', views.planning, name='planning'),
    path('report', views.report, name='report'),
]