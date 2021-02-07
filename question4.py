"""
    addition
"""
import random
import seaborn as sns
import matplotlib.pyplot as plt
from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram
import json

class PeerQ4(Peer):

    def send_data_to_backend(self):
        """
            Question 4: implement this method
            This method returns a json object which contains ALL the connection durations
            of a peer.
            JSON is used because it can store additional details of peer like p2p data, content watched and many more.
            "our backend server database, which is merely a list." - If this statement is taken too considerate we can
            random sample the data here and send it in form of a list. But I'm assuming all the data is processed at
            the backend.
        """
        json_object = json.dumps(self.peer_pool)
        return json_object

class SimulationQ4(Simulation):

    def generate_network(self):
        self.network = [PeerQ4() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 4: implement this method
            This method randomly samples half of the input data. This might not be the EXACT distribution but it preserves
            the shape and distribution of the data leading to a GOOD representation.
            Later it returns the histogram_bin_counts which can used for plot_histogram.
        """
        durations_ = random.sample(self.backend_database, int(self.number_of_peers/2))      # Sampling half of the data. When there is a millions of peers we can sample it and still gives a good distribution of the data
        k = [i for j in durations_ for i in (json.loads(j).values())]
        data, bins, counts = compute_histogram_bins(k, BINS)
        # sns.distplot(data, hist=False)
        # plt.show()
        # # plot_histogram((data, bins, counts))
        return (data, bins, counts)




if __name__ == "__main__":

    s = SimulationQ4(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
