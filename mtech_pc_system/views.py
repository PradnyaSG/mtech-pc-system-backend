from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



@api_view(['POST'])
def login(request):
    user = get_object_or_404(User,username = request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail":"Not Found"},status = status.HTTP_404_NOT_FOUND)
    
    token,created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token":token.key,"user":serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    print(request.user)
    user = User.objects.filter(email = request.user.email)
    serializer = UserSerializer(instance=user)
    #user = get_object_or_404(User,username = request.data['username'])

    print(user)
    return Response({"user":serializer.data})

   # return Response("passed for {}".format(request.user.email))