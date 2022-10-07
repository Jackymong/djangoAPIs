from functools import partial
from logging import exception
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TimingTOdoSerializer, TodoSerializer
from .models import TimingTOdo, Todo
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action



@api_view(['GET','POST','PATCH','DELETE'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message': 'Yes I am back',
            'method_called': 'Get method'
        })
    
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message': 'Yes I am back',
            'method_called': 'Post method'
        })
        
    elif request.method == 'PATCH':
        return Response({
            'status': 200,
            'message': 'Yes I am back',
            'method_called': 'Patch method'
        })
        
    elif request.method == 'DELETE':
        return Response({
            'status': 200,
            'message': 'Yes I am back',
            'method_called': 'Delete method'
        })
        
    else:
        return Response({
            'status': 400,
            'message': 'Yes I am back',
            'method_called': 'Invalid method'
        })



#GET method
@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs, many = True)
    return Response({
                'status': True,
                'message': "Fatch data",
                'data': serializer.data
            })
    



#POST method
@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "Successfully data",
                'data': serializer.data
            })
        return Response({
            'status': False,
            'message': "Invalid data",
            'data': serializer.errors
        })
    except Exception as e:
        print(e)
    return Response({
            'status': 400,
            'message': 'Something went wrong',
        })
    
    
#PATCH method
@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status': False,
                'message': 'uid is required',
                'data':{}
            })
        obj = Todo.objects.get(uid = data.get('uid'))
        serializer = TodoSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "Successfully data",
                'data': serializer.data
            })
            
        return Response({
            'status': False,
            'message': "Invalid data",
            'data': serializer.errors
        })
    except Exception as e:
        print(e)
    return Response({
            'status': False,
            'message': 'Invalid uid',
            'data':{}
        })
    
    
#Class based api view

class TodoView(APIView):
    def get(self, request):
        todo_objs = Todo.objects.all()
        serializer = TodoSerializer(todo_objs, many = True)
        return Response({
                    'status': True,
                    'message': "Fatch data",
                    'data': serializer.data
                })
        
    def post(self, request):
        try:
            data = request.data
            serializer = TodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': "Successfully data",
                    'data': serializer.data
                })
            return Response({
                'status': False,
                'message': "Invalid data",
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
                'status': 400,
                'message': 'Something went wrong',
            })
        
    def patch(self, request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({
                    'status': False,
                    'message': 'uid is required',
                    'data':{}
                })
            obj = Todo.objects.get(uid = data.get('uid'))
            serializer = TodoSerializer(obj, data = data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': "Successfully data",
                    'data': serializer.data
                })
                
            return Response({
                'status': False,
                'message': "Invalid data",
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
                'status': False,
                'message': 'Invalid uid',
                'data':{}
            })
        
        
        
        
#viewset using api
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    @action(detail=False, methods=['get'])
    def get_timing_todo(self, request):
        objs = TimingTOdo.objects.all()
        serializer = TimingTOdoSerializer(objs, many = True)
        return Response({
                    'status': True,
                    'message': "Timing Fatch data",
                    'data': serializer.data
                })
        
        
        
        
    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTOdoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': "Successfully data",
                    'data': serializer.data
                })
            return Response({
                'status': False,
                'message': "Invalid data",
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
        return Response({
                'status': False,
                'message': 'Invalid uid',
                'data':{}
            })
