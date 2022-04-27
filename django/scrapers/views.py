from django.shortcuts import render
from .models import Scraper, Doi
from blog.models import Post
from .serializers import ScraperSerializer, DoiSerializer, PostSerializer
from .handleScrap.activating_activator_and_add_resaults import main
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the user only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user



class ScraperList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ScraperSerializer
    
        # Define Custom Queryset
    def get_queryset(self):
        user = self.request.user
        return Scraper.objects.filter(user=user)


    def get_object(self, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Scraper, slug=item)



# to call scraping service 
class CallScraper(APIView):

    serializer_class  = ScraperSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            scraper = Scraper.objects.all().filter(name = serializer.data['name']).first()
            if scraper:
               if request.user == scraper.user:
                main(scraper,"scraper")
                this_scraper_articles = Post.objects.all().filter(user = request.user, scraper = scraper)
                article_serializer = PostSerializer(this_scraper_articles, many = True)
                if article_serializer.is_valid():
                   return Response(article_serializer.data, status=status.HTTP_200_OK)
        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# to call scihub scraping service 
class CallSci(APIView):

    serializer_class = DoiSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
                resault = main(serializer.data['doi'],"doi")
                data = {'doi': serializer.data['doi'], 'link': resault}
                doi_serializer = DoiSerializer(data=data, many=False)
                if doi_serializer.is_valid():
                    return Response(doi_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


