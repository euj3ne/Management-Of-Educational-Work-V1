from django.urls import path
from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.index, name='index'),

    path('teachers', views.teachers_index, name='teachers_index'),
    path('teachers/list', views.teachers_list, name='teachers_list'),
    path('teachers/add', views.teachers_add, name='teachers_add'),
    path('teachers/<int:pk>/remove_confirmation', views.teachers_remove_confirmation, name='teachers_remove_confirmation'),
    path('teachers/<int:pk>/remove', views.teachers_remove, name='teachers_remove'),
    path('teachers/<int:pk>/edit', views.teachers_edit, name='teachers_edit'),

    path('groups', views.groups_index, name='groups_index'),
    path('groups/list', views.groups_list, name='groups_list'),
    path('groups/add', views.groups_add, name='groups_add'),
    path('groups/<int:pk>/remove_confirmation', views.groups_remove_confirmation, name='groups_remove_confirmation'),
    path('groups/<int:pk>/remove', views.groups_remove, name='groups_remove'),
    path('groups/<int:pk>/edit', views.groups_edit, name='groups_edit'),

    path('works', views.works_index, name='works_index'),
    path('works/list', views.works_list, name='works_list'),
    path('works/add', views.works_add, name='works_add'),
    path('works/<int:pk>/remove_confirmation', views.works_remove_confirmation, name='works_remove_confirmation'),
    path('works/<int:pk>/remove', views.works_remove, name='works_remove'),
    path('works/<int:pk>/edit', views.works_edit, name='works_edit'),

    path('students', views.students_index, name='students_index'),
    path('students/list', views.students_list, name='students_list'),
    path('students/add', views.students_add, name='students_add'),
    path('students/<int:pk>/remove_confirmation', views.students_remove_confirmation,name='students_remove_confirmation'),
    path('students/<int:pk>/remove', views.students_remove, name='students_remove'),
    path('students/<int:pk>/edit', views.students_edit, name='students_edit'),

]