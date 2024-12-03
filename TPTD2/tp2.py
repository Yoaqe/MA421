#!/usr/bin/python3
import pyomo.environ as pyo
import os
from pyomo.opt import SolverFactory

# Choix du formalisme (concret)
# et du modele d'optimisation (PL)
m = pyo.ConcreteModel('linear_programming')

# Declaration et typage des variables
m.a = pyo.Var(domain = pyo.NonNegativeIntegers)
m.b = pyo.Var(domain = pyo.NonNegativeIntegers)
m.c = pyo.Var(domain = pyo.NonNegativeIntegers)
m.d = pyo.Var(domain = pyo.NonNegativeIntegers)
m.e = pyo.Var(domain = pyo.NonNegativeIntegers)
m.f = pyo.Var(domain = pyo.NonNegativeIntegers)
m.g = pyo.Var(domain = pyo.NonNegativeIntegers)
m.h = pyo.Var(domain = pyo.NonNegativeIntegers)
m.i = pyo.Var(domain = pyo.NonNegativeIntegers)
m.j = pyo.Var(domain = pyo.NonNegativeIntegers)


# Objectif
m.obj = pyo.Objective(expr = 1070*m.a + 860*m.b + 730*m.c + 200*m.d +  80*m.e + 75*m.f + 100*m.g + 55*m.h + 85*m.i + 43*m.j,
sense = pyo.minimize)

# declare constraints
m.c1 = pyo.Constraint(expr = m.a + m.b +m.c <= 2)
m.c2 = pyo.Constraint(expr = 70*m.h + 141*m.i + 89*m.j + 404.7*m.a + 319.5*m.b + 276.9 * m.c >= 1140)
m.c3 = pyo.Constraint(expr = 950*m.a + 750*m.b + 2650*m.c >= 1000)
m.c4 = pyo.Constraint(expr = m.a <= 2)
m.c5 = pyo.Constraint(expr = m.b <= 2)
m.c6 = pyo.Constraint(expr = m.c <= 2)
m.c7 = pyo.Constraint(expr = m.d <= 1)
m.c8 = pyo.Constraint(expr = m.e <= 2)
m.c9 = pyo.Constraint(expr = m.f <= 1)  
m.c10 = pyo.Constraint(expr = m.g <= 1)  
m.c11 = pyo.Constraint(expr = m.h <= 3)
m.c12 = pyo.Constraint(expr = m.i <= 1)
m.c13 = pyo.Constraint(expr = m.j <= 5)

#On priorise l'utilisation de la bombe qui pése moins lourd que la chambre à aire neuve et la pompe à vélo car on cherche à le poid
m.c14 = pyo.Constraint(expr = m.g >= 1)  

#6.
m.c15 = pyo.Constraint(expr = 202*(m.h + m.i +m.j) <= 950*m.a + 750*m.b + 650*m.c)


#7.
m.c15.deactivate
m.c16 = pyo.Constraint(expr = 1070*m.a + 860*m.b + 730*m.c + 200*m.d +  80*m.e + 75*m.f + 100*m.g + 55*m.h + 85*m.i + 43*m.j <= 3000)


# Resolution
# a) Choix du solveur CBC (open-source):
# solver='cbc'
# b) on choisit ici le solveur GLPK
solver='glpk'
mysolver = SolverFactory(solver)
results = mysolver.solve(m)

# Pour le debug, on affiche la formulation complète
# print(f' {m.pprint()}')
# On peut aussi ecrire le modele dans un format de type lp :
filename = os.path.join(os.path.dirname(__file__), 'model.lp')
m.write(filename, io_options={'symbolic_solver_labels': True})

# print results
if results.solver.termination_condition == pyo.TerminationCondition.optimal:
    print('The solution is optimal.')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f'Objective value: {pyo.value(m.obj)}')
    print(f'Solution: a= {pyo.value(m.a)}, b = {pyo.value(m.b)}, c = {pyo.value(m.c)}, d = {pyo.value(m.d)}, e = {pyo.value(m.e)}, f = {pyo.value(m.f)}, g = {pyo.value(m.g)}, h = {pyo.value(m.h)}, i = {pyo.value(m.i)}, j = {pyo.value(m.j)}')
