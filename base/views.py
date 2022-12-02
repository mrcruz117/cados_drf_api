from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
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


@api_view(['GET'])
def advocate_detail(request, username):
    advocate = Advocate.objects.get(username=username)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)
