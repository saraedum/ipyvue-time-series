from setuptools import setup
import os.path

setup(**{
    'name': 'ipyvue_time_series',
    'version': '0.1.0',
    'description': 'Real-Time Data Plotting in Jupyter',
    'long_description': 'Real-Time Data Plotting in Jupyter',
    'include_package_data': True,
    'data_files': [
        ('share/jupyter/nbextensions/ipyvue-time-series', [
            'generated/notebook/javascript/extension.js',
            'generated/notebook/javascript/widget.js',
            'generated/notebook/javascript/widget.js.map',
        ],),
        ('etc/jupyter/nbconfig/notebook.d' ,['assets/notebook/ipyvue-time-series.json'])
    ],
    'install_requires': [
        'ipywidgets>=7.0.0',
    ],
    'packages': ['ipyvue_time_series'],
    'zip_safe': False,
    'author': 'Julian Rüth',
    'author_email': 'julian.rueth@fsfe.org',
    'url': 'https://github.com/saraedum/ipyvue-time-series',
    'keywords': [
        'ipython',
        'jupyter',
        'widgets',
        'plotly',
        'timeseries',
        'vue',
    ],
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
})
