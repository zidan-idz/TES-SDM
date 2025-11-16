from django.urls import path
from . import views


# URL PATTERNS UNTUK APP COMMENTS
urlpatterns = [
    path('', views.comment_index, name='comment_index'),
    path('add/', views.add_comment, name='comment'),
    path('<int:quiz_id>s/', views.comment_list, name='comment_list'),
]