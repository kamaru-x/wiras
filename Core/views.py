from django.shortcuts import render,redirect
from Core.models import Post,Album,Album_Image,Department,Course,Faculty
from Core.pre_fun import setip
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#------------------------------------------------- add post --------------------------------------------#

def add_post(request):
    departments = Department.objects.filter(Status=1).order_by('-id')
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

    return render(request,'admin/post-add.html',{'departments':departments})

#------------------------------------------------- list post --------------------------------------------#

def list_post(request):
    posts = Post.objects.filter(Status=1).order_by('-id')
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        post.Status = 0
        post.save()
        return redirect('list-post')
    return render(request,'admin/post-list.html',{'posts':posts})

#------------------------------------------------- edit post --------------------------------------------#

def edit_post(request,post_id):
    departments = Department.objects.filter(Status=1).order_by('-id')
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
    return render(request,'admin/post-edit.html',{'post':post,'departments':departments})

#------------------------------------------------- delete post image  ------------------------------------------#

@login_required
def remove_post_img(request,post_id):
    post = Post.objects.get(id=post_id)

    post.Post_Image.delete(save=True)
    post.save()

    return redirect('/edit-post/%s/' %post_id)

#------------------------------------------------- create album ------------------------------------------#

def create_album(request):
    departments = Department.objects.filter(Status=1).order_by('-id')
    if request.method == 'POST':
        category = request.POST.get('category')
        title = request.POST.get('title')
        seo_url = request.POST.get('seo_url')
        seo_title = request.POST.get('seo_title')
        seo_keywords = request.POST.get('seo_keywords')
        seo_description = request.POST.get('seo_description')
        Album.objects.create(AddedBy=request.user,Ip=setip(request),Album_Category=category,Album_Title=title,
                             Seo_Url=seo_url,Seo_Title=seo_title,Seo_Keywords=seo_keywords,Seo_Description=seo_description)
        return redirect ('list-albums')
    return render(request,'admin/album-create.html',{'departments':departments})

#------------------------------------------------- list album --------------------------------------------#

def list_albums(request):
    albums = []
    alb = Album.objects.filter(Status=1).order_by('-id')
    for a in alb:
        images = Album_Image.objects.filter(Album=a).count()
        album = {'id':a.id,'title':a.Album_Title,'category':a.Album_Category,'date':a.Added_Date,'images':images}
        albums.append(album)
    return render(request,'admin/album-list.html',{'albums':albums})

#------------------------------------------------- edit album --------------------------------------------#

def edit_album(request,album_id):
    album = Album.objects.get(id=album_id)
    images = Album_Image.objects.filter(Album=album)
    departments = Department.objects.filter(Status=1).order_by('-id')
    if request.method == 'POST':
        if request.POST.get('image_id'):
            image_id = request.POST.get('image_id')
            image = Album_Image.objects.get(id=image_id)
            image.delete()
            return redirect('/edit-album/%s/' %album.id)
        else:
            album.Album_Title = request.POST.get('title')
            album.Album_Category = request.POST.get('category')
            album.Seo_Url = request.POST.get('seo_url')
            album.Seo_Title = request.POST.get('seo_title')
            album.Seo_Keywords = request.POST.get('seo_keywords')
            album.Seo_Description = request.POST.get('seo_description')
            album.save()
            return redirect('list-albums')

    return render(request,'admin/album-edit.html',{'album':album,'images':images,'departments':departments})

#------------------------------------------------- add image to album --------------------------------------------#

def upload_image(request):
    albums = Album.objects.filter(Status=1)
    if request.method == 'POST':
        album_id = request.POST.get('album')
        images = request.FILES.getlist('images')

        album = Album.objects.get(id=album_id)

        for img in images: 
            Album_Image.objects.create(AddedBy=request.user,Ip=setip(request),Album=album,Image=img)
        return redirect('list-albums')
    return render(request,'admin/upload_image.html',{'albums':albums})

#------------------------------------------------- add department --------------------------------------------#

def add_department(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        logo = request.FILES.get('logo')
        vision = request.POST.get('vision')
        mission = request.POST.get('mission')
        facilities = request.POST.get('facilities')
        placement = request.POST.get('placement')
        description = request.POST.get('description')
        seo_url = request.POST.get('seo_url')
        seo_title = request.POST.get('seo_title')
        seo_keywords = request.POST.get('seo_keywords')
        seo_description = request.POST.get('seo_description')
        Department.objects.create(AddedBy=request.user,Ip=setip(request),Department_Title=title,Department_Vission=vision,Department_Mission=mission,
                                  Department_Logo=logo,Department_Fecilities=facilities,Department_Placement=placement,
                                  Department_Description=description,Seo_Url=seo_url,Seo_Title=seo_title,Seo_Keywords=seo_keywords,
                                  Seo_Description=seo_description)
        return redirect('list-departments')
    return render(request,'admin/department-add.html')

#------------------------------------------------- list departments --------------------------------------------#

def list_departments(request):
    departments = Department.objects.filter(Status=1).order_by('-id')
    if request.method == 'POST':
        department_id = request.POST.get('department_id')
        department = Department.objects.get(id=department_id)
        department.Status = 0
        department.save()
        return redirect('list-departments')
    return render(request,'admin/departments-list.html',{'departments':departments})

#------------------------------------------------- edit departments --------------------------------------------#

def edit_department(request,department_id):
    department = Department.objects.get(id=department_id)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            department.Department_Logo = request.FILES['logo']
        department.Department_Title = request.POST.get('title')
        department.Department_Vission = request.POST.get('vision')
        department.Department_Mission = request.POST.get('mission')
        department.Department_Fecilities = request.POST.get('facilities')
        department.Department_Placement = request.POST.get('placement')
        department.Department_Description = request.POST.get('description')
        department.Seo_Url = request.POST.get('seo_url')
        department.Seo_Title = request.POST.get('seo_title')
        department.Seo_Keywords = request.POST.get('seo_keywords')
        department.Seo_Description = request.POST.get('seo_description')
        department.save()
        return redirect('list-departments')
    return render(request,'admin/department-edit.html',{'department':department})

#------------------------------------------------- delete department logo --------------------------------------#

def remove_department_img(request,department_id):
    department = Department.objects.get(id=department_id)

    department.Department_Logo.delete(save=True)
    department.save()

    return redirect('/edit-department/%s/' %department_id)

#------------------------------------------------- add course --------------------------------------#

def add_cources(request):
    departments = Department.objects.filter(Status=1)
    if request.method == 'POST':
        type = request.POST.get('type')
        dep = request.POST.get('department')
        department = Department.objects.get(id=dep)
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        complimentary = request.POST.get('complimentary')
        duration = request.POST.get('duration')
        seats = request.POST.get('seats')
        syllabus = request.FILES.get('syllabus')
        seo_url = request.POST.get('seo_url')
        seo_title = request.POST.get('seo_title')
        seo_keywords = request.POST.get('seo_keywords')
        seo_description = request.POST.get('seo_description')
        Course.objects.create(AddedBy=request.user,Ip=setip(request),Course_Type=type,Course_Department=department,
                              Course_Title=title,Course_Subject=subject,Course_Complementary_Subject=complimentary,
                              Course_Duration=duration,Course_Total_Seats=seats,Course_Syllabus=syllabus,
                              Seo_Url=seo_url,Seo_Title=seo_title,Seo_Keywords=seo_keywords,Seo_Description=seo_description)
        return redirect('list-course')
    return render(request,'admin/cources-add.html',{'departments':departments})

#------------------------------------------------- list course --------------------------------------#

def list_course(request):
    courses = Course.objects.filter(Status=1).order_by('-id')
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = Course.objects.get(id=course_id)
        course.Status = 0
        course.save()
        return redirect('list-course')
    return render(request,'admin/cources-list.html',{'courses':courses})

#------------------------------------------------- edit course --------------------------------------#

def edit_course(request,course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            course.Course_Syllabus = request.FILES['syllabus']
        course.Course_Type = request.POST.get('type')
        dep = request.POST.get('department')
        department = Department.objects.get(id=dep) 
        course.Course_Department = department
        course.Course_Title = request.POST.get('title')
        course.Course_Subject = request.POST.get('subject')
        course.Course_Complementary_Subject = request.POST.get('complimentary')
        course.Course_Duration = request.POST.get('duration')
        course.Course_Total_Seats = request.POST.get('seats')
        course.Seo_Url = request.POST.get('seo_url')
        course.Seo_Title = request.POST.get('seo_title')
        course.Seo_Keywords = request.POST.get('seo_keywords')
        course.Seo_Description = request.POST.get('seo_description')
        course.save()
        return redirect('list-course')
    return render(request,'admin/cources-edit.html',{'course':course})

#------------------------------------------------- remove course image ------------------------------#

def remove_course_image(request,course_id):
    course = Course.objects.get(id=course_id)

    course.Course_Syllabus.delete(save=True)
    course.save()

    return redirect('/edit-course/%s/' %course_id)

#------------------------------------------------- add faculty --------------------------------------#

def add_faculty(request):
    departments = Department.objects.filter(Status=1)
    if request.method == 'POST':
        dep = request.POST.get('department')
        department = Department.objects.get(id=dep)
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        qualification = request.POST.get('qualification')
        email = request.POST.get('email')
        photo = request.FILES.get('photograph')
        Faculty.objects.create(AddedBy=request.user,Ip=setip(request),Faculty_Department=department,Faculty_Name=name,
                               Faculty_Designation=designation,Faculty_Qualification=qualification,Faculty_Email=email,
                               Faculty_Image=photo)
        return redirect('list-faculties')
    return render(request,'admin/faculty-add.html',{'departments':departments})

#------------------------------------------------- list faculty --------------------------------------#

def list_faculties(request):
    faculties = Faculty.objects.filter(Status=1).order_by('-id')
    if request.method == 'POST':
        faculty_id = request.POST.get('faculty_id')
        faculty = Faculty.objects.get(id=faculty_id)
        faculty.Status = 0
        faculty.save()
        return redirect('list-faculties')
    return render(request,'admin/faculty-list.html',{'faculties':faculties})

#------------------------------------------------- edit faculty --------------------------------------#

def edit_faculties(request,faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    departments = Department.objects.filter(Status=1)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            faculty.Faculty_Image = request.FILES['photograph']
        dep = request.POST.get('department')
        department = Department.objects.get(id=dep)
        faculty.Faculty_Department = department
        faculty.Faculty_Name = request.POST.get('name')
        faculty.Faculty_Designation = request.POST.get('designation')
        faculty.Faculty_Qualification = request.POST.get('qualification')
        faculty.Faculty_Email = request.POST.get('email')
        faculty.save()
        return redirect('list-faculties')
    return render(request,'admin/faculty-edit.html',{'faculty':faculty,'departments':departments})

#------------------------------------------------- edit faculty --------------------------------------#

def remove_faculty_image(request,faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    faculty.Faculty_Image.delete(save=True)
    faculty.save()
    return redirect('/edit-faculty/%s/' %faculty_id)

#------------------------------------------------- edit faculty --------------------------------------#

def admission_enquiries(request):
    return render(request,'admin/admission-enquiries.html')