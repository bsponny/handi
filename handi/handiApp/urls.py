from django.urls import path
from . import views

app_name='handiApp'

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'),
    path('learn/', views.learn, name='learn'),
    path('connect/', views.connect, name='connect'),
    path('account/', views.account, name='account'),
    path('mentorRequest/', views.mentorRequest, name='mentorRequest'),
    path('mentorRequests/', views.mentorRequests, name='mentorRequests'),
    path('request/<int:request_id>/', views.request, name='request'),
    path('userType/', views.userType, name='userType'),
    path('community/', views.community, name='community'),
]

