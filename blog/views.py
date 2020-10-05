from django.shortcuts import render, redirect
from .models import Post, BlogComment
from django.contrib import messages
from .templatetags import extras
from django.http import HttpResponseRedirect

# Create your views here.
def bloghome(request):
    allpost = Post.objects.all()
    context = {'allposts': allpost}
    return render(request, 'blog/blog.html', context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comment = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None) #exclude none ke alawa

    replyDict = {}
    for reply in replies:
        if reply.parent.id not in replyDict.keys():
            replyDict[reply.parent.id] = [reply]
        else:
            replyDict[reply.parent.id].append(reply)

    context = {
        'post':post, 
        'comment':comment,
        'replyDict':replyDict
    }
    return render(request, 'blog/blogpost.html',context)

def Postcomment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        postSno = request.POST['postSno']
        post = Post.objects.get(id=postSno)
        parent = request.POST['perentSno']

        if parent == "":
            Scomment = BlogComment(comment=comment, user=user, post=post)
            Scomment.save()
            messages.success(request, "Comment Added Successfully")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            parent = BlogComment.objects.get(id=parent)
            Scomment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            Scomment.save()
            messages.success(request, "Replay Added Successfully")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    return redirect('home')