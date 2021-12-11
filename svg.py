#!/usr/bin/env python
#
# Render FFT flow graphs
# Author: Mikael Henriksson
#

from math import atan,cos,sin

# Write SVG header
def header_write(f):
    f.write(svg_header)

def footer_write(f):
    f.write('\n</svg>\n')

def create_node(f, x: int, y):
    x *= 40 
    y *= 20
    f.write(f'  <circle cx="{x}" cy="{y}" r="2" fill="black" />\n')

def create_arc(f, node_start: list[int], node_end: list[int], w: int):
    p_width = 40
    p_height = 20
    [x1, y1] = [node_start[0]*p_width, node_start[1]*p_height]
    [x2, y2] = [node_end[0]*p_width, node_end[1]*p_height]

    # Adjust length for arrow heads
    angle = atan( (y2-y1)/(x2-x1) )
    #[x2, y2] = [0.9*cos(angle)*x2, 0.9*cos(angle)*y2]
    [x2, y2] = [0.87*x2, y2]

    f.write(f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#000" stroke-width="1" marker-end="url(#arrowhead)" />\n')

svg_header = '\
<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n\
<svg version="1.1" width="210mm" height="297mm" xmlns="http://www.w3.org/2000/svg">\n\
\n\
  <defs>\n\
    <marker id="arrowhead" markerWidth="4" markerHeight="3" refX="0" refY="1.5" orient="auto">\n\
      <polygon points="0 0, 4 1.5, 0 3" />\n\
    </marker>\n\
  </defs>\n\
\n'
