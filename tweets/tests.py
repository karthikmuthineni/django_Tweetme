from django.contrib.auth import get_user_manual
from django.test import TestCase
from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):
	def setUp(self):
		some_random_user = User.objects.create(username='karthikmuthineni')

	def test_twet_item(self):
		obj = Tweet.objects.create(
			user= ,
			content='Some random content'
			)
		self.assetTrue(obj.content == "Some random content")
# Create your tests here.
