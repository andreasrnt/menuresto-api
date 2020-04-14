from rest_framework import generics

from .models import MenuResto
from .serializers import MenuSerializer

class MenuList(generics.ListCreateAPIView):
    queryset = MenuResto.objects.all()
    serializer_class = MenuSerializer

    def get_read_serializer_class(self):
        if self.request.method == 'POST':
            return MenuSerializer


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuResto.objects.all()
    serializer_class = MenuSerializer