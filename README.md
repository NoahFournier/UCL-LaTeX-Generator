# UCL-Latex-Generator

## To run on local server :

- Git clone on local repo

From parent folder, run : 
- python -m venv .venv
- source .venv/bin/activate
- pip install -r requirements.txt

- Use this link to generate a secret key : https://djecrety.ir/
- Copy secret key as a string into latex_generator/.env_template and rename file to .env
- python manage.py migrate
- python manage.py runserver

- Navigate to http://127.0.0.1:8000/

To do :

- Style page
- Make forms more user friendly (dropdowns/checklist)
- Introduce more .tex templates
- Write more tests
- Add sub-header at bottom of page