import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = input()   
    my_c = Counter(s)
    
    sorted_desc_c = dict(sorted(my_c.items(), key = lambda x: (-x[1], x[0])))
    k = 0
    for letter, count in sorted_desc_c.items():
        if(k<3):
            print(letter, count)
            k += 1