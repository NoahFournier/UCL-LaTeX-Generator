from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.conf import settings

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
            supervisor_bool = form.is_supervisor_needed()
            latex_renderer = LatexRenderer()
            if supervisor_bool:
                template = 'title_page.tex'
            else:
                template = 'title_page_nosupervisor.tex'
            latex_renderer.compile_tex_to_pdf(template, **form.cleaned_data)
            return HttpResponseRedirect('/download')
    else:
        form = FieldsForm()
    
    return render(request, 'pytex/index.html', {'form':form})

def download(request):
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'output/out.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            destroy_output()
            response = HttpResponse(fh.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=cover_page.pdf'
            return response
    raise Http404 
