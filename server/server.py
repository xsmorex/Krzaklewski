from math import floor
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

superclient = None
clients = []


class TrackServer(WebSocket):
    def __init__(self, *args, **kwargs):
        self.clients = []
        super(TrackServer, self).__init__(*args, **kwargs)

    def handleMessage(self):
        message = self.data.split(":")

        if message[0] == 'steer':
            suppliedPower = floor(float(message[1]) * 2.55)

            try:
                superclient.sendMessage(suppliedPower)
            except Exception, e:
                print "No superclient :-(."

        elif message[0] == 'status':
            for client in self.clients:
                if client != self:
                    client.sendMessage(message[1])

    def handleConnected(self):
        clients.append(self)

    def handleClose(self):
        clients.remove(self)

server = SimpleWebSocketServer('', 8000, TrackServer)
server.serveforever()