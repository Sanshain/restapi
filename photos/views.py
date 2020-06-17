# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.http import HttpResponse


from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Article
from serializers import ArticleSerializer


def index(request):

    return HttpResponse('hello')







class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()

        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})
        # return Response({"articles": articles})

    def post(self, request):
        article = request.data.get('article')
        serializer = ArticleSerializer(data=article)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})