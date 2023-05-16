from rest_framework.response import Response
from rest_framework.decorators import api_view
from Authentication.models import Fund
from .serializers import FundSerializer

@api_view(['GET'])
def fundList(request):
    funds = Fund.objects.all().order_by('-id')
    serializer = FundSerializer(funds,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fundDetail(request, pk):
    funds = Fund.objects.get(id=pk)
    serializer = FundSerializer(funds,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def fundCreate(request):
    serializer = FundSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def fundUpdate(request, pk):
    fund = Fund.objects.get(id=pk)
    serializer = FundSerializer(instance=fund, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def fundDelete(request, pk):
    fund = Fund.objects.get(id=pk)
    fund.delete()
    
    return Response('Object Deleted .')
