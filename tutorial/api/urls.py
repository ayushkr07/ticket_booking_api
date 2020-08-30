from django.urls import path
from tutorial.api import views

urlpatterns = [
    path('get_all_movies/',views.api_get_all_movies,name='api_get_all_movies'),
    path('get_all_tickets/',views.api_get_all_tickets,name='api_get_all_tickets'),
    path('get_user_detail_from_ticket/<int:id>/',views.api_get_user_detail_from_ticket,name='api_get_user_detail_from_ticket'),
    path('get_movie_detail_from_ticket/<int:id>/', views.api_get_movie_detail_from_ticket,name='api_get_movie_detail_from_ticket'),
    path('get_all_tickets_for_a_time/<int:id>/', views.api_get_all_tickets_for_a_time,name='api_get_all_tickets_for_a_time'),

    path('update_ticket_time/<int:id>/', views.api_update_ticket_time,name='api_update_ticket_time'),

    path('delete_ticket/<int:id>/', views.api_delete_ticket,name='api_delete_ticket'),

    path('book_ticket/', views.api_book_ticket,name='api_book_ticket'),
]
