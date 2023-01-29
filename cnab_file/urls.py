from django.urls import path
from .views import CNABDataView

urlpatterns = [
    path('upload/', CNABDataView.as_view()),
]