import time

from rest_framework import generics

from .models import MenuResto
from .serializers import MenuSerializer
from vendor.template import json_response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from vendor.helper import helper


class MenuList(generics.ListCreateAPIView):
    queryset = MenuResto.objects.all()
    serializer_class = MenuSerializer
#     print("asdffds")

#     def get_read_serializer_class(self):
#         print("ghj")
#         if self.request.method == 'POST':
#             print('test')
#             result = MenuSerializer
#             print('test1')
#             respond = helper.get_detail_serializer_error_message(result)
#             print(respond)
#             return MenuSerializer


#class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = MenuResto.objects.all()
    #serializer_class = MenuSerializer
@api_view(['GET', 'POST'])
def get_menu_list(request):

    if request.method == 'GET':
        menu = MenuResto.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def add_menu(request):
    if request.method == 'POST':
        data = {'name': request.POST.get('name'), 'description': request.POST.get('description'), 'price': request.POST.get('price'), 'status': request.POST.get('status'), 'update_at': request.POST.get('update_at'), 'modified_at': request.POST.get('modified_at')}
        print(data)
        # serializer_class = serializers.MenuSerializer
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.validated_data.get('name')
            message = f'Menu added!'
            # msg = f'Something Wrong!'
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET']) #decorator
def get_menu_by_id(self, menu_id):
    resp = {}
    status_code = status.HTTP_200_OK
    start_time = time.time()
    try:
        menu_detail = MenuResto.objects.get(pk=menu_id)
        result = MenuSerializer(menu_detail)
        status_code = status.HTTP_200_OK
        resp = json_response.render_api_success_response(result.data, start_time, {})
    except MenuResto.DoesNotExist:
        error_message = ['Menu not available']
        status_code = status.HTTP_404_NOT_FOUND
        resp = json_response.render_api_error_response(error_message, start_time, status=status_code)
    return Response(resp, status=status_code)
