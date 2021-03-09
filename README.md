ipyvue-time-series
===============================

Real-Time Plots in Jupyter Notebooks and JupyterLab

Installation
------------

To install use pip:

    $ pip install ipyvue_time_series

For a development installation (requires [Node.js](https://nodejs.org) and [Yarn version 1](https://classic.yarnpkg.com/)),

    $ git clone https://github.com/saraedum/ipyvue-time-series.git
    $ cd ipyvue-time-series
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --overwrite --sys-prefix ipyvue_time_series
    $ jupyter nbextension enable --py --sys-prefix ipyvue_time_series

When actively developing your extension for JupyterLab, run the command:

    $ jupyter labextension develop --overwrite ipyvue_time_series

Then you need to rebuild the JS when you make a code change:

    $ cd js
    $ yarn run build

You then need to refresh the JupyterLab page when your javascript changes.
