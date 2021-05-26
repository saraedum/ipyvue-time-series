from ipywidgets.widgets.widget import widget_serialization
from traitlets import Unicode, Any
from ipyvue import VueTemplate
from ipyvue_remote_component import RemoteComponent

from .comm_widget import CommWidget
from .force_load import force_load

class TimeSeries(VueTemplate, CommWidget, RemoteComponent):
    r"""
    A Time Series Plot.

    The plot is initially empty. Use `push` to add points the plot interactively.
    """
    __force = Any(force_load, read_only=True).tag(sync=True, **widget_serialization)
    template = Unicode(r"""
    <time-series v-slot="{ x, y }">
        <remote-component url="https://unpkg.com/vue-plotly@1.1.0/dist/vue-plotly.umd.min.js" integrity="sha384-3YjbENL4Izchmbn7RCdWL5tHYGPP7fy2B/vzCgBd3corbolRfPgjimXK4JEwGpYg" :extract="library => library.Plotly" :props="{
            data: [{ x: [...x], y: [...y], type: 'scatter' }],
            'display-mode-bar': false }" />
    </time-series>
    """).tag(sync=True)

    def _create_client(self, comm):
        r"""
        Called when a frontend client connects, i.e., when a plot starts to be
        shown in the frontend. See `CommWidget` for details.

        Return a client object that can be used to synchronize data with the
        frontend.
        """
        from .buffering_client import BufferingClient
        return BufferingClient(comm)

    def push(self, x, y):
        r"""
        Add the point `(x, y)` to the plot.
        """
        for client in self._clients:
            client.push({
                "x": x,
                "y": y,
            })
