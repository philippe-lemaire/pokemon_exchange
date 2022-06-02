from django.urls import path

from . import views

app_name = "user_messages"

urlpatterns = [
    path("", views.IndexView.as_view(), name="message_index"),
]
