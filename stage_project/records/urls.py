

from django.urls import path
from . import views

urlpatterns = [
    path("records/", views.record_list),
    path("records/<str:record_id>/", views.record_detail),
]