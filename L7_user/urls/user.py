from django.urls import path, include
from rest_framework import routers
from L7_user.views.user import UserModelViewSets

router = routers.DefaultRouter()
router.register('', UserModelViewSets, basename='user')

urlpatterns = [
    path('', include(router.urls))
]