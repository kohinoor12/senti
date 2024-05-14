from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'emotion'

urlpatterns = [
    path('', views.emotion_analysis, name="emotion_anaylsis"),
    path('type/', views.emotion_analysis_type, name="emotion_analysis_type"),
    path('import/', views.emotion_analysis_import, name="emotion_analysis_import"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
