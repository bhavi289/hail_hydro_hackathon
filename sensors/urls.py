from django.conf.urls import url

from . import views

from django.contrib.auth import views as v
app_name = 'sensors'

urlpatterns = [
	
    url(r'^logdata/$', views.sensor_data.as_view(), name = 'sensor_data'),
    url(r'^data/logout/$', v.logout , {'next_page': '/'}, name='logout'),
    url(r'^data/$', views.show_list, name = 'data'),
]
