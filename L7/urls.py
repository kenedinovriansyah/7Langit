# Author : Kenedy Nopriansyah
# Email : kenedinovriansyah@gmail.com
# description : Don't forgot to happy :D

from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth-token/', obtain_jwt_token, name='authtoken'),
    path('api-auth-refresh/', refresh_jwt_token, name='authtoken-refresh'),
    path('api-auth-verify', verify_jwt_token, name='authtoken-verify'),
    path('api/v1/', include('core.urls'))
]


urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)