from django.urls import path
from Core import views

urlpatterns = [
    path('add-post/',views.add_post,name='add-post'),
    path('list-post/',views.list_post,name='list-post'),
    path('edit-post/<int:post_id>',views.edit_post,name='edit-post'),
]