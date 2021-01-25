from django.conf.urls import url
from leadship import views

urlpatterns = [
    url(r'^$', views.test_hullform),
]
