from rest_framework import serializers
from .models import Scraper, Doi
from blog.models import Post
from django.conf import settings


class ScraperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scraper
        fields = ('id', 'name', 'user', 'website',
                  'key_words', 'years_to_search', 'slug')


class DoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doi
        fields = ('id','link','doi')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'authors',
                  'link', 'cites', 'details', 'status','date')