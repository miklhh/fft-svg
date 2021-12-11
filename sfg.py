#!/usr/bin/env python
#
# Render FFT flow graphs
# Author: Mikael Henriksson
#

from math import isnan, nan
import svg

N = 4
filename = "fft_4_sfg.svg"

f = open(filename, "w")

svg.header_write(f)

x1 = [ [  0, nan,   0, nan],
       [nan,   0, nan,   0],
       [  0, nan,   2, nan],
       [nan,   0, nan,   2] ]

x2 = [ [   0,   0, nan, nan ],
       [   0,   2, nan, nan ],
       [ nan, nan,   0,   1 ],
       [ nan, nan,   0,   3 ] ]

# Create first layer
for n in range(N):
    svg.create_node(f, x=0, y=n)

# Create second layer
for cur_y in range(len(x1)):
    n = x1[cur_y]
    svg.create_node(f, 1, cur_y)
    for prev_y in range(len(n)):
        w = n[prev_y]
        if not isnan(w):
            svg.create_arc(f, [0, prev_y], [1, cur_y], w)

# Create third layer
for cur_y in range(len(x2)):
    n = x2[cur_y]
    svg.create_node(f, 2, cur_y)
    for prev_y in range(len(n)):
        w = n[prev_y]
        if not isnan(w):
            svg.create_arc(f, [1, prev_y], [2, cur_y], w)

# Close file
svg.footer_write(f)
f.close()

