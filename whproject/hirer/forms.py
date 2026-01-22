from django import forms
from .models import JobPost

class JobPostForm(forms.ModelForm):

    job_type = forms.ChoiceField(
        choices=[
            ("", "Select Job Type"),
            ("Full-Time", "Full-Time"),
            ("Part-Time", "Part-Time"),
            ("Internship", "Internship"),
        ],
        required=True
    )

    class Meta:
        model = JobPost
        fields = [
            'job_position', 'company_name', 'location', 'salary',
            'job_type', 'job_field', 'experience',
            'description', 'requirements',
            'phone', 'email'
        ]

        widgets = {
            'description': forms.Textarea(attrs={'style': 'width:100%; height:120px;'}),
            'requirements': forms.Textarea(attrs={'style': 'width:100%; height:120px;'}),
            'experience': forms.TextInput(attrs={'style': 'width:100%;'}),
            'job_position': forms.TextInput(attrs={'style': 'width:100%;'}),
            'company_name': forms.TextInput(attrs={'style': 'width:100%;'}),
            'location': forms.TextInput(attrs={'style': 'width:100%;'}),
            'salary': forms.TextInput(attrs={'style': 'width:100%;', 'inputmode': 'decimal'}),
            'phone': forms.TextInput(attrs={'style': 'width:100%;'}),
            'email': forms.EmailInput(attrs={'style': 'width:100%;'}),
        }