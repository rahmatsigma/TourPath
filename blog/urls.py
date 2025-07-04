from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.index, name='index'),
    path('blog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('settings/', views.settings_view, name='settings'),
    path('rencana/', views.rencana_view, name='rencana'),
    path('delete-account/', views.delete_account, name='delete_account'),    path('about/', views.about_view, name='about'),    
    path('destinasi/', views.destinasi_view, name='destinasi'),
    path('destinasi2/', views.destinasi2_view, name='destinasi2'),
    path('destinasi3/', views.destinasi3_view, name='destinasi3'),
    path('contact/', views.contact_view, name='contact'),
    path('bantuan/', views.bantuan_view, name='bantuan'),
]