from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from L7_user.serializer.user import UserSerializer, UserModelSerializer


class UserModelViewSets(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    serializer_query = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny,]
        else:
            permission_classes = [permissions.IsAuthenticated,]
        return [permission() for permission in permission_classes]

    def create(self, request):
        serializer = self.serializer_query(data=request.data)
        serializer.context['types'] = 'create'
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Accounts has been created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)