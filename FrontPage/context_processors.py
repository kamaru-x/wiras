from Core.models import Department
from datetime import datetime

def extras(request):
    departments = Department.objects.filter(Status=1)
    date = datetime.today()
    year = date.year
    return {'departments':departments,'year':year}