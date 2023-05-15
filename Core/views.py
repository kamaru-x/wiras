from django.shortcuts import render,redirect
from Core.models import Post
from Core.pre_fun import setip

# Create your views here.

#------------------------------------------------- add post --------------------------------------------#

def add_post(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        category = request.POST.get('category')
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        seo_url = request.POST.get('seo_url')
        seo_title = request.POST.get('seo_title')
        seo_keywords = request.POST.get('seo_keyword')
        seo_description = request.POST.get('seo_description')

        Post.objects.create(AddedBy=request.user,Ip=setip(request),Post_Type=type,Post_Category=category,Post_Title=title,Post_Description=description,Post_Image=image,Seo_Url=seo_url,Seo_Title=seo_title,Seo_Keywords=seo_keywords,Seo_Description=seo_description)
        return redirect('list-post')

    return render(request,'admin/post-add.html')

#------------------------------------------------- list post --------------------------------------------#

def list_post(request):
    posts = Post.objects.filter(Status=1)
    return render(request,'admin/post-list.html',{'posts':posts})

#------------------------------------------------- edit post --------------------------------------------#

def edit_post(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            post.Post_Image = request.FILES['image']
        post.Post_Type = request.POST.get('type')
        post.Post_Category = request.POST.get('category')
        post.Post_Title = request.POST.get('title')
        post.Post_Description = request.POST.get('description')
        post.Seo_Url = request.POST.get('seo_url')
        post.Seo_Title = request.POST.get('seo_title')
        post.Seo_Keywords = request.POST.get('seo_keyword')
        post.Seo_Description = request.POST.get('seo_description')
        post.save()
        return redirect('list-post')
    return render(request,'admin/post-edit.html',{'post':post})