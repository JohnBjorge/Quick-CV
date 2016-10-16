#!/usr/bin/env python

# Takes two arguments a job position, and a company and updates your cover letter accordingly.

from __future__ import print_function
from reportlab.pdfgen import canvas

import sys
import webbrowser


point = 1
inch = 72

TEXT = """PUT YOUR CV TEXT HERE (you have to mess with the spacing for text wrap purposes)

I like the %s position at %s.
"""


def make_pdf_file(output_filename, np, company, role):
    title = output_filename
    c = canvas.Canvas(output_filename, pagesize=(8.5 * inch, 11 * inch))
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)
    c.setFont("Times-Roman", 11 * point)
    for pn in range(1, np + 1):
        v = 10 * inch
        for subtline in (TEXT % (role, company)).split('\n'):
            c.drawString(1 * inch, v, subtline)
            v -= 12 * point
        c.showPage()
    c.save()

if __name__ == "__main__":
    company = sys.argv[1]
    role = sys.argv[2]
    filename = "../../example.pdf"
    make_pdf_file(filename, 1, company, role)
    print ("Wrote", filename)
    webbrowser.open_new(r'file://C:\Users\John\Documents\example.pdf')
