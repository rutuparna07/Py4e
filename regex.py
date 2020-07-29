import re

hand = open('regex_sum_716291.txt')
all_lines = hand.read() #Reads in all lines as one long string
all_str_nums_as_one_line = re.findall('[0-9]+',all_lines)
hand.close()
tot = 0
for str_num in all_str_nums_as_one_line:
    tot += int(str_num)

print ('Overall sum is:',tot)