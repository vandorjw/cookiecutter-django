"""
NOTE:
    the below code is to be maintained Python 3.6-compatible
"""

import os
import shutil


PROJECT_DIR_PATH = os.path.realpath(os.path.curdir)


def remove_celery_app():
    shutil.rmtree(os.path.join(PROJECT_DIR_PATH, '{{ cookiecutter.project_slug }}', 'taskapp'))


def append_to_project_gitignore(path):
    gitignore_file_path = os.path.join(PROJECT_DIR_PATH, '.gitignore')
    with open(gitignore_file_path, 'a') as gitignore_file:
        gitignore_file.write(path)
        gitignore_file.write(os.linesep)


def main():
    if '{{ cookiecutter.use_celery }}'.lower() == 'n':
        remove_celery_app()


if __name__ == '__main__':
    main()
