#!/usr/bin/python3.4
#-*- coding: utf-8 -*-

#input_data = [1, 3.5, 0.53453,2,3,4,5,6,7,8,9]
str1 = 'RSRSRSLSRSRSRSRSLSRSRSRSRSLSRSRSRSRSLSRSRSRS'
def parse_data(data, buckets = 7):
    min_val = -5000
    max_val = 5000
    step = (max_val-min_val)/buckets
    parsed_list = list()
    for value in data:
        for i in range(buckets):
            if value > min_val + 0.5*i*step and value < min_val + (i+0.5)*step:
                parsed_list.append(i)
                break
    parsed_list[:] = [x-buckets/2 for x in parsed_list]
    return parsed_list

#output = parse_data(input_data)
#print(output)
#patterns_ordered = list()

def buckets_to_chars(buckets):
    out = list()
    for value in buckets:
        if value == 0:
            out.append('S')
        elif value >= 0:
            out.append('R')
        else:
            out.append('L')
    return out

def reduce_data(data):
   result = ''
   for c in data:
       if c != result[-1:]:
           result += c
   return result

def guess_seq_len(seq):
    if not seq:
        return 0
    numbers = list()
    max_len = len(seq) 
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
            numbers.append(x)
    max_val = max(numbers)
    index = max_val
    while max_val / 2 in numbers:
        max_val /= 2
        index = max_val
    return index

def get_patterns(data):
    size = len(data)/4
    if size > 5 :
        size = 5
    output = dict()
    for i in range(len(data) - size):
        output[data[i:i+size]] = 0
    return output

class Segment(object):
    def __init__(self, name):
        self.name = name
        self.offset = 120
        self.timestamps = list()
        self.a = 1
        self.function = lambda x: -a*x^2+120 
    def compute_error_fn(self):
        if len(timestamps) > 1:
           self.error_val = timestamps[-1] - timestamps[-2] 
        else: 
            pass

def count_signs(data):
    numbers = list()
    num = 0
    zeroed = True
    for it,char in enumerate(data):
        if zeroed:
            num = 1
            zeroed = False
        elif char == data[it-1] and it != len(data)-1:
            num+=1
        else:
            numbers.append(num)
            num = 1
            zeroed = True



    return numbers


