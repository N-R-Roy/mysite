
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from mysite.music.models import Album
# from .serializers import AlbumSerializer

import nltk


# @api_view(('GET',))
def value(request):
    if request.method == 'GET':
        pass
        # name = request.GET.get('ename')
        #
        # tokens = nltk.word_tokenize(name)

        # all_employees = Album.objects.filter(first_name=tokens[0])

        # all_album = Album.objects.all()
        #
        # serializer = AlbumSerializer(all_album, many=True)

        # return Response(serializer.data)
        # return Response(all_album)
        # return JsonResponse({'nm': name})


