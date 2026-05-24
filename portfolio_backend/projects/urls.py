from django.urls import path
from .views import ProjectListView, ProjectDetailView, FeaturedProjectsView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('featured/', FeaturedProjectsView.as_view(), name='featured-projects'),
]
