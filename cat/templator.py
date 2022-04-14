import os
from os.path import join
from jinja2 import Environment, FileSystemLoader


def render(template_name, folder='app/templates', **kwargs):
    file_path = join(folder, template_name)

    with open(file_path, encoding='utf-8') as f:
        template = Environment(loader=FileSystemLoader(folder)).from_string(f.read())

    return template.render(**kwargs)