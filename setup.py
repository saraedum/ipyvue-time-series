from __future__ import print_function
from setuptools import setup, find_packages
import os
from os.path import join as pjoin
from distutils import log

from jupyter_packaging import (
    create_cmdclass,
    install_npm,
    ensure_targets,
    combine_commands,
)


here = os.path.dirname(os.path.abspath(__file__))

log.set_verbosity(log.DEBUG)
log.info('setup.py entered')
log.info('$PATH=%s' % os.environ['PATH'])

name = 'ipyvue_time_series'
LONG_DESCRIPTION = 'Real-Time Plots in Jupyter Notebooks and JupyterLab'

js_dir = pjoin(here, 'js')

# Representative files that should exist after a successful build
jstargets = [
    pjoin(js_dir, 'dist', 'index.js'),
]

data_files_spec = [
    ('share/jupyter/nbextensions/ipyvue-time-series', 'ipyvue_time_series/nbextension', '*.*'),
    ('share/jupyter/labextensions/ipyvue-time-series', 'ipyvue_time_series/labextension', "**"),
    ("share/jupyter/labextensions/ipyvue-time-series", '.', "install.json"),
    ('etc/jupyter/nbconfig/notebook.d', '.', 'ipyvue-time-series.json'),
]

cmdclass = create_cmdclass('jsdeps', data_files_spec=data_files_spec)
cmdclass['jsdeps'] = combine_commands(
    install_npm(js_dir, npm=['yarn'], build_cmd='build:prod'), ensure_targets(jstargets),
)

setup_args = dict(
    name=name,
    version="1.0.0",
    description='Real-Time Plots in Jupyter Notebooks and JupyterLab',
    long_description=LONG_DESCRIPTION,
    include_package_data=True,
    install_requires=[
        'ipyvue-remote-component>=1.1.0',
    ],
    packages=find_packages(),
    zip_safe=False,
    cmdclass=cmdclass,
    author='Julian Rüth',
    author_email='julian.rueth@fsfe.org',
    url='https://github.com/saraedum/ipyvue-time-series',
    keywords=[
        'ipython',
        'jupyter',
        'widgets',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

setup(**setup_args)
