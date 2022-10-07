from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import TimingTOdo, Todo
import re
from django.template.defaultfilters import slugify



class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['uid','todo_title','todo_description','slug','is_done']
        # exclude = ['created_at']       //it is use for off perticulaer data
        
    def get_slug(self, obj):
        return slugify(obj.todo_title)
    
    
    
    
    def validate(self, validated_data):
        print(validated_data)
        
        if validated_data.get('todo_title'):
            todo_title = validated_data['todo_title']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            
            if len(todo_title) < 3:
                raise serializers.ValidationError('More then 3 checrecter')
            
            if not regex.search(todo_title) == None:
                raise serializers.ValidationError('Container not special checkter')
            
        return validated_data
    
    
class TimingTOdoSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()
    class Meta:
        model = TimingTOdo
        exclude = ['created_at','updated_at']
        # depth = 1