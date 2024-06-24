from django.urls import path, include
from . import views

app_name = "adminPortal"

urlpatterns = [
    path("", views.home, name="admin_home"),
    path("createForm/", views.createForm, name="shape_form"),
    path("editForm/<int:pk>/", views.editForm, name="shape_edit_form"),

    # API CRUD operations
    path('api/', views.apiOverview, name="api-overview"),
    path("api/shape_create/", views.shapeCreate, name="shape_create"),
    path("api/shape_list/", views.shapeList, name="shape_list"),
    path("api/shape_detail/<str:pk>/", views.shapeDetail, name="shape_detail"),
    path('api/shape/<int:pk>/edit/', views.shapeUpdate, name='shape_edit'),
    path('api/shape/<int:pk>/delete/', views.shapeDelete, name='shape_delete'),
]
