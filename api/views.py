from rest_framework import generics  
from .models import Tarea  
from .serializers import TareaSerializer  

class TareaList(generics.ListAPIView):
    # Vista para listar todas las tareas
    queryset = Tarea.objects.all()  # Obtiene todas las instancias
    serializer_class = TareaSerializer 

class TareaDetail(generics.DestroyAPIView):
    # Vista para eliminar una tarea específica
    queryset = Tarea.objects.all()  
    serializer_class = TareaSerializer  

class TareaCreate(generics.CreateAPIView):
    # Vista para crear una nueva tarea
    queryset = Tarea.objects.all()  
    serializer_class = TareaSerializer  

class TareaUpdate(generics.UpdateAPIView):
    # Vista para actualizar una tarea existente
    queryset = Tarea.objects.all()  
    serializer_class = TareaSerializer  
