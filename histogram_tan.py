from random import randint
import matplotlib.pyplot as plt

def compute_histogram_bins(data, bins):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted numbers that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins.
        You are not allowed to use external libraries other than those already
        imported.
    """
    
    bins_new = bins[1:]
    bins_new.append(max(data)*2)

    heights = [0] * len(bins)

    for n in data:
        for i in range(len(bins)):
            if n >= bins[i] and n < bins_new[i]:
                heights[i] += 1
    
    return (data, bins, heights)




def plot_histogram(full_data):
    """
        Question 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommend using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    data, bins, heights = full_data

    bin_labels = [str(bins[i])+"-"+str(bins[i+1]) for i in range(len(bins)-1)]
    bin_labels.append(str(bins[-1])+"+")
    
    ticks = [i for i in range(len(bins))]    

    print(ticks)
    print(heights)

    plt.bar(ticks, heights)
    plt.xticks(ticks, bin_labels)    # xticks(ticks, [labels])
    plt.show()

if __name__ == "__main__":

    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
