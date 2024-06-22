from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),  # Route de base
    path('chatbot/', views.chatbot_view, name='chatbot_view'),
    path('rag-search/', views.rag_search_view, name='rag_search_view'),
]


