from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import os
import subprocess



class verifyVideoAPIView(APIView):
    def post(self, request, *args, **kwargs):
        video_link = request.data.get('video_link')

        if not video_link:
            return Response({'error': 'Video link not provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Download the video
        response = requests.get(video_link)
        if response.status_code != 200:
            return Response({'error': 'Failed to uploaded video'}, status=response.status_code)

        # Save the video to a directory
        save_path = 'videos'
        os.makedirs(save_path, exist_ok=True)

        video_filename = os.path.join(save_path, 'downloaded_video.mp4')
        with open(video_filename, 'wb') as f:
            f.write(response.content)

        # Run the prediction script
        dataset_path = './videos'
        subprocess.run(['../predict_submission.sh', dataset_path, 'submission.csv'], check=True)

        return Response({'message': 'Video uploaded and prediction completed'}, status=status.HTTP_200_OK)
