from django.conf.urls import url
from leadship import views

urlpatterns = [
    url('ShipMainParticular/', views.create),
]
