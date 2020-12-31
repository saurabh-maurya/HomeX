from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('status',views.ApplianceStatusView)
router.register('user',views.UserView)

urlpatterns = [
    path('',views.loginpage,name = 'login'),
    path('logout',views.logoutpage,name='logout'),
    path('home/<int:uid>',views.homepage,name= 'home'),
    path('api/',include(router.urls)),
]
