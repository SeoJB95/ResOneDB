from django.shortcuts import render
from leadship.models import *
import glob
import pickle
import sys
import pprint
#from HGB_project import *
# Create your views here.
def test_hullform(request):
    with open('/workspace/data/DS2500TEU_2.proj','rb') as f:
        project = pickle.load(f)
    Hull = project.hull['DS2500TEU_forPaper']
    json = Hull.ToJson()
    return render(request, 'importHull.html',{'testjson':json})

def create(request):
    ships = ShipMainParticular.objects.order_by('ship_size')

    return render(request, 'ship_main.html',{'ship_input':ships})
    pass
