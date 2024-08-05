
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from .serializers import Bookserializers
from rest_framework.parsers import JSONParser
from .models import BookModel
import io
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def Book(request):
    return render(request, "index.html")

@csrf_exempt
def Details(request):
    if request.method == 'GET':
        data= BookModel.objects.all()
        serializer = Bookserializers(data, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type ='application/json')
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = Bookserializers(data = python_data)
        if serializer.is_valid():
            serializer.save()
            msg={'message':'Data is Inserted'}
            json_data= JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type ='application/json' )
        error_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(error_data, content_type ='application/json')
    
    # if request.method == 'PUT':
    #     python_data=JSONParser().parse(request)
    #     serializer = Bookserializers(data = python_data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         msg={'message':'DATA is Updated'}
    #         return JsonResponse(msg)
    #     return JsonResponse(serializer.errors)
        ## partial updata
    # if request.method=='PUT':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     python_data = JSONParser().parse(stream)
    #     id = python_data.get('id', None)
    #     if id is not None:
    #         stu = BookModel.objects.get(id=id)
    #         serializer = Bookserializers(stu,data = python_data, partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             msg={'message':'Data is Updated'}
    #             json_data=JSONRenderer().render(msg)
    #             return HttpResponse(json_data, content_tye='application/json')
    #         msg = {'messaage':'DaTa is error'}
    #         error_data= JSONRenderer().render(msg)
    #         return HttpResponse(error_data, content_tye='application/json')
    #     msg = {'messaage':'DaTa is error'}
    #     error_data= JSONRenderer().render(msg)
    #     return HttpResponse(error_data, content_tye='application/json')

        ##complete update
    elif request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        get_id =python_data.get('id')
        hm = BookModel.objects.get(id=get_id)
        serializer= Bookserializers(hm, data=python_data)
        if serializer.is_valid():
            serializer.save()
            msg={'message':'complete data updated'}
            json_data= JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type = 'application/json')
        return_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(return_data, content_type='application/json')


    elif request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        hm = BookModel.objects.get(id=id)
        hm.delete()
        msg= {'message':'data is deleted'}
        return_data = JSONRenderer().render(msg)
        return HttpResponse(return_data, content_type= 'application/json')
    