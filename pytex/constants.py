import os

SUPERVISOR_TITLES = [
    ('Dr.', 'Dr.'),
    ('Mr.', 'Mr.'),
    ('Ms.', 'Ms.'),
    ('Professor', 'Professor'),
]

SPECIAL_CHARACTERS = {
    '\\': '\\textbackslash',
    '&': '\&',
    '$': '\$',
    '#': '\#',
    '%': '\%',
    '_': '\_',
    '}': '\}',
    '{': '\{',
    '~': '\\textasciitilde',
    '^': '\\textasciicircum',
}

def get_color_pairs():
    COLOUR_PAIRS = []
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/pytex/latex/assets/')
    for file in sorted(os.listdir(path)):
        pair = (file, file.replace('_', ' ').replace('.png', '').title())
        COLOUR_PAIRS.append(pair)
    return COLOUR_PAIRS