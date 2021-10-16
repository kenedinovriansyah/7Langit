from django.urls import path, include

urlpatterns = [
    path('user', include('L7_user.urls.user')),
    path('event', include('L7_event.urls.event'))
]