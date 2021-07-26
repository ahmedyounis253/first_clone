from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView
from . import models
from django.utils import timezone
from . import forms
############# posts 
class createpost(LoginRequiredMixin ,CreateView):
    def form_valid(self, form) :
        print(self.request.user)
        object=form.save(commit=False)
        object.author=self.request.user
        object.create_time=timezone.now()
        object.save()

        return super(createpost,self).form_valid(form)

       
    form_class=forms.PostForm
    template_name='post_form.html'
    redirect_field_name='post/'
    model=models.Post


class UpdatePost(LoginRequiredMixin,UpdateView):
    model=models.Post
    form_class=forms.PostForm
    template_name='post_form.html'


class PostList(LoginRequiredMixin , ListView):
    model=models.Post
    template_name="post_list.html"
    def get_queryset(self):
        return models.Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
class draftPost(LoginRequiredMixin,ListView):
    def get_queryset(self):
        return models.Post.objects.filter(published_date__isnull=True, author=self.request.user).order_by('-create_time')
    template_name="post_list.html"
    model=models.Post
@login_required
def publishPost(request,pk):
    post=get_object_or_404(models.Post,pk=pk)
    post.publish()
    return redirect('blog:postdetails',pk=pk)
@login_required
def unpublishPost(request,pk):
    post=get_object_or_404(models.Post,pk=pk)
    post.published_date=None
    post.save()
    return redirect('blog:postdetails',pk=pk)
class PostDetials(LoginRequiredMixin,DetailView):
    model=models.Post
    template_name='post_details.html'




class DeletePost(LoginRequiredMixin,DeleteView):
    model=models.Post
    success_url='/posts'
    template_name='post_delete.html'




#################
#### comments 

@login_required
def add_comment(request,pk):

    post=get_object_or_404(models.Post,pk=pk)
    if request.method=="POST":
        form=forms.CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.author=request.user
            comment.save()
            return redirect('/post/{}'.format(comment.post.id))
    else:
        form=forms.CommentForm()
    return render(request,'comment_form.html',{'form':form})


@login_required
def approve_comment(request,pk):
    comment=get_object_or_404(models.Comment,pk=pk)
    comment.approve()
    return redirect('/post/{}'.format(comment.post.id))

@login_required
def remove_comment(request,pk):
    comment=get_object_or_404(models.Comment,pk=pk)
    post_pk=comment.post.id
    comment.delete()
    return redirect('postdetails',pk=post_pk)