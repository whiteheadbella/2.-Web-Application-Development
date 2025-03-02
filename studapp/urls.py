from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("add/", views.add_student, name='add_student'),
    path("update/<int:student_id>/", views.update_student, name="update_student"),
    path("delete/<int:id>/", views.delete_student, name="delete_student"),
]