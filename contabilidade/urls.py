from django.urls import path

from . import views

urlpatterns = [
	path("", views.landing_page, name="landing_page"),
	path("painel/", views.panel_messages, name="panel"),
	path('painel/ler/<int:id>/', views.mark_read, name='mark_read'),
    path('painel/excluir/<int:id>/', views.delete_message, name='delete_message'),
]
