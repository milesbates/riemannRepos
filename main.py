import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
#fortnite
x, y = sym.symbols('x y')
probs = [2*(sym.sec(x)**2)*sym.tan(x),
            4*x**5-5*x**4,
            sym.exp(x)*sym.sin(x)
            ]
g, m, c = sym.symbols('g m c')
probs2 = [g*m/c*(1-sym.exp(-c/m*x)), g*m/c]
def findRiemann(problem, interval, num):
    real = sym.N(sym.integrate(problem,(x,interval[0],interval[1])))
    dist = (interval[1]-interval[0])/num
    xs = np.linspace(interval[0],interval[1],num)
    ys = [(problem.subs(x,j))*dist for j in xs]
    guess = sym.N(sum(ys))
    print('Riemann Sum')
    print(f'guess: {guess}')
    print(f'real: {real}')
    print(f'percent error: {abs((real-guess)/real)*100}')
def plotRiemann(problem,interval,num,type=0):
    dist = (interval[1]-interval[0])/num
    xpl = np.linspace(interval[0],interval[1],300)
    ypl = [problem.subs(x,j) for j in xpl]
    xs = np.linspace(interval[0],interval[1],num)
    xs = xs[:(len(xs)-1)]
    ys = [(problem.subs(x,j+dist*type)) for j in xs]
    real = sym.integrate(problem,(x,interval[0],interval[1]))
    guess = sum(ys)*dist
    fig = plt.figure(dpi=300)
    plt.plot(xpl,ypl)
    plt.title(f'Riemann Sum\nReal:{round(sym.N(real),3)} Guess:{round(guess,3)}')
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    ax = plt.gca()
    for i in range(num-1):
        rect = patches.Rectangle([xs[i],0],dist,ys[i],linewidth=1,linestyle='dashed', edgecolor='black', facecolor='r')
        ax.add_patch(rect)
    plt.show()

def trapRiemann(problem, interval, num):
    dist = (interval[1]-interval[0])/num
    xpl = np.linspace(interval[0],interval[1],300)
    ypl = [problem.subs(x,j) for j in xpl]
    xs = np.linspace(interval[0],interval[1],num)
    xs = xs[:(len(xs)-1)]
    ys = []
    #for i in range(1,len(xs)):
    #    ys.append(dist*(problem.subs(x,xs[i-1])+(problem.subs(x,xs[i])-problem.subs(x,xs[i-1]))/2))
    ys.append(dist/2*problem.subs(x,xs[0]))
    for i in range(1,len(xs)-1):
        ys.append(dist*problem.subs(x,xs[i]))
    ys.append(dist/2*problem.subs(x,xs[-1]))
    real = sym.integrate(problem,(x,interval[0],interval[1]))
    guess = sum(ys)
    print('Trapezoidal Reiemann Sum')
    print(f'guess: {guess}')
    print(f'real: {real}')
    print(f'percent error: {abs((real-guess)/real)*100}%')

def thirdRiemann(problem, interval, num):
    dist = (interval[1]-interval[0])/num
    xpl = np.linspace(interval[0],interval[1],300)
    ypl = [problem.subs(x,j) for j in xpl]
    xs = np.linspace(interval[0],interval[1],num)
    xs = xs[:(len(xs)-1)]
    ys = []
    for i in range(1,len(xs)):
        ys.append((xs[i]-xs[i-1])/6*(problem.subs(x,xs[i-1])+4*problem.subs(x,(xs[i]+xs[i-1])/2)+problem.subs(x,xs[i-1])))
    real = sym.integrate(problem,(x,interval[0],interval[1]))
    guess = sum(ys)
    print('Simpsons 1/3 Reiemann Sum')
    print(f'guess: {guess}')
    print(f'real: {real}')
    print(f'percent error: {abs((real-guess)/real)*100}%')

def eighthRiemann(problem, interval, num):
    dist = (interval[1]-interval[0])/num
    xpl = np.linspace(interval[0],interval[1],300)
    ypl = [problem.subs(x,j) for j in xpl]
    xs = np.linspace(interval[0],interval[1],num)
    xs = xs[:(len(xs)-1)]
    ys = []
    for i in range(1,len(xs)):
        ys.append(((xs[i]-xs[i-1])/8)*(problem.subs(x,xs[i-1])+3*problem.subs(x,(xs[i]+2*xs[i-1])/3)+3*problem.subs(x,(2*xs[i]+xs[i-1])/3)+problem.subs(x,xs[i])))
        #ys.append((xs[i]-xs[i-1])/8*(problem.subs(x,xs[i-1])+3*problem.subs(x,(xs[i]+2*xs[i-1])/3))+3*problem.subs(x,(2*xs[i]+xs[i-1])/3)+problem.subs(x,xs[i]))
    real = sym.integrate(problem,(x,interval[0],interval[1]))
    guess = sum(ys)
    print('Simpsons 3/8 Reiemann Sum')
    print(f'guess: {guess}')
    print(f'real: {real}')
    print(f'percent error: {abs((real-guess)/real)*100}%')

findRiemann(probs[2],[-5,5],1000)
findRiemann(probs2[0],[0,5],1000)
#trapRiemann(probs[1],[-5,5],1000)
#thirdRiemann(probs[1],[-5,5],1000)
#eighthRiemann(probs[1], [-5,5],1000)

# for p in probs:
#     plotRiemann(p,[-5,5],50,.5)

