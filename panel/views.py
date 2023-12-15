import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from .models import Teachers, Groups, Works, Students
from .forms import TeachersForm, GroupsForm, WorksForm, StudentsForm


@login_required(login_url=reverse_lazy('login:login'))
def index(request):
    return render(request, 'index.html', {})


#---------------------------------------------------------Views Teachers---------------------------------------------------------
@login_required(login_url=reverse_lazy('login:login'))
def teachers_index(request):
    return render(request, 'teachers/index.html', {})
@login_required(login_url=reverse_lazy('login:login'))
def teachers_list(request):
    teachers = Teachers.objects.all()
    return render(request, 'teachers/list.html', {'teachers': teachers})
@login_required(login_url=reverse_lazy('login:login'))
def teachers_add(request):
    if request.method == "POST":
        form = TeachersForm(request.POST)
        if form.is_valid():
            teachers = Teachers.objects.create(
                surname = form.cleaned_data.get('surname'),
                name = form.cleaned_data.get('name'),
                middle_name = form.cleaned_data.get('middle_name'),
                birthday = form.cleaned_data.get('birthday'),
                sex = form.cleaned_data.get('sex'),
                address = form.cleaned_data.get('address'),
                telephone_number = form.cleaned_data.get('telephone_number'),
                job_post = form.cleaned_data.get('job_post'),
                date_job = form.cleaned_data.get('date_job'),
                subject = form.cleaned_data.get('subject'),
                email = form.cleaned_data.get('email')
            )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "teachersListChanged": None,
                        "showMessage": f"{teachers.surname} добавлена."
                    })
                })
        else:
            return render(request, 'teachers/form.html', {
                'form': form,
            })
    else:
        form = TeachersForm()
    return render(request, 'teachers/form.html', {
        'form': form,
    })
@login_required(login_url=reverse_lazy('login:login'))
def teachers_edit(request, pk):
    teachers = get_object_or_404(Teachers, pk=pk)
    if request.method == "POST":
        form = TeachersForm(request.POST, instance=teachers)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "teachersListChanged": None,
                        "showMessage": f"{teachers.surname} {teachers.name} {teachers.middle_name} обновлен."
                    })
                }
            )
    else:
        form = TeachersForm(instance=teachers)

    return render(request, 'teachers/form.html', {
        'form': form,
        'teachers': teachers,
    })
@login_required(login_url=reverse_lazy('login:login'))
def teachers_remove_confirmation(request, pk):
    teachers = get_object_or_404(Teachers, pk=pk)
    return render(request, 'teachers/delete_confirmation.html', {
        'teachers': teachers,
    })
@login_required(login_url=reverse_lazy('login:login'))
@ require_POST
def teachers_remove(request, pk):
    teachers = get_object_or_404(Teachers, pk=pk)
    teachers.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "teachersListChanged": None,
                "showMessage": f"{teachers.surname} удален(а,ы)."
            })
        })



# ---------------------------------------------------------Views Groups---------------------------------------------------------
@login_required(login_url=reverse_lazy('login:login'))
def groups_index(request):
    return render(request, 'groups/index.html', {})
@login_required(login_url=reverse_lazy('login:login'))
def groups_list(request):
    groups = Groups.objects.all()
    return render(request, 'groups/list.html', {'groups': groups})
@login_required(login_url=reverse_lazy('login:login'))
def groups_add(request):
    if request.method == "POST":
        form = GroupsForm(request.POST)
        if form.is_valid():
            groups = Groups.objects.create(
                number_group = form.cleaned_data.get('number_group'),
                number_1_students = form.cleaned_data.get('number_1_students'),
                date_1_creation = form.cleaned_data.get('date_1_creation'),
                date_2_creation = form.cleaned_data.get('date_2_creation'),
                data_teacher = form.cleaned_data.get('data_teacher'),
            )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "groupsListChanged": None,
                        "showMessage": f"{groups.number_group} добавлена."
                    })
                })
        else:
            return render(request, 'groups/form.html', {
                'form': form,
            })
    else:
        form = GroupsForm()
    return render(request, 'groups/form.html', {
        'form': form,
    })
@login_required(login_url=reverse_lazy('login:login'))
def groups_edit(request, pk):
    groups = get_object_or_404(Groups, pk=pk)
    if request.method == "POST":
        form = GroupsForm(request.POST, instance=groups)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "groupsListChanged": None,
                        "showMessage": f"{groups.number_group} обновлен."
                    })
                }
            )
    else:
        form = GroupsForm(instance=groups)

    return render(request, 'groups/form.html', {
        'form': form,
        'groups': groups,
    })
@login_required(login_url=reverse_lazy('login:login'))
def groups_remove_confirmation(request, pk):
    groups = get_object_or_404(Groups, pk=pk)
    return render(request, 'groups/delete_confirmation.html', {
        'groups': groups,
    })
@login_required(login_url=reverse_lazy('login:login'))
@ require_POST
def groups_remove(request, pk):
    groups = get_object_or_404(Groups, pk=pk)
    groups.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "groupsListChanged": None,
                "showMessage": f"{groups.number_group} удален(а,ы)."
            })
        })


# ---------------------------------------------------------Views Works---------------------------------------------------------
@login_required(login_url=reverse_lazy('login:login'))
def works_index(request):
    return render(request, 'works/index.html', {})
@login_required(login_url=reverse_lazy('login:login'))
def works_list(request):
    works = Works.objects.all()
    return render(request, 'works/list.html', {'works': works})
@login_required(login_url=reverse_lazy('login:login'))
def works_add(request):
    if request.method == "POST":
        form = WorksForm(request.POST)
        if form.is_valid():
            works = Works.objects.create(
                number_work = form.cleaned_data.get('number_work'),
                date_1 = form.cleaned_data.get('date_1'),
                number_1_students = form.cleaned_data.get('number_1_students'),
                number_2_students = form.cleaned_data.get('number_2_students'),
                description_work = form.cleaned_data.get('description_work'),
                number_groupn = form.cleaned_data.get('number_groupn'),
            )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "worksListChanged": None,
                        "showMessage": f"{works.number_work} добавлена."
                    })
                })
        else:
            return render(request, 'works/form.html', {
                'form': form,
            })
    else:
        form = WorksForm()
    return render(request, 'works/form.html', {
        'form': form,
    })
@login_required(login_url=reverse_lazy('login:login'))
def works_edit(request, pk):
    works = get_object_or_404(Works, pk=pk)
    if request.method == "POST":
        form = WorksForm(request.POST, instance=works)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "worksListChanged": None,
                        "showMessage": f"{works.number_work} обновлен."
                    })
                }
            )
    else:
        form = WorksForm(instance=works)

    return render(request, 'works/form.html', {
        'form': form,
        'works': works,
    })
@login_required(login_url=reverse_lazy('login:login'))
def works_remove_confirmation(request, pk):
    works = get_object_or_404(Works, pk=pk)
    return render(request, 'works/delete_confirmation.html', {
        'works': works,
    })
@login_required(login_url=reverse_lazy('login:login'))
@ require_POST
def works_remove(request, pk):
    works = get_object_or_404(Works, pk=pk)
    works.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "worksListChanged": None,
                "showMessage": f"{works.number_work} удален(а,ы)."
            })
        })

# ---------------------------------------------------------Views Students---------------------------------------------------------
@login_required(login_url=reverse_lazy('login:login'))
def students_index(request):
    return render(request, 'students/index.html', {})
@login_required(login_url=reverse_lazy('login:login'))
def students_list(request):
    students = Students.objects.all()
    return render(request, 'students/list.html', {'students': students})
@login_required(login_url=reverse_lazy('login:login'))
def students_add(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            students = Students.objects.create(
                surname = form.cleaned_data.get('surname'),
                name = form.cleaned_data.get('name'),
                middle_name = form.cleaned_data.get('middle_name'),
                birthday = form.cleaned_data.get('birthday'),
                sex = form.cleaned_data.get('sex'),
                address = form.cleaned_data.get('address'),
                telephone_number = form.cleaned_data.get('telephone_number'),
                date_join = form.cleaned_data.get('date_join'),
                date_leave = form.cleaned_data.get('date_leave'),
                number_group = form.cleaned_data.get('number_group'),
                email = form.cleaned_data.get('email')
            )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "studentsListChanged": None,
                        "showMessage": f"{students.surname} {students.name} {students.middle_name} добавлена."
                    })
                })
        else:
            return render(request, 'students/form.html', {
                'form': form,
            })
    else:
        form = StudentsForm()
    return render(request, 'students/form.html', {
        'form': form,
    })
@login_required(login_url=reverse_lazy('login:login'))
def students_edit(request, pk):
    students = get_object_or_404(Students, pk=pk)
    if request.method == "POST":
        form = StudentsForm(request.POST, instance=students)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "studentsListChanged": None,
                        "showMessage": f"{students.surname} {students.name} {students.middle_name} обновлен."
                    })
                }
            )
    else:
        form = StudentsForm(instance=students)

    return render(request, 'students/form.html', {
        'form': form,
        'students': students,
    })
@login_required(login_url=reverse_lazy('login:login'))
def students_remove_confirmation(request, pk):
    students = get_object_or_404(Students, pk=pk)
    return render(request, 'students/delete_confirmation.html', {
        'students': students,
    })
@login_required(login_url=reverse_lazy('login:login'))
@ require_POST
def students_remove(request, pk):
    students = get_object_or_404(Students, pk=pk)
    students.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "studentsListChanged": None,
                "showMessage": f"{students.surname} {students.name} {students.middle_name} удален(а,ы)."
            })
        })