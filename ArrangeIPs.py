from __future__ import print_function
import itertools
import re
import argparse

#Argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", type=str, required=True)
args = parser.parse_args()
file_input = args.input

with open(file_input,'r') as f:
    content = f.readlines()
ip_list = {}
final_list = []

#calculates the range
def ranges(i):
    for a, b in itertools.groupby(enumerate(i), lambda xy: xy[1] - xy[0]):
        b = list(b)
        yield b[0][1], b[-1][1]

for i in content:
    #Breaking down octects
    extractions = re.match("(\d{1,3}\.\d{1,3}\.\d{1,3})\.(\d{1,3})",i)
    if extractions:
        network, host = extractions.groups()
        host = int(host)

    if network not in ip_list:
        ip_list[network] = [host]
    elif network in ip_list:
        ip_list[network].append(host)
        ip_list[network].sort()

for k, v in ip_list.items():
    range_list = sorted(list(ranges(v)))
    for i in range_list:
        r = []
        for a in i:
            r.append(str(a))
        if r[0] == r[1]:
            final_list.append(str(k)+"."+r[0])
        else:
            final_list.append(str(k)+"."+r[0]+"-"+str(k)+"."+r[1])

#Removes the duplicates and prints the final list
new_list = []
for i in final_list:
    if i not in new_list:
        new_list.append(i)
print("Arranged IPs: ", *new_list, sep='\n')
    