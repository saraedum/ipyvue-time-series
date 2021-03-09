from .client import Client

class BufferingClient(Client):
    r"""
    A communication channel to the frontend that buffers data and sends it in
    chunks until the client has acknowledged the receipt of the previous chunk.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._buffer = []

    def push(self, frame):
        r"""
        Add a ``frame`` to the next chunk of data to be sent.
        """
        self._buffer.append(frame)
        if not self._ready:
            # Currently, we just return when the data could not be sent. It
            # would be better to return an asynchronous task instead. In
            # particular, this currently means that the final piece of data is
            # not sent when the line was not ready.
            return

        frames = self._buffer[:]
        self._buffer = []

        # Actually send the chunk to this client.
        self.send({
            "command": "push",
            "frames": frames,
        })


