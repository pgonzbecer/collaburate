# Created by Paul Gonzalez Becerra

from django.conf.urls import url

from . import views

urlpatterns=    [
    url(r"^$", views.index, name="index")
]

# End of File