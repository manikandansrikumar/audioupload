from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Song, AudioBook, Podcast
from .serializers import SongSerializer, PodcastSerializer, AudioBookSerializer


class AudioView(APIView):

    def post(self, request):
        try:
            data = request.data
            audio_file_type = data.get('audioFileType')
            audioFileMetadata = data.get('audioFileMetadata')
            if audio_file_type not in ['song', 'podcast', 'audiobook']:
                return Response({'status': 'fail', 'message': 'Invalid audio type'}, status=status.HTTP_400_BAD_REQUEST)

            if audio_file_type == 'song':
                serializer = SongSerializer(data=audioFileMetadata)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': 'success', 'message': 'song added successfully', 'data' : serializer.data})
                return Response({'status' : 'fail', 'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST)

            elif audio_file_type == 'podcast':
                serializer = PodcastSerializer(data=audioFileMetadata)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': 'success', 'message': 'podcast added successfully', 'data': serializer.data})
                return Response({'status': 'fail', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

            elif audio_file_type == 'audiobook':
                serializer = AudioBookSerializer(data=audioFileMetadata)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': 'success', 'message': 'audio book added successfully', 'data': serializer.data})
                return Response({'status': 'fail', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response({'status': 'fail', 'message': 'Something went wrong. Please try again later'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def put(self, request, audioFileType, audioFileID):
        try:
            data = request.data
            audioFileMetadata = data.get('audioFileMetadata')
            if audioFileType not in ['song', 'podcast', 'audiobook']:
                return Response({'status': 'fail', 'message': 'Invalid audio type'}, status=status.HTTP_400_BAD_REQUEST)

            if audioFileType == 'song':
                try:
                    song_obj = Song.objects.get(id=audioFileID, active=True)
                    serializer = SongSerializer(song_obj, data=audioFileMetadata)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({'status': 'success', 'message': 'song updated successfully', 'data': serializer.data})
                    return Response({'status': 'fail', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                except Song.DoesNotExist:
                    return Response({'status': 'fail', 'message': 'song not available'},
                                    status=status.HTTP_400_BAD_REQUEST)

            elif audioFileType == 'podcast':
                try:
                    podcast_obj = Podcast.objects.get(id=audioFileID, active=True)
                    serializer = PodcastSerializer(podcast_obj,data=audioFileMetadata)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({'status': 'success', 'message': 'podcast updated successfully', 'data': serializer.data})
                    return Response({'status': 'fail', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                except Podcast.DoesNotExist:
                    return Response({'status': 'fail', 'message': 'podcast not available'},
                                    status=status.HTTP_400_BAD_REQUEST)

            elif audioFileType == 'audiobook':
                try:
                    audiobook_obj = AudioBook.objects.get(id=audioFileID, active=True)
                    serializer = AudioBookSerializer(audiobook_obj,data=audioFileMetadata)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(
                            {'status': 'success', 'message': 'audio book updated successfully', 'data': serializer.data})
                    return Response({'status': 'fail', 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

                except AudioBook.DoesNotExist:
                    return Response({'status': 'fail', 'message': 'Audio book information not available'},
                                    status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response({'status': 'fail', 'message': 'Something went wrong. Please try again later'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def delete(self, request, audioFileType, audioFileID):
        try:
            if audioFileType not in ['song', 'podcast', 'audiobook']:
                return Response({'status': 'fail', 'message': 'Invalid audio type'}, status=status.HTTP_400_BAD_REQUEST)

            if audioFileType == 'song':
                try:
                    song_obj = Song.objects.get(id=audioFileID, active=True)
                    song_obj.active = False
                    song_obj.save()
                    return Response({'status': 'success', 'message': 'song deleted successfully'})
                except Song.DoesNotExist:
                    return Response({'status': 'fail', 'message': 'song not available'},
                                    status=status.HTTP_400_BAD_REQUEST)

            elif audioFileType == 'podcast':
                try:
                    podcast_obj = Podcast.objects.get(id=audioFileID, active=True)
                    podcast_obj.active = False
                    podcast_obj.save()
                    return Response({'status': 'success', 'message': 'podcast deleted successfully'})
                except Podcast.DoesNotExist:
                    return Response({'status': 'fail', 'message': 'podcast not available'},
                                    status=status.HTTP_400_BAD_REQUEST)

            elif audioFileType == 'audiobook':
                try:
                    audiobook_obj = AudioBook.objects.get(id=audioFileID, active=True)
                    audiobook_obj.active = False
                    audiobook_obj.save()
                    return Response(
                            {'status': 'success', 'message': 'audio book deleted successfully'})
                except AudioBook.DoesNotExist:
                    return Response({'status': 'fail', 'message': 'Audio book information not available'},
                                    status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response({'status': 'fail', 'message': 'Something went wrong. Please try again later'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get(self, request, audioFileType, audioFileID):
        try:
            if audioFileType == 'song':
                try:
                    song_obj = Song.objects.get(id=audioFileID, active=True)
                    serializer = SongSerializer(song_obj)
                    return Response({'status': 'success', 'data': serializer.data})
                except Song.DoesNotExist:
                    return Response({'status': 'fail', 'message': 'song not available'},
                                    status=status.HTTP_400_BAD_REQUEST)
            elif audioFileType == 'podcast':
                try:
                    podcast_obj = Podcast.objects.get(id=audioFileID, active=True)
                    serializer = PodcastSerializer(podcast_obj)
                    return Response({'status': 'success', 'data': serializer.data})
                except Podcast.DoesNotExist:
                    return Response({'status': 'fail', 'message': 'podcast not available'},
                                    status=status.HTTP_400_BAD_REQUEST)

            elif audioFileType == 'audiobook':
                try:
                    audiobook_obj = AudioBook.objects.get(id=audioFileID, active=True)
                    serializer = AudioBookSerializer(audiobook_obj)
                    return Response({'status': 'success', 'data': serializer.data})
                except AudioBook.DoesNotExist:
                    return Response({'status': 'fail', 'message': 'Audio book information not available'},
                                    status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response({'status': 'fail', 'message': 'Something went wrong. Please try again later'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


