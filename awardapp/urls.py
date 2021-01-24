from django.urls import path, include 
from . import views
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)
router.register('profile', views.ProfileViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search_project, name='search'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('profile/<username>/', views.profile, name='profile'),
    path('api/', include(router.urls)),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('project/<post>', views.project, name='project'),
    
]