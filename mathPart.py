import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym

xls = pd.ExcelFile('avgDEV.xlsx')
df = xls.parse()
print(df)
fig, ax = plt.subplots()
sc_plot = ax.scatter(df['ilosc'], df['Beksinski'])
sc_plot.set_label('Beksinski')
ax.legend()
sc_plot = ax.scatter(df['ilosc'], df['Hockney'])
sc_plot.set_label('Hockney')
ax.legend()
sc_plot = ax.scatter(df['ilosc'], df['vanGogh'])
sc_plot.set_label('Van Gogh')
ax.legend()
sc_plot = ax.scatter(df['ilosc'], df['Modigliani'])
sc_plot.set_label('Modigliani')
ax.legend()
sc_plot = ax.scatter(df['ilosc'], df['Monet'])
sc_plot.set_label('Monet')
ax.legend()
ax.set_title("Edge detector")
ax.set_xlabel("Image number")
ax.set_ylabel("Number of edges")

ax.grid(True)


x = np.array(df['ilosc'], dtype=float)
y1 = np.array(df['Beksinski'], dtype=float)
y2 = np.array(df['Hockney'], dtype=float)
y3 = np.array(df['vanGogh'], dtype=float)
y4 = np.array(df['Modigliani'], dtype=float)
y5 = np.array(df['Monet'], dtype=float)

def func(x, a, b, c, d):
    return a*x**3 + b*x**2 +c*x + d

popt, pcov = curve_fit(func, x, y1)
print ("a = %s , b = %s, c = %s, d = %s" % (popt[0], popt[1], popt[2], popt[3]))

xs = sym.Symbol('\lambda')
tex = sym.latex(func(xs,*popt)).replace('$', '')
plt.plot(x, func(x, *popt), label="Fitted Curve")

popt, pcov = curve_fit(func, x, y2)
print ("a = %s , b = %s, c = %s, d = %s" % (popt[0], popt[1], popt[2], popt[3]))

xs = sym.Symbol('\lambda')
tex = sym.latex(func(xs,*popt)).replace('$', '')
plt.plot(x, func(x, *popt), label="Fitted Curve")

popt, pcov = curve_fit(func, x, y3)
print ("a = %s , b = %s, c = %s, d = %s" % (popt[0], popt[1], popt[2], popt[3]))

xs = sym.Symbol('\lambda')
tex = sym.latex(func(xs,*popt)).replace('$', '')
plt.plot(x, func(x, *popt), label="Fitted Curve")

popt, pcov = curve_fit(func, x, y4)
print ("a = %s , b = %s, c = %s, d = %s" % (popt[0], popt[1], popt[2], popt[3]))

xs = sym.Symbol('\lambda')
tex = sym.latex(func(xs,*popt)).replace('$', '')
plt.plot(x, func(x, *popt), label="Fitted Curve")

popt, pcov = curve_fit(func, x, y5)
print ("a = %s , b = %s, c = %s, d = %s" % (popt[0], popt[1], popt[2], popt[3]))

xs = sym.Symbol('\lambda')
tex = sym.latex(func(xs,*popt)).replace('$', '')
plt.plot(x, func(x, *popt), label="Fitted Curve")
plt.show()

avgMonet = df['Monet'].mean()
avgModigliani = df['Modigliani'].mean()
avgVanGogh = df['vanGogh'].mean()
avgBeksinski = df['Beksinski'].mean()
avgHokcney = df['Hockney'].mean()
print(avgMonet, avgModigliani, avgVanGogh, avgBeksinski, avgHokcney)



