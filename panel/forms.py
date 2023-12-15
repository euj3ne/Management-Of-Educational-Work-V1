from datetime import date, timezone
from django import forms
from .models import Teachers, Groups, Works, Students

class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = '__all__'
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванова'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Инна'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ивановна'}),
            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': '01.01.1901'}),
            'sex': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Женщина'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'г. Каменск-Шахтинский, х. Иваново, ул. Иванкино, д. 1, кв. 1'}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 111 222 33-44'}),
            'date_job': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': '01.01.1901'}),
            'job_post': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Директор'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Информатика'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name_mail@example.ru'})
        }

class GroupsForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = '__all__'
        widgets = {
            'number_group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '44СПО'}),
            'number_1_students': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '25'}),
            'date_1_creation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': '01.01.1901'}),
            'date_2_creation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': '01.01.1901'}),
            'data_teacher': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Иванова Инна Ивановна'}),
        }

class WorksForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = '__all__'
        widgets = {
            'number_work': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1'}),
            'date_1': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': '01.01.1901'}),
            'number_groupn': forms.Select(attrs={'class': 'form-control', 'placeholder': '44СПО'}),
            'number_1_students': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '20'}),
            'number_2_students': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '5'}),
            'description_work': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Культура мира'}),
        }

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванович'}),
            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': '01.01.1901'}),
            'sex': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Женщина'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'г. Каменск-Шахтинский, х. Иваново, ул. Иванкино, д. 1, кв. 1'}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 111 222 33-44'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name_mail@example.ru'}),
            'date_join': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': '01.01.1901'}),
            'date_leave': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': '01.01.1901'}),
            'number_group': forms.Select(attrs={'class': 'form-control', 'placeholder': '44СПО'}),
        }