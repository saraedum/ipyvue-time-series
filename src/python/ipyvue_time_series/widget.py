import ipywidgets as widgets
from traitlets import Unicode

from traitlets import Unicode
from ipyvue import VueTemplate

from .comm_widget import CommWidget, Client

class TimeSeries(VueTemplate, CommWidget):
    template = Unicode(r"""
    <time-series v-slot="{ x, y }">
        <remote-component url="https://unpkg.com/vue-plotly@^1/dist/vue-plotly.umd.min.js" :extract="library => library.Plotly" :props="{
            data: [{ x: [...x], y: [...y], type: 'scatter' }],
            'display-mode-bar': false }" />
    </time-series>
    """).tag(sync=True)

    def create_client(self, comm):
        return BufferingClient(comm)

    def push(self, x, y):
        for client in self._clients:
            client.push({
                "x": x,
                "y": y,
            })

class BufferingClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._buffer = []

    def push(self, frame):
        self._buffer.append(frame)
        if not self._ready:
            # TODO: Promise instead
            return
        frames = self._buffer[:]
        self._buffer = []
        self.send({
            "command": "push",
            "frames": frames,
        })

