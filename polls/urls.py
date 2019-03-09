from django.urls import re_path

from . import views


urlpatterns = [
    re_path(
        r'^$',
        views.IndexView.as_view(),
        name='index'
    ),
    re_path(
        r'^(?P<pk>[0-9]+)/$',
        views.DetailView.as_view(),
        name='detail'
    ),
    re_path(
        r'^(?P<pk>[0-9]+)/delete/$',
        views.DeleteView.as_view(),
        name='delete'
    ),
]
