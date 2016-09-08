from __future__ import absolute_import, unicode_literals, print_function, division

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dataset/upload/(?P<pk>\d+)/?$', views.UploadDataSetView.as_view(), name='dataset_upload'),
]
