from django.urls import path
from users.views.user import UserDetailView

urlpatterns = [
    path("user/<int:key>/", UserDetailView.as_view(), name="user-detail"),
]
