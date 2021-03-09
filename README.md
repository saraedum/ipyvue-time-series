ipyvue-time-series
==================

Real-Time Plots in Jupyter Notebooks and JupyterLab

Installation
------------

To install use pip:

    pip install ipyvue_time_series

Development
-----------

Install a local copy of this package:

    git clone https://github.com/saraedum/ipyvue-time-series.git
    cd ipyvue-time-series
    pip install -e .

When working with the classical notebook:

    jupyter nbextension install --py --symlink --overwrite --sys-prefix ipyvue_time_series
    jupyter nbextension enable --py --sys-prefix ipyvue_time_series

When working with JupyterLab:

    jupyter labextension develop --overwrite ipyvue_time_series

To rebuild the JavaScript code after making changes to anything in the `js/`
directory:

    cd js
    yarn run build
    cd ..
    pip install -e . --no-deps

You then need to refresh the Notebook/JupyterLab page for the changes to take effect.
