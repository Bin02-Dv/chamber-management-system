from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signUp/', views.signUp, name='signUp'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path('scheduling/', views.scheduling, name='scheduling'),
    path('manage-case/', views.manage_case, name='manage-case'),
    path('manage-case2/', views.manage_case2, name='manage-case2'),
    path('case-view/<int:id>', views.case_view, name='case-view'),
    path('document-upload/<int:id>', views.document_upload, name='document-upload'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('contact/', views.support, name='contact'),
]