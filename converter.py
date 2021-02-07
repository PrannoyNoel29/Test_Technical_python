import csv
import re
fieldnames = ['- number_of_peers', '- max_peer_pool_size', 'Backend processing time']
re_fields = re.compile(r'({})\s+:\D(.*)'.format('|'.join(fieldnames)), re.I)

with open('log.txt') as f_input, open('output.csv', 'w', newline='') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames)
    csv_output.writeheader()
    start = False

    for line in f_input:
        line = line.strip()
        if len(line):
            if 'Running peer simulation with:' in line:
                if start:
                    start = False
                    # print()
                    block.append(line)
                    text_block = '\n'.join(block)
                    # print(text_block)
                    # txt = re.sub(r'\D', "", text_block)
                    # print(txt)
                    txt = re_fields.findall(text_block)
                    print(txt)
                    # for line in block.splitlines():
                    #     block = block.replace('-', '')
                    #     name,val = block.split(":")
                    # print(val)
                    # for field, value in re_fields.findall(text_block):
                    #     entry[field.upper()] = value


                    csv_output.writerow(entry)

                else:
                    start = True
                    entry = {}
                    block = [line]
            elif start:
                block.append(line)