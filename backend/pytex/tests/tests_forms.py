from django.test import SimpleTestCase, TestCase
from pytex.forms import FieldsForm, clean_charfield

from pytex.constants import SPECIAL_CHARACTERS, SUPERVISOR_TITLES, get_color_pairs

class FormTestCase(SimpleTestCase):

    def test_clean_charfield_special_characters(self):
        """
        clean_charfield() should clean text data, replacing special characters
        with LaTeX-safe alternatives.
        """
        data = '\\ & $ # % _ } { ~ ^'
        expected_outcome = '\\textbackslash \& \$ \# \% \_ \} \{ \\textasciitilde \\textasciicircum'
        self.assertEqual(clean_charfield(data, SPECIAL_CHARACTERS), expected_outcome)
    
    def test_clean_charfield_strip(self):
        """
        clean_charfield() should strip spaces from either end of string.
        """
        data = '  test  '
        expected_outcome = 'test'
        self.assertEqual(clean_charfield(data, SPECIAL_CHARACTERS), expected_outcome)
    
    def test_is_supervisor_needed_both_fields_empty(self):
        """
        is_supervisor_needed() should return False if no supervisor first name or
        last name has been specified
        """
        form = FieldsForm(data={
            'first_name':'First', #Required
            'last_name':'Last', #Required
            'assignment_title':'Title', #Required
            'supervisor_first_name':'', #Optional
            'supervisor_last_name':'', #Optional
        })
        form.is_valid()
        self.assertFalse(form.is_supervisor_needed())
    
    def test_is_supervisor_needed_one_field_empty(self):
        """
        is_supervisor_needed() should return True if supervisor has either no first name
        or no last name, and if supervisor has both a first and last name
        """
        form1 = FieldsForm(data={
            'first_name':'First', #Required
            'last_name':'Last', #Required
            'assignment_title':'Title', #Required
            'supervisor_first_name':'First-Supervisor', #Optional
            'supervisor_last_name':'', #Optional
        })
        form2 = FieldsForm(data={
            'first_name':'First', #Required
            'last_name':'Last', #Required
            'assignment_title':'Title', #Required
            'supervisor_first_name':'', #Optional
            'supervisor_last_name':'Last-Supervisor', #Optional
        })
        form1.is_valid()
        form2.is_valid()
        self.assertTrue(form1.is_supervisor_needed())
        self.assertTrue(form2.is_supervisor_needed())
    
    def test_is_supervisor_needed_both_fields_filled(self):
        form3 = FieldsForm(data={
            'first_name':'First', #Required
            'last_name':'Last', #Required
            'assignment_title':'Title', #Required
            'supervisor_first_name':'First-Supervisor', #Optional
            'supervisor_last_name':'Last-Supervisor', #Optional
        })
        form3.is_valid()
        self.assertTrue(form3.is_supervisor_needed())