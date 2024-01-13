import random
import re

flag_re = 'grodno{.*?}'

shuffled_flag = "}r3,_oeL'_lNS1NIfNF____0pnGjl3eo1APbN_tilB_H10{IdlN33_L'4l_uoggT_D"
for seed in range(1000):
    n = len(shuffled_flag)
    orig_index = list(range(n))
    random.seed(seed)
    random.shuffle(orig_index)
    unshuffled_flag = [None]*n
    for i, orig_i in enumerate(orig_index):
        unshuffled_flag[orig_i] = shuffled_flag[i]
    unshuffled_flag = ''.join(unshuffled_flag)
    flag = re.findall(flag_re, unshuffled_flag)
    if "grodno{" in unshuffled_flag:
        print(flag[0])
        exit()