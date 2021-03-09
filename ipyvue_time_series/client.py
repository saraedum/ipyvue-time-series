class Client:
    r"""
    Wraps a Comm with a blocking interface.

    When trying to send data in real-time to the frontend, the comms are
    easily saturated. Here we wrap each comm such that it does not accept new
    data until the client has sent an acknowledgment that the data was
    received.
    """
    def __init__(self, comm):
        self._comm = comm

        # Currently we treat any message from the frontend as an ACK that the
        # data has been received and more data can be sent.
        @comm.on_msg
        def _recv(msg):
            self._ready = True

        self._ready = True

    def send(self, data):
        r"""
        Send ``data`` to the frontend.

        Raises an except if the client has not sent an ACK for the previous
        data.
        """
        if not self._ready:
            raise NotImplementedError("Cannot send when client is not ready");
        self._ready = False
        self._comm.send(data)
