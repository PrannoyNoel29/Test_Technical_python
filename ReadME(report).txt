Technical Test - Python - 6/2/2021 - Prannoy Noel BHUMANA

Problem - 1: Connections:

This question deals with peers and their connection durations. The files used to solve it and their description are below:

1. Histogram.py - First part of computing bins count is done without any external libraries import.  Solved using brute-force(Not optimized) algorithm. This returns a tuple which contains the durations data, bins and their counts. This tuple is then fed into plot_histogram. Here Matplotlib is used for plotting. The x-axis values are changed into the required text of intervals. Later it is plotted with the labels.

2. Peer.py - This file contains pre-defined functions about peer and adding peers to his pool. The connection durations are calculated here using the data defined. The data is generated from 'random' library. This mainly follows normal distribution. So, when we plot these values mostly we will see a bell curve. Not completely, but the shape is similar.

3. Simulation.py - This file contains pre-defined functions on simulations like generating network of peers and sending the data to backend along with processing.

4. Question2.py - Filled the functions and array is returned. This data is processed to find backend  processing time. These values are saved into 'log.txt' file.

5. Question3.py - This is file completely created by me to plot the generated data. Some of the observations are:
	
	5.1) When the distributions are plotted for 10 peers and pool size of 2, We can observe a clear bell curve. But when the peers and the pools are increased, it becomes more of rectangular bell curve. The distribution values are also getting changed on the x-axis. However, we can see the maximum density value remains same for all of the plots. This is an 'Exact-Distribution' of data.

	5.2) Another observation is that whenever the peers and pool size are increased by value of 10, the backend processing time is also increasing along with it in a linear manner. This shows that backend processing time is directly proportional to total peers (peers * max_pool)

	5.3) If there are millions of peers and max pool size is also set to million, then the processing time will be huge which is a unfavourable case. So, the max_pool size should be set to a small number(somewhere in 100's) to achieve the best results of all the cases

6. Question4.py - This problem is completely assumed and solved by those constraints. I want to get the data of peers other than the connection duration. Some of the additional details like streaming content, errors, live or VOD stream. However with an array we need to make list of lists to get all these details. But if we use a JSON data format, we can get them in a single file in a more clean format. Thus giving us a clear picture of peer's activity and company's performance. 
Since there are millions of peers, I decided to sample the data randomly. I'll select the data of half of the peers, this doesn't change the distribution of data hugely. But we can analyse it in a lesser time. When the distributions are plotted, we can see they didn't change much from the previous question. However, the processing time didn't go down, but it almost remained the same. 


Problem - 2: Data Mining

All the explanations and comments are given in Jupyter notebook. Please refer to it.


------------------------------------------ THANK YOU ------------------------------------------------
