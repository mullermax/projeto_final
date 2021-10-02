from django.urls import path
from .views import person_list
from .views import person_new
from .views import persons_update
from .views import persons_delete


urlpatterns = [
    path('list/', person_list, name="person_list"),
    path('new/', person_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
]
