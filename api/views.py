from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BankDetail
from .serializers import ApiSerializer
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes



@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer,))
def index(request, format=None):
    return Response({}, template_name='index.html')
    
#Overiding Django's default 404 with custom JSON response
@api_view(['GET'])
def error_404(request, exception):
    return Response(status=status.HTTP_404_NOT_FOUND)

#Return details of branch with matching ifsc
@api_view(['GET'])
def ifsc_details(request,ifsc,format=None):
    ifsc=ifsc.upper()
    try:
        ifsc = BankDetail.objects.get(ifsc_code=ifsc)
    except BankDetail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApiSerializer(ifsc)
        return Response(serializer.data)

#Return all branches of a bank in a city
@api_view(['GET'])
def details_of_branches(request,bank,city,format=None):
    bank=bank.replace('-',' ').upper()
    city=city.replace('-',' ').upper()
    branches = BankDetail.objects.filter(bank_name=bank,city=city).all()
    if bool(branches)==False:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ApiSerializer(branches, many=True)
        return Response(serializer.data)