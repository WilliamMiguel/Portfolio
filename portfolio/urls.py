from django.urls import path
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #Vista principal de projects
    path('', views.index, name='index'),
    path('new-project/', views.new_project, name='new-project'),
    path('project-detail/<str:title>/', views.project_details, name='project-details'),
    path('project-detail/<str:title>/add_images/', views.add_images_project, name='add-images_project'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),
]