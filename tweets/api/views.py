from rest_framework import generics
from rest_framework import permissions


from tweets.models import Tweet

from .pagination import StandardResultsPagination
from .serializers import TweetModelSerializer

class TweetCreateAPIView(generics.CreateAPIView):
	serializer_class = TweetModelSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class TweetListAPIView(generics.ListAPIView):
	serializer_class = TweetModelSerializer
	pagination_class = StandardResultsPagination

	def get_queryset(self):
		qs = Tweet.objects.all().order_by("-timestamp")
		return Tweet.objects.all()
