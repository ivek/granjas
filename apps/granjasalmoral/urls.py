from django.conf.urls import url, include
from apps.granjasalmoral.views import index
urlpatterns = [
    url(r'^$', index),
]
