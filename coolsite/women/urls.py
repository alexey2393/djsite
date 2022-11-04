from django.urls import path, re_path
from .views import index, categories, archive, pageNotFound


urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:catid>/', categories),
    re_path(r'archive/(?P<year>\d{4})/', archive)
]

