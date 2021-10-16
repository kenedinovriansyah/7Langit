from django.urls import path ,include
from rest_framework import routers
from L7_event.views.event import EventModelViewSets

router = routers.DefaultRouter()
router.register('', EventModelViewSets, basename='event')

urlpatterns = [
    path('', include(router.urls))
]