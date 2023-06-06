from Core.models import Department

def extras(request):
    departments = Department.objects.all()
    return {'departments':departments}