 
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns=[
    url(r'^ifsc/(?P<ifsc>\w+)$', views.ifsc_details, name='ifsc'),
    url(r'^branches/(?P<bank>[-\w]+)/(?P<city>[-\w]+)$', views.details_of_branches, name='branches'),
]
urlpatterns = format_suffix_patterns(urlpatterns)