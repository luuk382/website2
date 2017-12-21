from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recipe_list/(?P<c>\d+)/$', views.recipe_list, name='recipe_list'),
    url(r'^recipe/(?P<pk>\d+)/$', views.recipe, name='recipe'),
    url(r'^construction/$', views.construction, name='construction'),
]
