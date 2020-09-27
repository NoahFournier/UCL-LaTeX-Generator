import os
import jinja2 
from subprocess import Popen
import tempfile
import shutil
import glob


class LatexRenderer():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    OUTPUT_DIR = os.path.join(BASE_DIR, 'output/')
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'static/pytex/latex/')

    def __init__(self):
        self.latex_jinja_env = jinja2.Environment(
            block_start_string='\BLOCK{',
            block_end_string='}',
            variable_start_string='\VAR{',
            variable_end_string='}',
            comment_start_string='\#{',
            comment_end_string='}',
            line_statement_prefix='%%',
            line_comment_prefix='%#',
            trim_blocks=True,
            autoescape=False,
            loader=jinja2.FileSystemLoader(self.TEMPLATES_DIR)
        )

    def render_tex(self, filename, **fields):
        template = self.latex_jinja_env.get_template(filename)
        rendered_tex = template.render(**fields)
        return rendered_tex

    def print_template(self, template):
        print(self.latex_jinja_env.loader.get_source(self.latex_jinja_env, template)[0])
    
    def compile_tex_to_pdf(self, filename, **fields):
        out_path = self.OUTPUT_DIR
        rendered_tex = self.render_tex(filename, **fields)
        self.compile_template(rendered_tex, out_path)

    def compile_template(self, rendered_tex, output_path):
        tmp_dir = tempfile.mkdtemp(dir=self.BASE_DIR)
        in_tmp_path = os.path.join(tmp_dir, 'rendered_tex')
        with open(in_tmp_path, 'w') as outfile:
            outfile.write(rendered_tex)
        out_tmp_path = os.path.join(self.BASE_DIR, 'out.pdf')
        p = Popen(['pdflatex', '-jobname', 'out', in_tmp_path], cwd=self.BASE_DIR)
        p.communicate()
        shutil.copy(out_tmp_path, output_path)
        shutil.rmtree(tmp_dir)
    
    
def destroy_output():
    #add code for destroying temp folders
    for file in glob.glob('pytex/out.*'):
            try:
                os.remove(file)
                print('Removing : ' + file)
            except:
                print('Error when removing file : ' + file)
    for file in glob.glob('pytex/output/out.*'):
        try:
            os.remove(file)
            print('Removing : ' + file)
        except:
            print('Error when removing file : ' + file)