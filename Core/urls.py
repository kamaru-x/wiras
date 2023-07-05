from django.urls import path
from Core import views

urlpatterns = [

    # ------------------------------- post urls ---------------------------------#

    path('add-post/',views.add_post,name='add-post'),
    path('list-post/',views.list_post,name='list-post'),
    path('view-post/<int:post_id>/',views.view_post,name='view-post'),
    path('edit-post/<int:post_id>/',views.edit_post,name='edit-post'),
    path('remove-post-image/<int:post_id>/',views.remove_post_img,name='remove-post-image'),
    
    #------------------------------- album urls ---------------------------------#

    path('create-album/',views.create_album,name='create-album'),
    path('list-albums/',views.list_albums,name='list-albums'),
    path('view-album/<int:album_id>/',views.view_album,name='view-album'),
    path('edit-album/<int:album_id>/',views.edit_album,name='edit-album'),
    path('upload-images/',views.upload_image,name='upload-images'),
    path('delete_cover_image/<int:album_id>/',views.delete_cover_image, name='delete_cover_image'),

    #------------------------------- album urls ---------------------------------#

    path('add-department/',views.add_department,name='add-department'),
    path('list-departments/',views.list_departments,name='list-departments'),
    path('view-department/<int:department_id>/',views.view_department,name='view-department'),
    path('edit-department/<int:department_id>/',views.edit_department,name='edit-department'),
    path('delete-department-logo/<int:department_id>/',views.remove_department_img,name='remove-department-image'),

    #------------------------------- course urls ---------------------------------#

    path('add-course/',views.add_cources,name='add-course'),
    path('list-courses/',views.list_course,name='list-course'),
    path('view-course/<int:course_id>/',views.view_cource,name='view-course'),
    path('edit-course/<int:course_id>/',views.edit_course,name='edit-course'),
    path('delete-course-image/<int:course_id>/',views.remove_course_image,name='remove-course-image'),

    #------------------------------- faculty urls ---------------------------------#

    path('add-faculty/',views.add_faculty,name='add-faculty'),
    path('list-faculties/',views.list_faculties,name='list-faculties'),
    path('view-faculty/<int:faculty_id>/',views.view_faculty,name='view-faculty'),
    path('edit-faculty/<int:faculty_id>/',views.edit_faculties,name='edit-faculty'),
    path('delete-faculty-image/<int:faculty_id>/',views.remove_faculty_image,name='remove-faculty-image'),

    #------------------------------- registration urls ---------------------------------#

    path('enquiries/',views.enquiries,name='enquiries'),
    path('complaints/',views.complaints,name='complaints-list'),
    path('view-complaint/<str:complaint_id>/',views.view_complaint,name='view-complaint'),
    path('newslatter/',views.news_emails,name='newslatters'),
    path('admission-requests/',views.admission_requests,name='admission-requests'),
    path('view-admission/<str:admission_id>',views.view_admission,name='view-admission'),
    path('alumni_registrations/',views.alumni_registrations,name='alumni-registrations'),
    path('view-alumni/<str:alumni_id>',views.view_alumni,name='view-alumni'),

    #------------------------------- exams urls ----------------------------------------#

    path('list-exam-schedules/',views.exam_schedule_list,name='list-exam-schedules'),
    path('add-exam-schedules/',views.exam_schedule_add,name='add-exam-schedules'),
    path('edit-exam-schedules/<str:schedule_id>',views.exam_schedule_edit,name='edit-exam-schedules'),

    path('list-exam-results/',views.exam_result_list,name='list-exam-results'),
    path('add-exam-results/',views.exam_result_add,name='add-exam-results'),
    path('edit-exam-results/<str:result_id>/',views.exam_result_edit,name='edit-exam-results'),
]