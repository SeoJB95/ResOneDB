from django.shortcuts import render
from DBLoading.models import *
import glob
import pickle
import sys
from HGB_project import *
# Create your views here.
def list(request):
    #students = InformationTable.objects.all()

    with open('/workspace/data/DS2500TEU_2.proj','rb') as f:
        project = pickle.load(f)
    Hull = project.hull['DS2500TEU_forPaper']
    #json=Hull.STEM.curve.ToJson()
    json = Hull.ToJson()
    #raise ValueError(Hull.stations.linesF)
    #return render(request, 'feedbacklist.html', {'feedbacks': students})
    return render(request, 'importHull.html',{'testjson':json})
def create(resquest):
    pass
