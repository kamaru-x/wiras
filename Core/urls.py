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

    #------------------------------- faculty urls ---------------------------------#

    path('enquiries/',views.enquiries,name='enquiries'),
    path('complaints/',views.complaints,name='complaints-list'),
]