from django.conf.urls import patterns, url
from share.views import EmailFormView

urlpatterns = patterns('',
  url(r'^email/$', EmailFormView.as_view(), name='share_email'),
)
