from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name= 'boards'

urlpatterns = [
    # path('',views.home,name='index'),
    path('about/',views.about, name='about'),
    # path('boards/<int:board_id>', views.board_topics, name='board_topics'),
]
