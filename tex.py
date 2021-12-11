#!/usr/bin/env python
#
# Render FFT flow graphs
# Author: Mikael Henriksson
#

import subprocess

TEX_TEMPLATE = r'''
    \documentclass{article}
    \pagestyle{empty}
    \begin{document}
        \[ \sum_{i=1}^5 i \cdot i \]
    \end{document}
'''

def tex_to_pdf(tex: str):
    with open('tmp.tex', 'w') as f:
        f.write(tex)
    cmd = ['pdflatex', '-interaction', 'nonstopmode', 'tmp.tex']
    proc = subprocess.Popen(cmd)
    proc.communicate()
    if proc.returncode:
        print("Error generating PDF from TeX")
        exit(1)

def pdf_to_svg(filename: str):
    cmd = ['inkscape', '--pdf-poppler', '--pdf-page=1',
           '--export-type=svg', '--export-text-to-path', '--export-area-drawing',
           '--export-filename', filename+'.svg', filename]
    proc = subprocess.Popen(cmd)
    proc.communicate()


tex_to_pdf(TEX_TEMPLATE)
pdf_to_svg('tmp.pdf')
