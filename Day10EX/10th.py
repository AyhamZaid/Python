# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:31:44 2019

@author: Ayham
"""

import sympy as sym
from sympy.plotting import plot
from sympy.plotting import plot3d, plot3d_parametric_line, plot3d_parametric_surface
import xlsxwriter, xlwt, xlrd
print("---------EX1------")
sym.init_printing()
x = sym.symbols('x')
expr = x**2 + x**3 + 21*x**4 + 10*x + 1
print('a -> for x = 7')
print(expr, '=', expr.subs(x, 7))

y= sym.symbols('y')
print('b ->', sym.expand(x + y)**2)

print('c ->', sym.simplify(4*x**3 + 21*x**2 + 10*x + 12)) 

print('d ->', sym.limit(1/(x**2), x, sym.oo))
n,i= sym.symbols('n i' )
print('e ->', sym.summation(2*i + i - 1, (i, 5, n)))

print('f ->', sym.integrate(sym.sin(x) + sym.exp(x)*sym.cos(x) + sym.tan(x)))

z = sym.symbols('z')
print('g ->', sym.factor(x**3 + 12*x*y*z + 3*y**2*z)) 

print('h ->', sym.solveset(x-4, x))

matrix1 = sym.Matrix([[5, 12, 40], [30, 70, 2]])
matrix2 = sym.Matrix([2, 1, 0])
print('i ->')
sym.pprint(matrix1*matrix2)
print()

print('j ->')
plot(x**3 + 3, (x, -10, 10))
print()

print('k ->')
plot3d(x**2*y**3, (x, -6, 6), (y, -6, 6))
#==============================================================================
print("----------EX2-----------")
workbook = xlsxwriter.Workbook('sample1.xlsx')
worksheet = workbook.add_worksheet()

str1 = 'This is Example'
str2 = 'My first export examlpe'

format1 = workbook.add_format({
		'bold': True,
		'font_color': 'red',
		'font_size': 15
		})

format2 = workbook.add_format({
		'font_size': 10
		})

worksheet.write('A1', str1, format1)
worksheet.write('A2', str2, format2)
worksheet.write('A3', 1, format2)
worksheet.write('A4', 2, format2)
worksheet.write('A5', 3, format1)

workbook.close()
#==============================================================================
# =============================================================================
print("--------------EX3---------------")
from xlrd import open_workbook

wb = open_workbook('sample2.xlsx')

for s in wb.sheets():
    print ('Sheet:',s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print (','.join(values))
