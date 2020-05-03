from django.urls import path
from . import views

urlpatterns = [
    # Home Page / About
    path('', views.PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    # Post pages
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name = 'post-update'),
    path('post/new/', views.PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'post-delete'),
    path('user/<str:username>/', views.UserPostListView.as_view(), name = 'user-posts'),
]
