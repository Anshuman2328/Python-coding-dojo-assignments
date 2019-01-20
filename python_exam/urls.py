from django.conf.urls import url,include

urlpatterns = [
    url(r'^', include('apps.app_one.urls')),
    url(r'^exam/', include('apps.exam_one.urls')),

]
