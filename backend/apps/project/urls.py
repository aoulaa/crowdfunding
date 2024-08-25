from django.urls import path

from project.views.filter import ProjectCategoryFilterView, CategoryView
from project.views.investment import InvestmentListCreateView
from project.views.project import ProjectListCreateView, ProjectDetailView
from project.views.search import ProjectSearchView

urlpatterns = [
    path('campaigns/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('campaigns/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('investments/', InvestmentListCreateView.as_view(), name='investment-list-create'),
    path('investments/<int:pk>/', ProjectDetailView.as_view(), name='investment-detail'),
    path('search/', ProjectSearchView.as_view(), name='project-search'),
    path('category/<int:pk>/', ProjectCategoryFilterView.as_view(), name='project-category'),
    path('category/', CategoryView.as_view(), name='project-category'),
]
