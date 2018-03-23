#from django import forms
#from django.forms.utils import ErrorList
from django.shortcuts import render
#from django.views.generic import DetailView, Listview, CreateView

# Create your views here.
from .forms import TweetModelForm
from .models import Tweet 
#Create

#class TweetCreateView(CreateView):
#	form_class = TweetModelForm
#	queryset = Tweet.objects.all()
#	form = TweetModelForm
#	fields = ['user', 'content']
#	def form valid(self, form):
#		if self.request.user.is_authenticated():
#			return super(TweetCreateView, self).form_valid(form)
#		else:
#			form_errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
#			return self.form_valid(form)

#Retrieve

#Update

#Delete


#List / Search
def tweet_create_view(request):
	form = TweetModelForm(request.POST or None)

	if form.is_valid():
		instance = form .save(commit=False)
		instance.user = request.user
		instance.save()

	context = {
		"form":form
	}
	return render(request, 'tweets/create_view.html', context)


def tweet_detail_view(request, id=1):
	obj = Tweet.objects.get(id=id)
	print(obj)
	context = {
		"object": obj
	}
	return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request):
	queryset = Tweet.objects.all()
	print(queryset)
	for obj in queryset:
		print(obj.content)
	context = {
		"object_list": queryset
	}
	return render(request, "tweets/list_view.html", context)