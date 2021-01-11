from django.conf.urls import url
from students import views

urlpatterns = [
    url(r'^$', views.list),
]
