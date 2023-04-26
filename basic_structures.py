#-*- coding:utf-8 -*-
# AUTHOR:   sam1360
# FILE:     basic_structures.py
# ROLE:     TODO (some explanation)
# CREATED:  2023-04-06 20:00:10
# MODIFIED: 2023-04-13 19:42:47
#
# Copyright Henry Stone 2023
#
#BSD license

import sys

# print(sys.argv[1])
# print(sys.argv[2])

opt = sys.argv[1]
person = sys.argv[2]

if opt == '-h':
     i = 0
     while i < 22:
        i = i + 1
        print("Hello, " + person + "! (" + str(i) + ")")
elif opt == '-g':
    i = 0
    while i < 22:
        i = i + 1
        print("goodbye, " + person + "! (" + str(i) + ")")


