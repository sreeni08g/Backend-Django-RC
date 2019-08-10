from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    url(r'^rc/$', views.CreateView.as_view(), name="create"),
    url(r'^rcget/$', views.GetView.as_view(), name="get"),
}

urlpatterns = format_suffix_patterns(urlpatterns)