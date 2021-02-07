from random import sample
import datetime
import json
from peer import Peer
from histogram import *

BINS = [0, 10, 50, 100, 150, 200, 300]

class Simulation(object):

    def __init__(self, number_of_peers=1, max_peer_pool_size=5):
        self.number_of_peers = number_of_peers
        self.max_peer_pool_size = max_peer_pool_size if max_peer_pool_size < number_of_peers else number_of_peers

        self.network = []

        self.backend_database = []
        self.backend_processing_time = 0

    def generate_network(self):
        self.network =  [Peer() for _ in range(self.number_of_peers)]

    def connect_peers(self):
        for p in self.network:
            p.add_peers_to_peer_pool(sample(self.network, self.max_peer_pool_size))

    def retrieve_data_from_peers(self):
        for p in self.network:
            self.backend_database.append(p.send_data_to_backend())

    def run(self):
        self.generate_network()

        self.connect_peers()

        self.retrieve_data_from_peers()

        start = datetime.datetime.now() 
        self.process_backend_data()
        self.backend_processing_time = datetime.datetime.now() - start

    def process_backend_data(self):
        return
        
    def report_result(self):
        print("Running peer simulation with:") 
        print(" - number_of_peers: {}".format(self.number_of_peers))
        print(" - max_peer_pool_size: {}".format(self.max_peer_pool_size))
        print("Backend processing time: {}\n".format(self.backend_processing_time))

