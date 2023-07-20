#!/usr/bin/python3
"""
 0. Log parsing
"""

import sys


def print_stat(dict_scode, file_size):
    """prints filesize and status code count"""
    print("File size: {}".format(file_size))
    for code, count in sorted(dict_scode.items()):
        if count != 0:
            print("{}: {}".format(code, count))


acc_file_size = 0
code = 0
counter = 0
dict_stat_code = {
                  "200": 0,
                  "301": 0,
                  "400": 0,
                  "401": 0,
                  "403": 0,
                  "404": 0,
                  "405": 0,
                  "500": 0}

try:
    for line in sys.stdin:
        log_arg_list = line.split()
        log_reversed = log_arg_list[::-1]
        if len(log_reversed) > 2:
            counter += 1
            if counter <= 10:
                acc_file_size += int(log_reversed[0])  # file size
                code = log_reversed[1]  # status code
                if (code in dict_stat_code.keys()):
                    dict_stat_code[code] += 1
                    if (counter == 10):
                        print_msg(dict_stat_code, acc_file_size)
                        counter = 0
finally:
    print_msg(dict_stat_code, acc_file_size)
