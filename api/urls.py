from django.urls import path  
from .views import TareaList, TareaDetail, TareaCreate, TareaUpdate  

urlpatterns = [
    path('tareas/', TareaList.as_view(), name='tarea-list'),  # Ruta para listar tareas
    path('tareas/<int:pk>/', TareaDetail.as_view(), name='tarea-detail'),  # Ruta para eliminar una tarea
    path('tareas/create/', TareaCreate.as_view(), name='tarea-create'),  # Ruta para crear una tarea
    path('tareas/update/<int:pk>/', TareaUpdate.as_view(), name='tarea-update'),  # Ruta para actualizar una tarea
]

