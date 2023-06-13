from django.shortcuts import render,redirect
from Core.models import Post,Album,Album_Image,Department,Course,Faculty,Enquiry,Contact_message,Complaints,Exam_Schedules,Exam_Results,News_letter,Admission,Alumni_Registration
from Core.pre_fun import setip
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

#------------------------------------------------- add post --------------------------------------------#

@login_required
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

        try:
            Post.objects.get(Seo_Url=seo_url)
            messages.error(request,'post with same url already exists')
            return redirect('.')
        except:
            Post.objects.create(AddedBy=request.user,Ip=setip(request),Post_Type=type,Post_Category=category,Post_Title=title,Post_Description=description,Post_Image=image,Seo_Url=seo_url,Seo_Title=seo_title,Seo_Keywords=seo_keywords,Seo_Description=seo_description)
            return redirect('list-post')

    return render(request,'admin/post-add.html',{'departments':departments})

#------------------------------------------------- list post --------------------------------------------#

@login_required
def list_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        post.Status = 0
        post.save()
        return redirect('list-post')
    
    p = Paginator(Post.objects.filter(Status=1).order_by('-id'),10)
    page = request.GET.get('page')
    posts = p.get_page(page)
    nums = 'a' * posts.paginator.num_pages
    return render(request,'admin/post-list.html',{'posts':posts,'nums':nums})

#------------------------------------------------- View post --------------------------------------------#

@login_required
def view_post(request,post_id):
    post = Post.objects.get(id=post_id)
    return render(request,'admin/post-view.html',{'post':post})

#------------------------------------------------- edit post --------------------------------------------#

@login_required
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

    return redirect('/admin/edit-post/%s/' %post_id)

#------------------------------------------------- create album ------------------------------------------#

@login_required
def create_album(request):
    departments = Department.objects.filter(Status=1).order_by('-id')
    if request.method == 'POST':
        category = request.POST.get('category')
        title = request.POST.get('title')
        cover = request.FILES.get('cover')
        seo_url = request.POST.get('seo_url')
        seo_title = request.POST.get('seo_title')
        seo_keywords = request.POST.get('seo_keywords')
        seo_description = request.POST.get('seo_description')
        
        try:
            Album.objects.get(Seo_Url=seo_url)
            messages.error(request,'album with same name already exists')
            return redirect('.')
        except:
            Album.objects.create(AddedBy=request.user,Ip=setip(request),Album_Category=category,Album_Title=title,Cover_Image=cover,
                                Seo_Url=seo_url,Seo_Title=seo_title,Seo_Keywords=seo_keywords,Seo_Description=seo_description)
            return redirect ('list-albums')
        
    return render(request,'admin/album-create.html',{'departments':departments})

#------------------------------------------------- list album --------------------------------------------#

@login_required
def list_albums(request):
    albums = []
    alb = Album.objects.filter(Status=1).order_by('-id')
    for a in alb:
        images = Album_Image.objects.filter(Album=a).count()
        album = {'id':a.id,'title':a.Album_Title,'category':a.Album_Category,'date':a.Added_Date,'images':images}
        albums.append(album)

    if request.method == 'POST':
        if request.POST.get('album_id'):
            album_id = request.POST.get('album_id')
            album  = Album.objects.get(id=album_id)
            album.delete()
            return redirect('.')
        
        if request.POST.get('a_id'):
            a_id = request.POST.get('a_id')
            images = request.FILES.getlist('images')
            album = Album.objects.get(id=a_id)

            for img in images: 
                Album_Image.objects.create(AddedBy=request.user,Ip=setip(request),Album=album,Image=img)
                print('object saved .... !')
            return redirect('list-albums')
    
    return render(request,'admin/album-list.html',{'albums':albums})

#------------------------------------------------- view album --------------------------------------------#

@login_required
def view_album(request,album_id):
    album = Album.objects.get(id=album_id)
    images = Album_Image.objects.filter(Album=album)
    return render(request,'admin/album-view.html',{'album':album,'images':images})

#------------------------------------------------- edit album --------------------------------------------#

@login_required
def edit_album(request,album_id):
    album = Album.objects.get(id=album_id)
    images = Album_Image.objects.filter(Album=album)
    departments = Department.objects.filter(Status=1).order_by('-id')
    if request.method == 'POST':
        if len(request.FILES) != 0:
            album.Cover_Image = request.FILES['cover']
        if request.POST.get('image_id'):
            image_id = request.POST.get('image_id')
            image = Album_Image.objects.get(id=image_id)
            image.delete()
            return redirect('/admin/edit-album/%s/' %album.id)
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

@login_required
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

@login_required
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

        try:
            Department.objects.get(Seo_Url=seo_url)
            messages.error(request,'department with same name already exists')
            return redirect ('.')
        except:
            Department.objects.create(AddedBy=request.user,Ip=setip(request),Department_Title=title,Department_Vission=vision,Department_Mission=mission,
                                    Department_Logo=logo,Department_Fecilities=facilities,Department_Placement=placement,
                                    Department_Description=description,Seo_Url=seo_url,Seo_Title=seo_title,Seo_Keywords=seo_keywords,
                                    Seo_Description=seo_description)
            return redirect('list-departments')
    return render(request,'admin/department-add.html')

#------------------------------------------------- list departments --------------------------------------------#

@login_required
def list_departments(request):
    # departments = Department.objects.filter(Status=1).order_by('-id')
    if request.method == 'POST':
        department_id = request.POST.get('department_id')
        department = Department.objects.get(id=department_id)
        department.Status = 0
        department.save()
        return redirect('list-departments')
    p = Paginator(Department.objects.filter(Status=1).order_by('-id'),10)
    page = request.GET.get('page')
    departments = p.get_page(page)
    nums = 'a' * departments.paginator.num_pages
    return render(request,'admin/departments-list.html',{'departments':departments,'nums':nums})

#------------------------------------------------- view departments --------------------------------------------#

@login_required
def view_department(request,department_id):
    department = Department.objects.get(id=department_id)
    faculties = Faculty.objects.filter(Faculty_Department=department)
    courses = Course.objects.filter(Course_Department=department)
    return render(request,'admin/department-view.html',{'department':department,'faculties':faculties,'courses':courses})

#------------------------------------------------- edit departments --------------------------------------------#

@login_required
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

@login_required
def remove_department_img(request,department_id):
    department = Department.objects.get(id=department_id)

    department.Department_Logo.delete(save=True)
    department.save()

    return redirect('/admin/edit-department/%s/' %department_id)

#------------------------------------------------- add course --------------------------------------#

@login_required
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
        image = request.FILES.get('image')
        seo_url = request.POST.get('seo_url')
        seo_title = request.POST.get('seo_title')
        seo_keywords = request.POST.get('seo_keywords')
        seo_description = request.POST.get('seo_description')

        try:
            Course.objects.get(Seo_Url=seo_url)
            messages.error(request,'course with same name already exists')
            return redirect('.')
        except:
            Course.objects.create(AddedBy=request.user,Ip=setip(request),Course_Type=type,Course_Department=department,
                                Course_Title=title,Course_Subject=subject,Course_Complementary_Subject=complimentary,
                                Course_Duration=duration,Course_Total_Seats=seats,Course_Syllabus=syllabus,
                                Seo_Url=seo_url,Seo_Title=seo_title,Seo_Keywords=seo_keywords,Seo_Description=seo_description,Course_Image=image)
            return redirect('list-course')
    return render(request,'admin/cources-add.html',{'departments':departments})

#------------------------------------------------- list course --------------------------------------#

@login_required
def list_course(request):
    # courses = Course.objects.filter(Status=1).order_by('-id')
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = Course.objects.get(id=course_id)
        course.Status = 0
        course.save()
        return redirect('list-course')
    p = Paginator(Course.objects.filter(Status=1).order_by('-id'),10)
    page = request.GET.get('page')
    courses = p.get_page(page)
    nums = 'a' * courses.paginator.num_pages
    return render(request,'admin/cources-list.html',{'courses':courses,'nums':nums})

#------------------------------------------------- view course --------------------------------------#

@login_required
def view_cource(request,course_id):
    course = Course.objects.get(id=course_id)
    return render(request,'admin/course-view.html',{'course':course})

#------------------------------------------------- edit course --------------------------------------#

@login_required
def edit_course(request,course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if request.FILES.get('syllabus') :
                course.Course_Syllabus = request.FILES.get('syllabus')
            if request.FILES.get('image'):
                course.Course_Image = request.FILES.get('image')
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

@login_required
def remove_course_image(request,course_id):
    course = Course.objects.get(id=course_id)

    course.Course_Image.delete(save=True)
    course.save()

    return redirect('/admin/edit-course/%s/' %course_id)

#------------------------------------------------- add faculty --------------------------------------#

@login_required
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

@login_required
def list_faculties(request):
    # faculties = Faculty.objects.filter(Status=1).order_by('-id')
    if request.method == 'POST':
        faculty_id = request.POST.get('faculty_id')
        faculty = Faculty.objects.get(id=faculty_id)
        faculty.Status = 0
        faculty.save()
        return redirect('list-faculties')
    p = Paginator(Faculty.objects.filter(Status=1).order_by('-id'),10)
    page = request.GET.get('page')
    faculties = p.get_page(page)
    nums = 'a' * faculties.paginator.num_pages
    return render(request,'admin/faculty-list.html',{'faculties':faculties,'nums':nums})

#------------------------------------------------- view faculty --------------------------------------#

@login_required
def view_faculty(request,faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    return render(request,'admin/faculty-view.html',{'faculty':faculty})

#------------------------------------------------- edit faculty --------------------------------------#

@login_required
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

@login_required
def remove_faculty_image(request,faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    faculty.Faculty_Image.delete(save=True)
    faculty.save()
    return redirect('/admin/edit-faculty/%s/' %faculty_id)

#------------------------------------------------- edit faculty --------------------------------------#

@login_required
def admission_enquiries(request):
    return render(request,'admin/admission-enquiries.html')

#------------------------------------------------- enquiries list --------------------------------------#

@login_required
def enquiries(request):
    enquiries = Contact_message.objects.all()
    return render(request,'admin/enquiries.html',{'enquiries':enquiries})

#------------------------------------------------- complaints list --------------------------------------#

@login_required
def complaints(request):
    complaints = Complaints.objects.all()
    return render(request,'admin/complaints.html',{'complaints':complaints})

#------------------------------------------------- complaints list --------------------------------------#

@login_required
def view_complaint(request,complaint_id):
    complaint = Complaints.objects.get(id=complaint_id)
    return render(request,'admin/view-complaint.html',{'complaint':complaint})

#------------------------------------------------- news latter list --------------------------------------#

@login_required
def news_emails(request):
    newslatters = News_letter.objects.filter(Status=1)
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        email = News_letter.objects.get(id=email_id)
        email.Status = 0
        email.save()
        return redirect('.')
    return render(request,'admin/newslatter.html',{'newslatters':newslatters})

#------------------------------------------------- Admission List --------------------------------------#

@login_required
def admission_requests(request):
    requests = Admission.objects.filter(Status=1)
    if request.method == 'POST':
        admission_id = request.POST.get('admission_id')
        admission = Admission.objects.get(id=admission_id)
        admission.Status = 1
        admission.save()
        return redirect('.')
    return render(request,'admin/admission-requests.html',{'requests':requests})

#------------------------------------------------- View Admission --------------------------------------#

@login_required
def view_admission(request,admission_id):
    admission = Admission.objects.get(id=admission_id)
    return render(request,'admin/admission-view.html',{'admission':admission})

#------------------------------------------------- Alumni Registration ---------------------------------#

@login_required
def alumni_registrations(request):
    registrations = Alumni_Registration.objects.all()
    if request.method == 'POST':
        alumni_id = request.POST.get('alumni_id')
        alumni = Alumni_Registration.objects.get(id=alumni_id)
        alumni.Status = 0
        alumni.save()
        return redirect('.')
    return render(request,'admin/alumni-registrations.html',{'registrations':registrations})

#------------------------------------------------- Alumni View --------------------------------------------#

@login_required
def view_alumni(request,alumni_id):
    alumni = Alumni_Registration.objects.get(id=alumni_id)
    return render(request,'admin/alumni-view.html',{'alumni':alumni})

#------------------------------------------------- exam schedule list --------------------------------------#

@login_required
def exam_schedule_list(request):
    schedules = Exam_Schedules.objects.exclude(Status=0)
    if request.method == 'POST':
        if request.POST.get('schedule_id'):
            schedule_id = request.POST.get('schedule_id')
            schedule = Exam_Schedules.objects.get(id=schedule_id)
            schedule.Status = 0
            schedule.save()
            return redirect('.')

        if request.POST.get('hs_id'):
            hs_id = request.POST.get('hs_id')
            schedule = Exam_Schedules.objects.get(id=hs_id)
            status = schedule.Status
            if status == 1:
                schedule.Status = 3
            elif status == 3:
                schedule.Status = 1
            schedule.save()
            return redirect('.')
    return render(request,'admin/exam-schedule-list.html',{'schedules':schedules})

#------------------------------------------------- exam schedule add --------------------------------------#

@login_required
def exam_schedule_add(request):
    if request.method == 'POST':
        tite = request.POST.get('title')
        schedule = request.FILES.get('schedule')
        Exam_Schedules.objects.create(Title=tite,Schedule=schedule)
        return redirect('list-exam-schedules')

    return render(request,'admin/exam-schedule-add.html')

#------------------------------------------------- exam schedule edit --------------------------------------#

@login_required
def exam_schedule_edit(request,schedule_id):
    schedule = Exam_Schedules.objects.get(id=schedule_id)
    if request.method == 'POST':
        schedule.Title = request.POST.get('title')
        if len(request.FILES) != 0:
            schedule.Schedule = request.FILES['schedule']
        schedule.save()
        return redirect('list-exam-schedules')

    return render(request,'admin/exam-schedule-edit.html',{'schedule':schedule})

#------------------------------------------------- exam results list --------------------------------------#

@login_required
def exam_result_list(request):
    results = Exam_Results.objects.exclude(Status=0)
    if request.method == 'POST':
        if request.POST.get('result_id'):
            result_id = request.POST.get('result_id')
            result = Exam_Results.objects.get(id=result_id)
            result.Status = 0
            result.save()
            return redirect('.')
        if request.POST.get('hr_id'):
            hr_id = request.POST.get('hr_id')
            result = Exam_Results.objects.get(id=hr_id)
            status = result.Status
            if status == 1:
                result.Status = 3
            elif status == 3:
                result.Status = 1
            result.save()
            return redirect('.')
    return render(request,'admin/exam-results-list.html',{'results':results})

#------------------------------------------------- exam results add --------------------------------------#

@login_required
def exam_result_add(request):
    if request.method == 'POST':
        tite = request.POST.get('title')
        result = request.FILES.get('result')
        Exam_Results.objects.create(Title=tite,Result=result)
        return redirect('list-exam-results')
    return render(request,'admin/exam-results-add.html')

#------------------------------------------------- exam results edit --------------------------------------#

@login_required
def exam_result_edit(request,result_id):
    result = Exam_Results.objects.get(id=result_id)
    if request.method == 'POST':
        result.Title = request.POST.get('title')
        if len(request.FILES) != 0:
            result.Result = request.FILES['result']
        result.save()
        return redirect('list-exam-results')
    return render(request,'admin/exam-results-edit.html',{'result':result})