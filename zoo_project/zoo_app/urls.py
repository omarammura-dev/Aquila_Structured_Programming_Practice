from django.urls import path
from . import views



urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_animal/', views.add_animal, name='add_animal'),
    path('add_random_visitors/<int:habitat_id>', views.add_random_visitors, name='add_random_visitors'),
    path('<int:habitat_id>/list_animals/', views.list_animals, name='list_animals'),
    path('animal/<int:id>/eat/', views.animal_eat, name='animal_eat'),
    path('animal/<int:id>/sleep/', views.animal_sleep, name='animal_sleep'),
    path('animal/<int:id>/move/', views.animal_move, name='animal_move'),
    path('animal/<int:id>/birth/', views.animal_birth, name='animal_birth'),
    path('animal/<int:id>/hunt/', views.animal_hunt, name='animal_hunt'),
]