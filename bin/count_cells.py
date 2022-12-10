#!/usr/bin/env pvpython
#
# Script to calculate total # of cells
#

from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

# create a new OpenFOAMReader
pfoam = OpenFOAMReader(FileName=r'pv.foam')
pfoam.CaseType = 'Decomposed Case'
pfoam.Decomposepolyhedra = 0

UpdatePipeline()
print("Cells: ",pfoam.GetDataInformation().GetNumberOfCells())





