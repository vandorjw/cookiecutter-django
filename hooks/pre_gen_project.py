"""
NOTE:
    the below code is to be maintained Python 3.6-compatible
"""

project_slug = '{{ cookiecutter.project_slug }}'
if hasattr(project_slug, 'isidentifier'):
    assert project_slug.isidentifier(), "'{}' project slug is not a valid Python identifier.".format(project_slug)

assert "\\" not in "{{ cookiecutter.author_name }}", "Don't include backslashes in author name."

