from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("student", views.student, name="student"),
    path("student/modal_edit/<int:student_id>", views.modal_edit, name="modal_edit"),
    path("student/modal_delete/<int:student_id>", views.modal_delete, name="modal_delete")
]
