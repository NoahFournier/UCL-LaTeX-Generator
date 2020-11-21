from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseServerError
from django.conf import settings

from subprocess import TimeoutExpired

import os

from .forms import FieldsForm
from .renderer import LatexRenderer, destroy_output

# Create your views here.
def get_fields(request):
    if request.method == 'POST':
        form = FieldsForm(request.POST)
        if form.is_valid():
            # check data and pass into latex rendered
            # return downloaded .pdf
            form.cleaned_data['supervisor_bool'] = form.is_supervisor_needed()
            latex_renderer = LatexRenderer()
            errs = latex_renderer.compile_tex_to_pdf('title_page.tex', **form.cleaned_data)
            if errs:
                return render(
                    request, 
                    'pytex/index.html',
                    {'error_message': 'Request timed out.',
                    'form': FieldsForm()}
                )
            return HttpResponseRedirect('/download')
    else:
        form = FieldsForm()
    
    return render(request, 'pytex/index_text.html', {'form':form})

def download(request):
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'output/out.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            destroy_output()
            response = HttpResponse(fh.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=cover_page.pdf'
            return response
    raise Http404 
