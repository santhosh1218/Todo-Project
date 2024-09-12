from django.urls import path
from django.contrib.auth import views as auth_views
from todoapp import views
app_name='todoapp'
urlpatterns=[
    path('create/',views.create_task,name='create'),
    path('index/',views.index,name='index'),
    path('status/',views.complete_task,name='status'),
    path('delete/<int:id>',views.delete_task,name='delete'),
    path('update/<int:id>',views.update_task,name='update'),
    path('filter/',views.filter_task,name='filter'),
    path('password/',auth_views.PasswordChangeView.as_view()),
]