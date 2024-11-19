#!/usr/bin/python3
import os
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Choix du formalisme (concret)
# et du modele d'optimisation (PL)

m = pyo.ConcreteModel('linear_programming')

# Declaration et typage des variables

m.a = pyo.Var(domain = pyo.Binary)
m.b = pyo.Var(domain = pyo.Binary)
m.c = pyo.Var(domain = pyo.Binary)
m.d = pyo.Var(domain = pyo.Binary)
m.e = pyo.Var(domain = pyo.Binary)
m.f = pyo.Var(domain = pyo.Binary)
m.g = pyo.Var(domain = pyo.Binary)
m.h = pyo.Var(domain = pyo.Binary)
m.i = pyo.Var(domain = pyo.Binary)


# Objectif

m.obj = pyo.Objective(expr = m.a*14 + m.b*14+m.c*12+m.d*10+m.e*13+m.f*8+m.g*9+m.h*11+m.i*16,
sense = pyo.minimize)

# declare constraints
m.c1 = pyo.Constraint(expr = m.a+m.b+m.c <= 2)
m.c2 = pyo.Constraint(expr = m.d+m.e+m.f <= 2)
m.c3 = pyo.Constraint(expr = m.g+m.h+m.i<= 2)
m.c4 = pyo.Constraint(expr = m.a+m.d+m.g == 1)
m.c5 = pyo.Constraint(expr = m.b+m.e+m.h== 1)
m.c6 = pyo.Constraint(expr = m.c+m.f+m.i== 1)

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
    print(f'Solution: a= = {pyo.value(m.a)}, b = {pyo.value(m.b)},c = {pyo.value(m.c)}, d = {pyo.value(m.d)}, e = {pyo.value(m.e)}, f = {pyo.value(m.f)}, g = {pyo.value(m.g)}, h = {pyo.value(m.h)}, i = {pyo.value(m.i)}')