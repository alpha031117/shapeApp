from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

from shapeModel.models import Shape
from shapeModel.forms import ShapeForm
from shapeModel.serializers import ShapeSerializer, UserSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



def admin_group_required(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(admin_group_required)
@api_view(['GET'])
def home(request):
    shapes = Shape.objects.all()
    users = User.objects.all()

    shapes_serializer = ShapeSerializer(shapes, many=True)
    users_serializer = UserSerializer(users, many=True)

    context = {
        'shapes': shapes_serializer.data,
        'users': users_serializer.data,
		'user_count': users.count(),
		'shape_count': shapes.count()
    }

    return render(request, "adminPortal/admin_home.html", context=context)

@user_passes_test(admin_group_required)
def createForm(request):
	form = ShapeForm()
	return render(request, 'adminPortal/shape_form.html', {'form': form})

@user_passes_test(admin_group_required)
def editForm(request, pk):
	shape = Shape.objects.get(id=pk)
	form = ShapeForm(instance=shape)
	return render(request, 'adminPortal/shape_form.html', {'form': form})

@user_passes_test(admin_group_required)
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'api/shape-list/',
		'Detail View':'api/shape-detail/<str:pk>/',
		'Create':'api/shape-create/',
		'Update':'api/shape-update/<str:pk>/',
		'Delete':'api/shape-delete/<str:pk>/',
		}

	return Response(api_urls)

@user_passes_test(admin_group_required)
@api_view(['GET'])
def shapeList(request):
	shape = Shape.objects.all()
	serializer = ShapeSerializer(shape, many=True)
	return Response(serializer.data)

@user_passes_test(admin_group_required)
@api_view(['GET'])
def shapeDetail(request, pk):
    try:
        shape = Shape.objects.get(pk=pk)
        serializer = ShapeSerializer(shape)
        return Response(serializer.data)
    except Shape.DoesNotExist:
        return Response({'error': 'Shape not found'}, status=status.HTTP_404_NOT_FOUND)

@user_passes_test(admin_group_required)
@api_view(['POST'])
def shapeCreate(request):
    serializer = ShapeSerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@user_passes_test(admin_group_required)
@api_view(['PUT'])
def shapeUpdate(request, pk):
    shape = get_object_or_404(Shape, pk=pk)
    serializer = ShapeSerializer(instance=shape, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@user_passes_test(admin_group_required)
@api_view(['DELETE'])
def shapeDelete(request, pk):
	shape = Shape.objects.get(id=pk)
	shape.delete()

	return Response('Shape succsesfully delete!')
