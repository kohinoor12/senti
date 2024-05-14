from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'sentiment_or_emotion'

urlpatterns = [
    path('', views.choose_sentiment_or_emotion, name="choose_sentiment_or_emotion"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
