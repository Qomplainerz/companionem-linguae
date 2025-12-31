from django.contrib import admin
from django.urls import path
from . import views  # Importiere die views von eben

urlpatterns = [
    path('admin/', admin.site.urls),
    # Hier ist unsere neue Schnittstelle für JavaScript:
    path('chat-api/', views.chat_api, name='chat_api'),
]
