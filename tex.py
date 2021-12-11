#!/usr/bin/env python
#
# Render FFT flow graphs
# Author: Mikael Henriksson
#

import subprocess
import os
import re

TEX_TEMPLATE = r'''
    \documentclass{article}
    \pagestyle{empty}
    \begin{document}
        ___TEX___BODY___
    \end{document}
'''

def tex_to_pdf(tex: str):
    tex_filename = 'tmp.tex'
    [prologue, epilogue] = re.split(r'___TEX___BODY___', TEX_TEMPLATE)
    tex = prologue+tex+epilogue
    with open(tex_filename, 'w') as f:
        f.write(tex)
    cmd = ['pdflatex', '-interaction', 'nonstopmode', 'tmp.tex']
    proc = subprocess.Popen(cmd)
    proc.communicate()
    if proc.returncode:
        print("Error generating PDF from TeX")
        exit(1)
    else:
        return os.path.splitext(tex_filename)[0]+'.pdf'

def pdf_to_svg(pdf_filename: str):
    svg_filename = os.path.splitext(pdf_filename)[0]+'.svg'
    cmd = ['inkscape', '--pdf-poppler', '--pdf-page=1',
           '--export-type=svg', '--export-text-to-path', '--export-area-drawing',
           '--export-filename', svg_filename, pdf_filename]
    proc = subprocess.Popen(cmd)
    proc.communicate()
    if proc.returncode:
        print("Error generating PDF from TeX")
        exit(1)
    else:
        return svg_filename


#tex_to_pdf(TEX_TEMPLATE)
#pdf_to_svg('tmp.pdf')
