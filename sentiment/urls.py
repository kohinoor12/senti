from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'sentiment'

urlpatterns = [
    path('', views.sentiment_analysis, name="sentiment_anaylsis"),
    path('type/', views.sentiment_analysis_type, name="sentiment_analysis_type"),
    path('import/', views.sentiment_analysis_import, name="sentiment_analysis_import"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
