from django.contrib import admin
from Core.models import Post,Album,Album_Image,Department,Course,Faculty,Enquiry

# Register your models here.

admin.site.register(Post)
admin.site.register(Album)
admin.site.register(Album_Image)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Enquiry)