# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Article
from serializers import ArticleSerializer


def index(request):

    return HttpResponse('hello')



def theArticle(request, **kwargs):
    print request.build_absolute_uri()
    return HttpResponse(kwargs.get('pk'))





class ArticleView(APIView):

    def put(self, request, pk):

        print '-------'
        print pk

        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Article '{}' updated successfully".format(article_saved.title)
        })


    def get(self, request):
        print '???????????'
        articles = Article.objects.all()

        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})
        # return Response({"articles": articles})

    def post(self, request):
        print ':::::::::::'
        article = request.data.get('article')
        serializer = ArticleSerializer(data=article)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

