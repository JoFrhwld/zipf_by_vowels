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
by_space_sort = by_space_dict.most_common()

out_space_fi = open(out_by_space, "a")
out_space_fi.write("Word\tFreq\tRank\tLength\n")

for i in range(len(by_space_sort)):
    rank = i+1
    word = by_space_sort[i][0]
    freq = by_space_sort[i][1]
    nchar = len(word)

    out_line = word + "\t" + repr(freq) + "\t" + repr(rank) + "\t" + repr(nchar) + "\n"
    out_space_fi.write(out_line)



vowels = ["a","e","i","o","u"]

for v in vowels:
    out_by_v = "by_"+v+".txt"
    by_v_dict = Counter(raw_brown.split(v))


    by_v_sort = by_v_dict.most_common()

    out_v_fi = open(out_by_v, "a")
    out_v_fi.write("Word\tFreq\tRank\tLength\n")

    for i in range(len(by_v_sort)):
        rank = i+1
        word = by_v_sort[i][0]
        freq = by_v_sort[i][1]
        nchar = len(word)

        out_line = word + "\t" + repr(freq) + "\t" + repr(rank) + "\t" + repr(nchar) + "\n"
        out_v_fi.write(out_line)    



    
