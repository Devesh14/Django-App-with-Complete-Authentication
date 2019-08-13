from django.conf.urls import url
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    url('about/', views.about, name='blog-about'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url('post/new/', PostCreateView.as_view(), name='post-create'),
    url(r'^(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='post-update'),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post-delete'),
    url('', PostListView.as_view(), name='blog-home'),
    

    ]
    
