from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram
import matplotlib.pyplot as plt
import seaborn as sns
import sys

stdoutOrigin=sys.stdout
sys.stdout = open("log.txt", "w")                                         # Saving the output logs into a text file. This output will be used for the next question

class PeerQ2(Peer):
        
    def send_data_to_backend(self):
        """
            Question 2:
            This method should return an _array_ of the peer's
            connection durations.
        """
        duration_ = []
        for k, v in self.peer_pool.items():                                 # Appending the value durations of peer and his additional peers into a empty array(list here)
            duration_.append(v)
        return duration_                                                    # Returns all the durations

class SimulationQ2(Simulation):        
        
    def generate_network(self):
        self.network =  [PeerQ2() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 2:
            This method should do all necessary processing to return
            the connection durations histogram bins counts.
            Don't call `plot_histogram` in this method, we just want
            to compute the histogram bins counts!
        """

        # contains list of lists of all connection durations for each peer in the network
        durations_ = [i for j in self.backend_database for i in j]          # Self.backend_database is a list of lists. Taking all these values and placing them into a list
        data, bins, counts = compute_histogram_bins(durations_, BINS)       # Computing histogram bins using histogram.py by the duration data produced
        # sns.distplot(data, hist=False)                                    # Plotting the distribution of data
        # plt.show()                                                        # Show the plot
        return (data, bins, counts)                                         # Returns a histogram_bin_counts tuple which can be used in plot_histogram function


if __name__ == "__main__":

    s = SimulationQ2(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
