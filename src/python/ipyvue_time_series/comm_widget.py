from ipywidgets import DOMWidget
from traitlets import Unicode
from ipykernel.comm import Comm

class CommWidget(DOMWidget):
    target = Unicode().tag(sync=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.target = f"{self.model_id}-comm-widget"

        self._clients = set()
        self._commands = {}

        self.command("register", self.register)

        self._register_target()

    def command(self, command, callback):
        self._commands[command] = callback

    def _receive(self, message):
        data = message["content"]["data"]
        command = data["command"]

        if command not in self._commands:
            raise NotImplementedException(f"Unsupported command {command}")

        self._commands[command](data)

    def register(self, data):
        comm = Comm(target_name=data["target"])
        self._clients.add(self.create_client(comm))

    def create_client(self, comm):
        raise NotImplementedException("create_client() needs to be overridden by implementing classes")

    def _register_target(self):
        def configure_comm(comm, open_msg):
            @comm.on_msg
            def _recv(msg): self._receive(msg)

        self.comm.kernel.comm_manager.register_target(self.target, configure_comm)

class Client:
    def __init__(self, comm):
        self._comm = comm

        # TODO: We treat every message as an ACK
        @comm.on_msg
        def _recv(msg): self._ready = True

        self._ready = True

    def send(self, data):
        if not self._ready:
            raise NotImplementedError("Cannot send when client is not ready");
        self._ready = False
        self._comm.send(data)
