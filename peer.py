from random import random
import uuid

MIN_CONNECTION_DURATION = 0.1 # in seconds
MAX_CONNECTION_DURATION = 600 # in seconds

class Peer(object):

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.peer_pool = {}

    def add_peers_to_peer_pool(self, peers):
        for p in peers:
            if self.id == p.id:
                break
            if (p not in self.peer_pool) and (self not in p.peer_pool):
                connection_duration = MIN_CONNECTION_DURATION + random() * (MAX_CONNECTION_DURATION - MIN_CONNECTION_DURATION)
                self.peer_pool[p.id] = connection_duration 
                p.peer_pool[self.id] = connection_duration
            elif (p not in self.peer_pool) and (self in p.peer_pool):
                self.peer_pool[p.id] = p.peer_pool[self.id]
            elif (p in self.peer_pool) and (self not in p.peer_pool):
                p.peer_pool[self.id] = self.peer_pool[p.id]

    def send_data_to_backend(self):
        return 0