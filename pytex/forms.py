from django import forms

from .constants import SUPERVISOR_TITLES, SPECIAL_CHARACTERS, get_color_pairs

COLOUR_PAIRS = get_color_pairs()

def clean_charfield(data, special_characters):
    data = data.strip()
    for character_old, character_new in special_characters.items():
        if character_old in data:
            data = data.replace(character_old, character_new)
    return data

class FieldsForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    course_name = forms.CharField(label='Course name', max_length=200, required=False, empty_value=' ')
    module_name = forms.CharField(label='Module name', max_length=200, required=False, empty_value=' ')
    assignment_title = forms.CharField(label='Assignment Title', max_length=200)
    supervisor_title = forms.CharField(
        label='Supervisor Title', #
        max_length=5,
        widget=forms.Select(choices=SUPERVISOR_TITLES)
    )
    supervisor_first_name = forms.CharField(label='Supervisor First Name', max_length=100, required=False, empty_value=' ')
    supervisor_last_name = forms.CharField(label='Supervisor Last Name', max_length=100, required=False, empty_value=' ')
    banner_color = forms.CharField(widget=forms.Select(choices=COLOUR_PAIRS),max_length=25)

    def clean_first_name(self):
        data = clean_charfield(self.cleaned_data['first_name'], SPECIAL_CHARACTERS)
        return data
    
    def clean_last_name(self):
        data = clean_charfield(self.cleaned_data['last_name'], SPECIAL_CHARACTERS)
        return data
    
    def clean_course_name(self):
        data = clean_charfield(self.cleaned_data['course_name'], SPECIAL_CHARACTERS)
        return data

    def clean_module_name(self):
        data = clean_charfield(self.cleaned_data['module_name'], SPECIAL_CHARACTERS)
        return data

    def clean_assignment_title(self):
        data = clean_charfield(self.cleaned_data['assignment_title'], SPECIAL_CHARACTERS)
        return data
    
    def clean_supervisor_first_name(self):
        data = clean_charfield(self.cleaned_data['supervisor_first_name'], SPECIAL_CHARACTERS)
        return data

    def clean_supervisor_last_name(self):
        data = clean_charfield(self.cleaned_data['supervisor_last_name'], SPECIAL_CHARACTERS)
        return data

