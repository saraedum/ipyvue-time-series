ipyvue-time-series
===============================

Real-Time Data Plotting in Jupyter

Installation
------------

To install use pip:

    $ pip install ipyvue_time_series
    $ jupyter nbextension enable --py --sys-prefix ipyvue_time_series

To install for jupyterlab

    $ jupyter labextension install ipyvue_time_series

For a development installation (requires npm),

    $ git clone https://github.com/saraedum/ipyvue-time-series.git
    $ cd ipyvue-time-series
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix ipyvue_time_series
    $ jupyter nbextension enable --py --sys-prefix ipyvue_time_series
    $ jupyter labextension install js

When actively developing your extension, build Jupyter Lab with the command:

    $ jupyter lab --watch

This take a minute or so to get started, but then allows you to hot-reload your javascript extension.
To see a change, save your javascript, watch the terminal for an update.

Note on first `jupyter lab --watch`, you may need to touch a file to get Jupyter Lab to open.

