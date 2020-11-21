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
    student_number = forms.CharField(label='Student number', max_length=8, required=False)
    course_name = forms.CharField(label='Course name', max_length=200, required=False, empty_value='')
    module_name = forms.CharField(label='Module name', max_length=200, required=False, empty_value='')
    assignment_title = forms.CharField(label='Assignment Title', max_length=200)
    supervisor_title = forms.ChoiceField(
        label='Supervisor Title', #
        choices=SUPERVISOR_TITLES
    )
    supervisor_first_name = forms.CharField(label='Supervisor First Name', max_length=100, required=False, empty_value='')
    supervisor_last_name = forms.CharField(label='Supervisor Last Name', max_length=100, required=False, empty_value='')
    date = forms.BooleanField(label='Date', required=False)
    banner_color = forms.ChoiceField(label="Banner Color", choices=COLOUR_PAIRS)

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
    
    def is_supervisor_needed(self):
        """Returns True if either Supervisor fields have been filled, False otherwise."""
        if not self.cleaned_data['supervisor_first_name'] and not self.cleaned_data['supervisor_last_name']:
            return False
        else:
            return True
