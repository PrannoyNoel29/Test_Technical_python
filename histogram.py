from random import randint
import matplotlib.pyplot as plt

def compute_histogram_bins(data=[], bins=[]):
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
    bins_new = bins[1:]                         # Removing 0 to create a new bin list to compare
    bins_new.append(max(data)*2)                # Appending a value which is twice the maximum value to indicate the value is out of bin range

    counts = [0] * len(bins)

    for n in data:
        for i in range(len(bins)):
            if n >= bins[i] and n < bins_new[i]: # Comparing the two bins and adding the count if it's present in the interval
                counts[i] += 1

    return (data, bins, counts)                  # Retruns a tuple of 3 elements which contain random data, bins, counts - THis tuple is ideally bins_count




def plot_histogram(bins_count):
    """
        Question 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommend using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    data, bins, counts = bins_count

    bin_labels = [str(bins[i])+"-"+str(bins[i+1]) for i in range(len(bins)-1)] # Changing the names of the labels becuase the example figure displayed -
    bin_labels.append(str(bins[-1])+"+")                                       ## are in the form of intervals

    ticks = [i for i in range(len(bins))]

    plt.bar(ticks, counts)                                                      # Plotting a bar chart between bins and counts
    plt.xticks(ticks, bin_labels)                                               # xticks(ticks, [labels]) set the current tick locations and labels of the x-axis.
    for i in range(len(ticks)):
        plt.annotate(str(counts[i]), xy=(ticks[i], counts[i]), ha='center', va='bottom')    # Adding labels on the bar plot
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
