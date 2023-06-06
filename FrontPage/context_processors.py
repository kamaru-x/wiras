from Core.models import Department

def extras(request):
    departments = Department.objects.filter(Status=1)
    return {'departments':departments}