from django.urls import path
from django.urls.conf import include
from . import views
from django.views.generic import RedirectView
app_name='blog'
urlpatterns=[
    path('', RedirectView.as_view(url='/posts')),
    path('posts',views.PostList.as_view(),name='postlist'),
    path('post/create/',views.createpost.as_view(),name='createpost'),
    path('post/<int:pk>/update/',views.UpdatePost.as_view(),name='updatepost'),    
    path('post/<int:pk>/delete/', views.DeletePost.as_view(),name='updatepost'),
    path('post/<int:pk>', views.PostDetials.as_view(),name='postdetails'),
    path('posts/draft/', views.draftPost.as_view(),name='drafts'),
    path('post/<int:pk>/publish',views.publishPost,name='publishPost'),
    path('post/<int:pk>/unpublish',views.unpublishPost,name='unpublishPost'),
    ###################################  comments  ###############################
    path('post/<int:pk>/comment',views.add_comment,name='addComment'),
    path('post/<int:pk>/comment/approve',views.approve_comment,name='addComment'),
    path('post/<int:pk>/remove',views.remove_comment,name='addComment')

    
]   