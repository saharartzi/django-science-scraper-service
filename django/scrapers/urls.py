from .views import ScraperList,CallScraper,CallSci
from rest_framework.routers import DefaultRouter
from django.urls import path, include

app_name = 'scrapers'

router = DefaultRouter()
router.register('', ScraperList, basename='post')


urlpatterns = [
    path('call-scraper/', CallScraper.as_view(), name='token_obtain_pair'),
    path('call-sci/', CallSci.as_view(), name='token_refresh'),
]

urlpatterns += router.urls