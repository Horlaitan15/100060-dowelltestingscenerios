from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import YouTubeUser

class UserChannels(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):
        '''Gets Users Youtube channels'''

        print('============== User ==', request.user)
        youtube_user = YouTubeUser.objects.get(user=request.user)
        if not youtube_user:
            return Response({'Error': 'Account is not a google account'}, status=status.HTTP_401_UNAUTHORIZED)
        
        credentials = Credentials.from_authorized_user_info(info=youtube_user.credential)

        youtube = build('youtube', 'v3', credentials=credentials, cache_discovery=False)

        channels_response = youtube.channels().list(part='snippet', mine=True).execute()
        channels = [
            {
                'channel_id': channel['id'],
                'channel_title': channel['snippet']['title']
            }
            for channel in channels_response['items']
        ]
        return Response(channels, status=status.HTTP_200_OK)
