from django.conf.urls import url
from django.urls import path


from .views import AudioCreateView, UpdateAPIView, DeleteAPIView, DetailsAPIVIew

urlpatterns = [
    url('create/', AudioCreateView.as_view()),
    path('update/<str:audioFileType>/<int:audioFileID>/', UpdateAPIView.as_view()),
    path('delete/<str:audioFileType>/<int:audioFileID>/', DeleteAPIView.as_view()),
    path('details/<str:audioFileType>/<int:audioFileID>/', DetailsAPIVIew.as_view()),
]