from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSet, basename='todo')

urlpatterns = [
    path('',home, name="home"),
    #function based
    path('get-todo/',get_todo, name="get_todo"),
    path('post-todo/',post_todo, name="post_todo"),
    path('patch-todo/',patch_todo, name="patch_todo"),
    
    #for class based
    path('todo/',TodoView.as_view()),
]

urlpatterns += router.urls