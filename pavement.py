import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys

from sphinxcontrib import paverutils

sys.path.append(os.getcwd())

home_dir = os.getcwd()
master_url = 'http://127.0.0.1:8000'
master_app = 'runestone'
serving_dir = "./build/Teacher-CSP"

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/Teacher-CSP",
        sourcedir="_sources",
        outdir="./build/Teacher-CSP",
        confdir=".",
        project_name = "Teacher-CSP",
        template_args={'course_id': 'TeacherCSP',
                       'login_required':'true',
                       'appname':master_app,
                       'loglevel': 0,
                       'course_url':master_url,
                       'use_services': 'true',
                       'python3': 'true'
                        }
    )
)

from runestone import build  # build is called implicitly by the paver driver.

