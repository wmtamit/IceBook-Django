from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path(
    	"login/",
    	auth_views.LoginView.as_view(template_name="accounts/login.html"),
    	name="login"
    ),
    path(
    	"logout/",
    	auth_views.LogoutView.as_view(template_name="accounts/logout.html"),
    	name="logout"
    ),
    path("profile/", views.profile_view, name="profile"),
    path("update/", views.update_view, name="update"),
    path("delete/", views.delete_view, name="delete"),
    path('users/<str:username>', views.display_user_view, name="display")
]
