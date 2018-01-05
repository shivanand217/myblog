from django.conf.urls import url

from . import views

urlpatterns = [
	# assign a view post_list to ^$ url
	url(r'^$', views.post_list , name = 'post_list'),
]