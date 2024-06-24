from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from shapeModel.models import Shape
from django.contrib.auth.models import User
from shapeModel.serializers import ShapeSerializer, UserSerializer


@login_required
@api_view(['GET'])
def userHome(request):
    shapes = Shape.objects.all()
    users = User.objects.all()

    shapes_serializer = ShapeSerializer(shapes, many=True)
    users_serializer = UserSerializer(users, many=True)

    context = {
        'shapes': shapes_serializer.data,
    }

    return render(request, "userPortal/user_home.html", context=context)


