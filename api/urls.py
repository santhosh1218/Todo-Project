from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('getemp',views.getemp),
    path('modify/<int:pk>',views.modifytask),
    path('register/',views.registerapi),
    path('login/',obtain_auth_token),
    path('classapi/',views.Getpostapi.as_view()),
    path('modifyapi/<int:pk>',views.Putfetch.as_view()),
    path('genericapi/',views.Genericapiview.as_view())
]
