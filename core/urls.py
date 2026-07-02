from django.urls import path

from .views import (
    JobListAPI,
    JobCreateAPI,
    UserTestAPI,
)

urlpatterns = [
    path("", UserTestAPI.as_view()),      # Home page
    path("test/", UserTestAPI.as_view()),
    path("jobs/", JobListAPI.as_view()),
    path("jobs/create/", JobCreateAPI.as_view()),
]