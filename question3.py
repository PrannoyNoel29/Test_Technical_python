import csv
import re
import pandas as pd
import matplotlib.pyplot as plt
with open('log.txt') as f_input:

    df = pd.DataFrame(columns=['No. of Peers', 'Max Pool Size', 'Processing Time'])
    peers = list()
    pool_size = list()
    time = list()
    for line in f_input:
        line = line.strip()
        if 'Running peer simulation with:' in line:
            pass
        elif line[:line.find(':')] == '- number_of_peers':
            val1 = line[line.find(':'):]
            val1 = val1.strip(':')
            peers.append(val1)

        elif line[:line.find(':')] == '- max_peer_pool_size':
            val2 = line[line.find(':'):]
            val2 = val2.strip(':')
            pool_size.append(val2)

        elif line[:line.find(':')] == 'Backend processing time':
            val3 = line[line.find(':'):]
            val3 = val3.strip(':')
            time.append(val3)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # ax.plot3D(, , , 'gray')

    df['No. of Peers'] = peers
    df['Max Pool Size'] = pool_size
    df['Processing Time'] = time

    df.to_csv(r'output.csv', index = False)
