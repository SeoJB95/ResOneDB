from django.shortcuts import render
from DBLoading.models import *
# Create your views here.
def list(request):
    students = InformationTable.objects.all()
    return render(request, 'feedbacklist.html', {'feedbacks': students})
def create(resquest):
    pass
