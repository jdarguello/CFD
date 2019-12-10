import matplotlib.pyplot as plt 
from sympy import *
import sqlite3 as sql
import math
from IPython.display import display

class Solve():
    def __init__(self, Tp, Tipo, Peclet, data, Dx, Dy):
        Tp = (Tp,)
        #---Base de datos---
        nodos = None
        while nodos is None:
            con = sql.connect('App/data.db')
            nodos = con.execute("SELECT * FROM nodes ORDER BY ID ASC").fetchall()
            elementos = con.execute("SELECT * FROM elements ORDER BY p ASC").fetchall()
            con.close()
        #---Ecuación específica---
        #Creación de símbolos generales
        a_p, a_S, a_N, a_E, a_W, T_p, T_S, T_N, T_E, T_W, u, v, x, y, a_p0, b, F_S, F_N, F_E, F_W, D_S, D_N, D_E, D_W, Q_g = \
            symbols("a_p, a_S, a_N, a_E, a_W, T_p, T_S, T_N, T_E, T_W, u, v, x, y, a_{p0}, b, F_S, F_N, F_E, F_W, D_S, D_N, D_E, D_W, Q_g")
        T_p0 = Symbol("T_p ^0")
        rho, A, K = symbols("\\rho, A, K")
        A_pE, A_pW, A_pN, A_pS = symbols("A_{pE}, A_{pW}, A_{pN}, A_{pS}")
        
        #Fs y Ds
        K = data['Propiedades']['K']
        rrho = Peclet*K
        D_E = K*(Dy/Dx)
        D_W = D_E
        D_N = K*(Dx/Dy)
        D_S = D_N
        F_E = rho*u*Dy
        F_W = rho*u*Dy
        F_N = rho*v*Dx
        F_S = rho*v*Dx
        Cons = {}
        if Tipo == "Upwind":
            Cons[A_pE], Cons[A_pW], Cons[A_pN], Cons[A_pS] = 1,1,1,1
        elif Tipo == "Diferencias Centradas":
            Cons[A_pE], Cons[A_pW], Cons[A_pN], Cons[A_pS] = 1-0.5*abs(F_E/D_E), 1-0.5*abs(F_W/D_W), 1-0.5*abs(F_N/D_N), 1-0.5*abs(F_S/D_S)
        else:
            Cons[A_pE], Cons[A_pW], Cons[A_pN], Cons[A_pS] = Max(0, 1-0.5*abs(F_E/D_E)), Max(0, 1-0.5*abs(F_W/D_W)), Max(0, 1-0.5*abs(F_N/D_N)), Max(0, 1-0.5*abs(F_S/D_S))
        Cons[rho] = rrho
        Ec = Tp[0].subs(Cons)
        display(Ec)
        
        #Ts
        
        
        
        
        