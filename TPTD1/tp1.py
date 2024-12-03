#!/usr/bin/python3
import os
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

# Choix du formalisme (concret)
# et du modele d'optimisation (PL)
m = pyo.ConcreteModel('linear_programming')

# Declaration et typage des variables
m.w = pyo.Var(domain = pyo.NonNegativeReals)
m.x = pyo.Var(domain = pyo.NonNegativeReals)
m.y = pyo.Var(domain = pyo.NonNegativeReals)
m.z = pyo.Var(domain = pyo.NonNegativeReals)


# Objectif
m.obj = pyo.Objective(expr = 0.59*m.x + 0.17*m.y + 1.53*m.z + 0.17*m.w,
sense = pyo.minimize)

# declare constraints
m.c1 = pyo.Constraint(expr = 407*m.x+79*m.y+241*m.z+50*m.w >= 2618)
m.c2 = pyo.Constraint(expr = 72*m.x+15*m.y+0*m.z+13*m.w >= 155)
m.c3 = pyo.Constraint(expr = 10*m.x+2*m.y+15*m.z+0*m.w >= 63)
m.c4 = pyo.Constraint(expr = 2*m.x+1*m.y+21*m.z+0*m.w >= 18)


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
    print(f'Solution: x = {pyo.value(m.x)}, y = {pyo.value(m.y)}, z = {pyo.value(m.z)}, w = {pyo.value(m.w)}')
