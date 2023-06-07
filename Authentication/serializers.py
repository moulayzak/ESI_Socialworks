from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
 
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()    
    class Meta:
        model = User
        fields = ['email']
     

class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = '__all__'
            
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'     

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'  
            
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['chapter','description'] 
            
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'  
            
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'  
            
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'  
            
class NotificationSerializer(serializers.ModelSerializer):
     class Meta:
        model = Notification
        fields = '__all__'  