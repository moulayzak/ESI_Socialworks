from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
class HomeView(APIView):
     
    permission_classes = (IsAuthenticated, )   
    
    def get(self, request):       
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}   
        
        return Response(content)

class LogoutView(APIView): 
        
    permission_classes = (IsAuthenticated,) 
        
    def post(self, request):
          
        try:          
                 
            refresh_token = request.data["refresh_token"]               
            token = RefreshToken(refresh_token)               
            token.blacklist()     
                      
            return Response(status=status.HTTP_205_RESET_CONTENT)          
        except Exception as e:  
                         
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            
            username = User.objects.get(email=email).username
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None :
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username or password is incorrect')
                    
        context = {}
        return render(request,'authenticate/login.html',context)


@login_required(login_url='login')
def homePage(request):
    return render(request,'authenticate/home.html')
@allowed_users(allowed_roles=['Employee'])
@login_required(login_url='login')
def userPage(request):
    return render(request,'authenticate/user.html')



def logoutUser(request):
    logout(request)
    return redirect('login')

#------------------User_views---------------------------

@api_view(['GET'])
def UserList(request):
    users = User.objects.all().order_by('-id')
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UserDetail(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def UserUpdate(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def UserDelete(request, pk):
    User = user.objects.get(id=pk)
    User.delete()
    
    return Response('Object Deleted .')

#------------------fund_views---------------------------

@api_view(['GET'])
def FundList(request):
    funds = Fund.objects.all().order_by('-id')
    serializer = FundSerializer(funds,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def FundDetail(request, pk):
    funds = Fund.objects.get(id=pk)
    serializer = FundSerializer(funds,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def FundCreate(request):
    serializer = FundSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def FundUpdate(request, pk):
    fund = Fund.objects.get(id=pk)
    serializer = FundSerializer(instance=fund, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def FundDelete(request, pk):
    fund = Fund.objects.get(id=pk)
    fund.delete()
    
    return Response('Object Deleted .')


#------------------Chapter_views---------------------------

@api_view(['GET'])
def ChapterList(request):
    chapters = Chapter.objects.all().order_by('-id')
    serializer = ChapterSerializer(chapters,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ChapterDetail(request, pk):
    chapters = Chapter.objects.get(id=pk)
    serializer = ChapterSerializer(chapters,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ChapterCreate(request):
    serializer = ChapterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def ChapterUpdate(request, pk):
    chapter = Chapter.objects.get(id=pk)
    serializer = ChapterSerializer(instance=chapter, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def ChapterDelete(request, pk):
    chapter = Chapter.objects.get(id=pk)
    chapter.delete()
    
    return Response('Object Deleted .')

#------------------article_views---------------------------

@api_view(['GET'])
def ArticleList(request):
    articles = Article.objects.all().order_by('-id')
    serializer = ArticleSerializer(articles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ArticleDetail(request, pk):
    articles = Article.objects.get(id=pk)
    serializer = ArticleSerializer(articles,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ArticleCreate(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def ArticleUpdate(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(instance=article, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def ArticleDelete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    
    return Response('Object Deleted .')

#------------------Program_views---------------------------

@api_view(['GET'])
def ProgramList(request):
    programs = Program.objects.all().order_by('-id')
    serializer = ProgramSerializer(programs,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ProgramDetail(request, pk):
    programs = Program.objects.get(id=pk)
    serializer = ProgramSerializer(programs,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ProgramCreate(request):
    serializer = ProgramSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def ProgramUpdate(request, pk):
    program = Program.objects.get(id=pk)
    serializer = ProgramSerializer(instance=program, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def ProgramDelete(request, pk):
    program = Program.objects.get(id=pk)
    program.delete()
    
    return Response('Object Deleted .')

#------------------Request_views---------------------------

@api_view(['GET'])
def RequestList(request):
    requests = Request.objects.all().order_by('-id')
    serializer = RequestSerializer(requests,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def RequestDetail(request, pk):
    requests = Request.objects.get(id=pk)
    serializer = RequestSerializer(requests,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def RequestCreate(request):
    serializer = RequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def RequestUpdate(request, pk):
    request = Request.objects.get(id=pk)
    serializer = RequestSerializer(instance=request, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def RequestDelete(request, pk):
    request = Request.objects.get(id=pk)
    request.delete()
    
    return Response('Object Deleted .')

#------------------Transaction_views---------------------------

@api_view(['GET'])
def TransactionList(request):
    transactions = Transaction.objects.all().order_by('-id')
    serializer = TransactionSerializer(transactions,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TransactionDetail(request, pk):
    transactions = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(transactions,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def TransactionCreate(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def TransactionUpdate(request, pk):
    transaction = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(instance=transaction, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def TransactionDelete(request, pk):
    transaction = Transaction.objects.get(id=pk)
    transaction.delete()
    
    return Response('Object Deleted .')

#------------------Event_views---------------------------

@api_view(['GET'])
def EventList(request):
    events = Event.objects.all().order_by('-id')
    serializer = EventSerializer(events,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def EventDetail(request, pk):
    events = Event.objects.get(id=pk)
    serializer = EventSerializer(events,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def EventCreate(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def EventUpdate(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(instance=event, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def EventDelete(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    
    return Response('Object Deleted .')

#------------------Notification_views---------------------------

@api_view(['GET'])
def NotificationList(request):
    notifications = Notification.objects.all().order_by('-id')
    serializer = NotificationSerializer(notifications,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def NotificationDetail(request, pk):
    notifications = Notification.objects.get(id=pk)
    serializer = NotificationSerializer(notifications,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def NotificationCreate(request):
    serializer = NotificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def NotificationUpdate(request, pk):
    notification = Notification.objects.get(id=pk)
    serializer = NotificationSerializer(instance=notification, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def NotificationDelete(request, pk):
    notification = Notification.objects.get(id=pk)
    notification.delete()
    
    return Response('Object Deleted .')