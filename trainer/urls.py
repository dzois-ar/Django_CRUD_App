from django.urls import path
from . import views



urlpatterns = [
    path('all_trainer/', views.all_trainer, name='all_trainer'),
    path('delete_trainer/<int:id>/', views.delete_trainer, name='delete_trainer'),
    path('update_trainer/<int:id>/', views.update_trainer, name='update_trainer'),
    path('trainer-details/<int:id>/', views.trainer_details, name='trainer_details'),
    path('success/<str:message>/', views.success, name='success'),
    path('add_trainer/', views.add_trainer, name='add_trainer'),
]