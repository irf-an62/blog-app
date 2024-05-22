from django.urls import path
from .views import (
    PostListCreateView, PostDetailView, 
    CommentListCreateView, CommentDetailView,
    LikePostView,UserRegistrationView,PasswordResetRequestView,PasswordResetConfirmView
)

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
]
