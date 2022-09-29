
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from.models import Art
from .serializers import Artserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated




''' Created through Generic view set  with TokenAuthentication '''.


class Generic(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,):

    serializer_class = Artserializers
    queryset = Art.objects.all()

    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication,BasicAuthentication]

    #created based on TOKEN Authenication base

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)


    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)


'''-------------------------------------------------end---------------------------------------------------------------------------'''




''' Created through  api_view()Decorator in function based api view  without Authentication '''.



@api_view(['GET','POST'])

def article_list(request):

    # by using GET method we can display all details

    if request.method =='GET':
        art = Art.objects.all()
        serializers=Artserializers(art,many=True)



    # by using POST method we can create new   details


    elif request.method == 'POST':
        serializers=Artserializers(data=request.data)
        if serializers.is_valid():
              serializers.save()
              return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])

'''art_detail function  are using display ,update and delete'''

def art_detail(request,pk):
    try:
        art = Art.objects.get(pk=pk)

    except Art.DoesNotExist:
         return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    if request.method =='GET':
        Serializer = Artserializers(art)
        return Response(Serializer.data)


    elif request.method =='PUT':

        serializers=Artserializers(art,data=request.data)
        if serializers.is_valid():
             serializers.save()
             return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#CLASS BASED VIEW
class Artapiview(APIView):
    def get(self,request):
        art = Art.objects.all()
        serializers = Artserializers(art, many=True)
        return Response(serializers.data)

    def post(self,request):
        serializers = Artserializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class Detailview(APIView):
    def get_obj(self, id):
        try:
            return Art.objects.get(id=id)

        except Art.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        art=self.get_obj(id)
        Serializer = Artserializers(art)
        return Response(Serializer.data)

    def put(self,request,id):
        art = self.get_obj(id)

        serializers = Artserializers(art, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        art = self.get_obj(id)

        art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



