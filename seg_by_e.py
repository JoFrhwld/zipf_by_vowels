from nltk import corpus as corp
import re
import string
from collections import Counter

out_by_space = "by_space.txt"
out_by_e = "by_e.txt"


raw_brown = corp.brown.raw()
raw_brown = re.sub("/.*?(\b|\s|$)", " ", raw_brown)
raw_brown = raw_brown.translate(string.maketrans("",""), string.punctuation)
raw_brown = re.sub("\s+", " ", re.sub("\s", " ", raw_brown))
raw_brown = raw_brown.lower()

by_space_dict = Counter(raw_brown.split(" "))
by_e_dict = Counter(raw_brown.split("e"))

for x in by_space_dict:
    n = by_space_dict[x]
    nchar = len(x)

    by_space_dict[x] = [n, nchar]

for x in by_e_dict:
    n =  by_e_dict[x]
    nchar = len(x)

    by_e_dict[x] = [n, nchar]

by_space_sort = by_space_dict.most_common()
by_e_sort = by_e_dict.most_common()

out_space_fi = open(out_by_space, "a")
out_space_fi.write("Word\tFreq\tRank\tLength\n")

for i in range(len(by_space_sort)):
    rank = i+1
    word = by_space_sort[i][0]
    freq = by_space_sort[i][1][0]
    nchar = by_space_sort[i][1][1]

    out_line = word + "\t" + repr(freq) + "\t" + repr(rank) + "\t" + repr(nchar) + "\n"
    out_space_fi.write(out_line)


out_e_fi = open(out_by_e, "a")
out_e_fi.write("Word\tFreq\tRank\tLength\n")

for i in range(len(by_e_sort)):
    rank = i+1
    word = by_e_sort[i][0]
    freq = by_e_sort[i][1][0]
    nchar = by_e_sort[i][1][1]

    out_line = word + "\t" + repr(freq) + "\t" + repr(rank) + "\t" + repr(nchar) + "\n"
    out_e_fi.write(out_line)    



    
