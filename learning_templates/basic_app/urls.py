from django.urls import path
from . import views

# TEMPLATE TAGGING (This app_name is called in the html inside the <a>)
app_name = 'basic_app'

urlpatterns= [
    path("relative/",views.relative,name='relative'),
    path("other/",views.other,name='other'),
]
