from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns=[
    path('',views.createpost.as_view()),
    path('accounts/',include('django.contrib.auth.urls'))
]