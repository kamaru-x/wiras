from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Post(models.Model):
    Added_Date = models.DateTimeField(auto_now_add=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='Added_By')
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateField(null=True)
    EditedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,related_name='Edited_By')
    Edited_Ip = models.GenericIPAddressField(null=True)

    Post_Type = models.CharField(max_length=225)
    Post_Category = models.CharField(max_length=225)
    Post_Title = models.CharField(max_length=225)
    Post_Description = models.TextField()
    Post_Image = models.ImageField(upload_to='post/',null=True)

    Seo_Url = models.CharField(max_length=500,null=True)
    Seo_Title = models.CharField(max_length=225,null=True)
    Seo_Keywords = models.CharField(max_length=500,null=True)
    Seo_Description = models.TextField(null=True)

    def __str__(self):
        return f'{self.Post_Title}///{self.Added_Date}'
    

class Album(models.Model):
    Added_Date = models.DateTimeField(auto_now_add=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='AddedBy')
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateField(null=True)
    EditedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    Edited_Ip = models.GenericIPAddressField(null=True)

    Album_Category = models.CharField(max_length=225)
    Album_Title = models.CharField(max_length=225)

    Seo_Url = models.CharField(max_length=500,null=True)
    Seo_Title = models.CharField(max_length=225,null=True)
    Seo_Keywords = models.CharField(max_length=500,null=True)
    Seo_Description = models.TextField(null=True)

    def __str__(self):
        return f'{self.Album_Title}///{self.Added_Date}'
    

class Album_Image(models.Model):
    Added_Date = models.DateTimeField(auto_now_add=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Ip = models.GenericIPAddressField(null=True)

    Album = models.ForeignKey(Album,on_delete=models.DO_NOTHING)
    Image = models.ImageField(upload_to='alubum_images')

    def __str__(self):
        return f"{self.Image}///{self.Album}"
    

class Department(models.Model):
    Added_Date = models.DateTimeField(auto_now_add=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateField(null=True)
    EditedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,related_name='EditedBy')
    Edited_Ip = models.GenericIPAddressField(null=True)

    Department_Title = models.CharField(max_length=225)
    Department_Vission = models.TextField(null=True)
    Department_Mission = models.TextField(null=True)
    Department_Description = models.TextField(null=True)
    Department_Logo = models.ImageField(null=True)
    Department_Fecilities = models.TextField(null=True)
    Department_Placement = models.TextField(null=True)

    def __str__(self):
        return f'{self.Department_Title}///{self.Added_Date}'
    

class Course(models.Model):
    Added_Date = models.DateTimeField(auto_now_add=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateField(null=True)
    EditedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,related_name='Edited')
    Edited_Ip = models.GenericIPAddressField(null=True)

    Course_Type = models.CharField(max_length=225)
    Course_Department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    Course_Title = models.CharField(max_length=225)
    Course_Subject = models.CharField(max_length=225,null=True)
    Course_Complementary_Subject = models.CharField(max_length=225,null=True)
    Course_Duration = models.CharField(max_length=225,null=True)
    Course_Total_Seats = models.IntegerField(null=True)
    Course_Syllabus = models.FileField(null=True,upload_to='syllabus')

    def __str__(self):
        return f'{self.Course_Title}///{self.Added_Date}'
    

class Faculty(models.Model):
    Added_Date = models.DateTimeField(auto_now_add=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='Added')
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateField(null=True)
    EditedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    Edited_Ip = models.GenericIPAddressField(null=True)

    Faculty_Department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    Faculty_Name = models.CharField(max_length=225)
    Faculty_Designation = models.CharField(max_length=225,null=True)
    Faculty_Qualification = models.CharField(max_length=225,null=True)
    Faculty_Email = models.EmailField(max_length=225,null=True)
    Faculty_Image = models.ImageField(null=True,upload_to='faculties')

    def __str__(self):
        return f'{self.Faculty_Name}///{self.Faculty_Department}'
    

class Enquiry(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=225)
    Course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    DOB = models.DateField()
    Qualification = models.CharField(max_length=225)
    Mobile_Number = models.CharField(max_length=25)
    Email = models.EmailField(max_length=225,null=True)

    def __str__(self):
        return f'{self.Name}///{self.Date}'