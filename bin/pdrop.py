#!/usr/bin/env pvpython
#
# Script to calculate pressure drop from OpenFOam
#

from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

# create a new OpenFOAMReader
pfoam = OpenFOAMReader(FileName=r'pv.foam')
pfoam.CaseType = 'Decomposed Case'
pfoam.Decomposepolyhedra = 0

# inlet pressure is the pressure drop, since teh outlet is at zero
pfoam.MeshRegions = ['patch/inlet']
pfoam.CellArrays = ['U', 'k', 'nut', 'omega', 'p']

integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=pfoam)
ivals = paraview.servermanager.Fetch(integrateVariables1)

p   = ivals.GetCellData().GetArray('p').GetValue(0)     # integral p_i dA
A   = ivals.GetCellData().GetArray('Area').GetValue(0)  # inlet area
rho = 2645.0845     # fuel salt density kg/m^3

Pd = rho * p / A    # static pressure = rho * kinematic pressure / area

print("Pd [Pa] = ", Pd)




