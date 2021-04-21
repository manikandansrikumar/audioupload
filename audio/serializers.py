from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class SongSerializer(ModelSerializer):

    class Meta:
        model = Song
        exclude = ('active', 'modified_on')




class PodcastSerializer(ModelSerializer):

    class Meta:
        model = Podcast
        exclude = ('active', 'modified_on')


class AudioBookSerializer(ModelSerializer):

    class Meta:
        model = AudioBook
        exclude = ('active', 'modified_on')