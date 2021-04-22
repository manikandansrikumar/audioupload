from django.conf.urls import url
from django.urls import path


from .views import AudioView

urlpatterns = [
    path('<str:audioFileType>/<int:audioFileID>/', AudioView.as_view()),
]