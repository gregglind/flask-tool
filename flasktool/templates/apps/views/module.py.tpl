from flask import Module, render_template, request, session, g

{{module_name}} = Module(__name__{% if module_name != 'main' %}, url_prefix='/{{module_name}}'{% endif %})

@{{module_name}}.route('/')
def index():
    return "Index of {{module_name}}."
