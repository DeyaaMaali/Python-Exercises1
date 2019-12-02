# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:43:28 2019

@author: OJO3
"""

import sympy as sym 
# =============================================================================
# x = sym.symbols('x') 
# expr = x + 1 
# print ( expr.subs(x, 2) )
# =============================================================================

# =============================================================================
# x = sym.symbols('x') 
# expr = x + x**2 + 1 
# print ( expr.subs(x, 2) )
# =============================================================================


# =============================================================================
# from sympy import * 
# =============================================================================
# =============================================================================
# x = symbols('x') 
# str_expr = "x**2 + 3*x - 1/2" 
# expr = sympify(str_expr)
# print ( expr) 
# print ( expr.subs(x, 2))
# =============================================================================


# =============================================================================
# x = sym.symbols('x') 
# sym.init_printing() 
# expr = Integral(sqrt(1/x),x) 
# sym.pprint (expr)
# =============================================================================

# =============================================================================
# x = sym.Symbol('x')
# y, i ,n, a, b = sym.symbols('y i n a b')
# 
# print(  sym.expand( (x + y) ** 3 )   )
# print( sym.simplify((x + x * y) / x))
# print(  sym.limit(sym.sin(x) / x, x, 0))
# print( sym.integrate(6 * x ** 5, x))
# print( sym.solveset(x - 1, x)) 


from sympy import symbols
from sympy.plotting import plot 
# =============================================================================
# x = symbols('x')
# plot(x **2, (x, -5, 5))
# 
# 
# =============================================================================


from sympy.plotting import plot3d 
# =============================================================================
# x, y = symbols('x y') 
# f=x**2*y**2 
# plot3d(f, (x, -5, 5), (y, -5, 5))
# 
# f=cos(x)+sin(y) 
# plot3d(f, (x, -10, 10), (y, -10, 10) )
# =============================================================================


 
from sympy import symbols, cos, sin 
from sympy.plotting import plot3d_parametric_line
# =============================================================================
# u, v = symbols('u v') 
# plot3d_parametric_line(cos(u), sin(u), u, (u, -5, 5))
# =============================================================================



import xlsxwriter
# =============================================================================
# 
# workbook = xlsxwriter.Workbook('example10.xlsx')
# worksheet = workbook.add_worksheet()
# 
# worksheet.autofilter('A1:B4')
# 
# data = ["Test",10,40,50,20]
# format = workbook.add_format()
# format.set_bold()
# format.set_font_color('red')
# format.set_font_size(20)
# 
# worksheet.write_column('A1', data ,format)
# 
# worksheet.write_comment('B1', "this is a comment")
# 
# format2 = workbook.add_format({'bold' : True, 'font_color' : 'blue'})
# 
# worksheet.write_column('B1' , data,format2)
# 
# workbook.close()
# =============================================================================

# =============================================================================
# workbook = xlsxwriter.Workbook('chart_line.xlsx')
# worksheet = workbook.add_worksheet()
# 
# data = [10, 40 , 50 ,20 ,10 , 50]
# worksheet.write_column('A1' , data)
# 
# chart = workbook.add_chart({'type': 'line'})
# 
# chart.add_series({'values': '=Sheet1!$A$1:$A$6'})
# 
# worksheet.insert_chart('C1', chart)
# 
# workbook.close()
# =============================================================================


from xlwt import Workbook, Formula

# =============================================================================
# book = Workbook()
# 
# sheet1 = book.add_sheet("Sheet 1")
# sheet1.write(0,0,10)
# sheet1.write(0,1,20)
# sheet1.write(1,0,Formula('A1/B1'))
# 
# sheet2 = book.add_sheet('Sheet 2')
# row = sheet2.row(0)
# 
# row.write(0,Formula('sum(1,2,3)'))
# row.write(1,Formula('SuM(1,2,3)'))
# row.write(2,Formula("$A$1+$B$1*SUM('ShEEt 1'!$A$1:$B$2)"))
# 
# book.save('example4.xlsx')
# =============================================================================


from xlrd import open_workbook



from sympy import *
from sympy.plotting import *
# =============================================================================
# x,y,z = symbols('x y z')
# expr= x**2+x**3+21*x**4 + 10*x+1
# print( expr.subs(x, 7) )
# print(expand( (x + y) ** 2))
# print(simplify(4*x**3+21*x**2+10*x+12))
# print(limit(1/(x**2),x,oo))
# print(integrate(sin(x)+exp(x)*cos(x)+tan(x),x))
# print(factor(x**3 + 12*x*y*z +3*y**2*z) )
# print(solveset(x-4,x))
# m1 =Matrix([[5, 12, 40], [30, 70, 2]])
# m2 =Matrix([2, 1, 0])
# print( m1*m2 )
# plot(x**3+3, (x, -10, 10))
# f=x**2*y**3
# plot3d(f, (x, -6, 6), (y, -6, 6))
# =============================================================================


import xlsxwriter
# =============================================================================
# Ex2:
# workbook = xlsxwriter.Workbook('example10.xlsx')
# worksheet = workbook.add_worksheet()
# worksheet.autofilter('A1:B1')
# data = ["this is example"]
# format = workbook.add_format()
# format.set_font_color('red')
# format.set_font_size(12)
# worksheet.write_column('A1:B1', data ,format)
# data2 = ["export my sheet"]
# format = workbook.add_format()
# format.set_font_color('black')
# format.set_font_size(12)
# worksheet.write_column('A2:B2', data2 ,format)
# data3=[1,2]
# data4=[3]
# for elem in data3:
#     format = workbook.add_format()
#     format.set_font_color('black')
#     format.set_font_size(12)
#     worksheet.write_column("A3:A4", data3 ,format)
# for elem in data4:
#     format = workbook.add_format()
#     format.set_font_color('red')
#     format.set_font_size(12)
#     worksheet.write_column("A5", data4 ,format)
# workbook.close()
# =============================================================================


from xlrd import open_workbook

# =============================================================================
# Ex3:
# wb = open_workbook('simple.xlsx')
# for s in wb.sheets():
#     print ("Sheet:", s.name)
#     for row in range(s.nrows):
#          values = []
#          for col in range(s.ncols):
#              values.append(s.cell(row,col).value)
#          print(values)
# 
# =============================================================================


















