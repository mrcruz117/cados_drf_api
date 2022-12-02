from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from .models import Advocate
from .serializers import AdvocateSerializer


# GET /advocates
# POST /advocates

# GET /advocates/:id
# PUT /advocates/:id
# DELETE /advocates/:id


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', '/advocates/:username']
    return Response(data)


@api_view(['GET', 'POST'])
def advocate_list(request):
    # Handles GET reqs
    if request.method == 'GET':
        search = request.GET.get('search')

        if search == None:
            search = ''

        print('search: ', search)
        advocates = Advocate.objects.filter(
            Q(username__icontains=search) | Q(bio__icontains=search))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)
    # Handles POST reqs
    if request.method == 'POST':

        advocate = Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)


class AdvocateDetail(APIView):
    def get(self, request, id):
        advocate = Advocate.objects.get(id=id)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def advocate_detail(request, id):
#     advocate = Advocate.objects.get(id=id)
#     if request.method == 'GET':
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)
#     # handle PUT req
#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         advocate.save()

#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)
#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('User deleted')
