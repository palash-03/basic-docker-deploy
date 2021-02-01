from django.urls import path
from scrap_app import views
from django.contrib.auth import views as auth_views

# app_name = 'scrap_app'
urlpatterns =[
	path('',auth_views.LoginView.as_view(template_name = "employes/login.html"), name="login"),
	path('logout/',auth_views.LogoutView.as_view(next_page='login'),name="logout"),
	path('register/',views.EmployeeRegisterView.as_view(),name='register'),
	path('project/',views.ProjectRegisterView.as_view(),name='project'),
	path('project_detail/',views.ProjectDetailView.as_view(),name='project_detail'),
]