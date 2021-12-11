#!/usr/bin/env python
#
# Render FFT flow graphs
# Author: Mikael Henriksson
#

from math import atan,sqrt,sin,cos
from tex import tex_to_pdf,pdf_to_svg
import xml.etree.ElementTree as ET
import re

# Write SVG header
def header_write(f):
    f.write(svg_header)

def footer_write(f):
    f.write('\n</svg>\n')

def create_node(f, x: int, y):
    x *= 40 
    y *= 20
    f.write(f'  <circle cx="{x}" cy="{y}" r="2" fill="black" />\n')

def create_arc(f, node_start: tuple[int,int], node_end: tuple[int,int], w: int):
    p_width = 40
    p_height = 20
    (x1, y1) = (node_start[0]*p_width, node_start[1]*p_height)
    (x2, y2) = (node_end[0]*p_width, node_end[1]*p_height)

    # Adjust length for arrow heads
    arc_len = sqrt( (y2-y1)**2 + (x2-x1)**2) - 5
    angle = atan( (y2-y1)/(x2-x1) )
    (dh, dw) = (arc_len*sin(angle), arc_len*cos(angle))
    (y2, x2) = (y1+dh, x1+dw)

    f.write(f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#000" stroke-width="1" marker-end="url(#arrowhead)" />\n')

def tex_draw(f, tex_body: str, x: float, y: float):
    pdf_filename = tex_to_pdf(tex_body)
    svg_filename = pdf_to_svg(pdf_filename)


    root = ET.parse(svg_filename).getroot()
    for child in root:
        if re.match('(^defs)|(^surface)', str(child.attrib.get('id'))):
            print(child.tag, child.attrib)




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
