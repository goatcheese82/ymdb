from django.urls import path

from . import views

#/directories/
app_name = "directories"

urlpatterns = [
   path("", views.IndexView.as_view(), name="index"),
   path("stake/<int:pk>/", views.StakeDetailView.as_view(), name="stake"),
   path("ward/<int:pk>/", views.WardDetailView.as_view(), name="ward"),
   path("users/<int:pk>/", views.UserDetailView.as_view(), name="member"),
   path("event/<int:pk", views.EventDetailView.as_view(), name="event"),
   path("<int:stake_id>/add_event/", views.add_event, name="add_event"),
]