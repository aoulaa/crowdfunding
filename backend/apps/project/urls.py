from django.urls import path

from project.views.investment import InvestmentListCreateView
from project.views.project import ProjectListCreateView, ProjectDetailView

urlpatterns = [
    path('campaigns/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('campaigns/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('investments/', InvestmentListCreateView.as_view(), name='investment-list-create'),
    path('investments/<int:pk>/', ProjectDetailView.as_view(), name='investment-detail'),
]
