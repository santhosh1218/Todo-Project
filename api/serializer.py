from rest_framework import serializers
from todoapp.models import Task
from django.contrib.auth.models import User

class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'

# class Taskserializer(serializers.Serializer):
#     id=serializers.IntegerField()
#     title=serializers.CharField(max_length=100)
#     priority=serializers.CharField()
#     completed=serializers.BooleanField()

#     def create_task(self):
#         taskdata=Task.objects.create(title=self.validated_data['title'],
#                                      priority=self.validated_data['priority'],completed=self.validated_data['completed'])
        
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']