#!/usr/bin/python3

import pyomo.environ as pyo
import os
from pyomo.opt import SolverFactory

from random import *


def generate_bp_instance(n,s):
    seed(s)
    l=[0]*n
    for i in range ( 0 , n ) :
        l[i] = randint(n,2*n)
        size=3*n
    return(l,size)

cpl = generate_bp_instance(5, 4)

n = len(cpl[0])       # nombre d'objets
b = 5       # nombre de boites
C = cpl[1]   # capacité d'une boîte
a = cpl[0]  # tailles des objets


# Choix du formalisme (concret)
# et du modele d'optimisation (PL)
m = pyo.ConcreteModel('linear_programming')

m.i = range(n)
m.j = range(b)

m.x = pyo.Var(m.i, m.j, domain = pyo.Binary)
m.y = pyo.Var(m.j, domain = pyo.Binary)

# Objectif : minimiser les couts
m.obj = pyo.Objective (expr = sum(m.y[j] for j in m.j), sense = pyo.minimize)


# Contrainte : chaque objet doit être placé dans une boîte
m.place_objet = pyo.ConstraintList()
for i in m.i:
    m.place_objet.add(sum(m.x[i, j] for j in m.j) == 1)

# Contrainte : la capacité des boîtes ne doit y = {pyo.value(m.y) pas être dépassée
m.capacite = pyo.ConstraintList()
for j in m.j:
    m.capacite.add(sum(a[i] * m.x[i, j] for i in m.i) <= C * m.y[j])


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
    for i in m.i :
        for j in m.j: 
            print(f'Solution: x({i},{j})= {pyo.value(m.x[i,j] )}')

