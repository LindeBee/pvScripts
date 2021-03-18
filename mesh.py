# state file generated using paraview version 5.8.1-1634-g6bacce2f26

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1818, 1146]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.0, 0.0, 6.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-19.517870614478063, -58.065601014166255, 38.97107031029266]
renderView1.CameraFocalPoint = [1.060377920498384, -0.9447236006935089, 5.052360173308529]
renderView1.CameraViewUp = [0.1507343979572938, 0.4640301161285433, 0.872900448274706]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 18.0
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1818, 1146)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XDMF Reader'
uxdmf = XDMFReader(registrationName='u.xdmf', FileNames=['./results/u.xdmf'])
uxdmf.PointArrayStatus = ['u']

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=uxdmf)

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=extractSurface1)
clip1.ClipType = 'Box'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', '']

# init the 'Box' selected for 'ClipType'
clip1.ClipType.Position = [-12.0, -12.0, -1.0]
clip1.ClipType.Length = [25.0, 25.0, 13.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.0, 0.0, 6.0]

# create a new 'Extract Edges'
extractEdges1 = ExtractEdges(registrationName='ExtractEdges1', Input=uxdmf)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from extractEdges1
extractEdges1Display = Show(extractEdges1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
extractEdges1Display.Representation = 'Surface'
extractEdges1Display.ColorArrayName = [None, '']
extractEdges1Display.Opacity = 0.07
extractEdges1Display.SelectTCoordArray = 'None'
extractEdges1Display.SelectNormalArray = 'None'
extractEdges1Display.SelectTangentArray = 'None'
extractEdges1Display.OSPRayScaleArray = 'u'
extractEdges1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractEdges1Display.SelectOrientationVectors = 'u'
extractEdges1Display.ScaleFactor = 2.4000000000000004
extractEdges1Display.SelectScaleArray = 'None'
extractEdges1Display.GlyphType = 'Arrow'
extractEdges1Display.GlyphTableIndexArray = 'None'
extractEdges1Display.GaussianRadius = 0.12
extractEdges1Display.SetScaleArray = ['POINTS', 'u']
extractEdges1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractEdges1Display.OpacityArray = ['POINTS', 'u']
extractEdges1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractEdges1Display.DataAxesGrid = 'GridAxesRepresentation'
extractEdges1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractEdges1Display.ScaleTransferFunction.Points = [-0.13641615211963654, 0.0, 0.5, 0.0, 1.260075330734253, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractEdges1Display.OpacityTransferFunction.Points = [-0.13641615211963654, 0.0, 0.5, 0.0, 1.260075330734253, 1.0, 0.5, 0.0]

# show data from clip1
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface With Edges'
clip1Display.AmbientColor = [0.0, 0.0, 0.0]
clip1Display.ColorArrayName = [None, '']
clip1Display.DiffuseColor = [0.0, 0.0, 0.0]
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.EdgeColor = [0.0, 0.5690394445716029, 0.5746242465857938]
clip1Display.OSPRayScaleArray = 'u'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'u'
clip1Display.ScaleFactor = 2.4000000000000004
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 0.12
clip1Display.SetScaleArray = ['POINTS', 'u']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'u']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 3.038587528692336
clip1Display.OpacityArrayName = ['POINTS', 'u']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [-0.13641615211963654, 0.0, 0.5, 0.0, 1.259952425956726, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [-0.13641615211963654, 0.0, 0.5, 0.0, 1.259952425956726, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# restore active source
SetActiveSource(clip1)
# ----------------------------------------------------------------

import os.path
from os import path

print("Rendering: mesh")
SaveScreenshot('./images/mesh.png', renderView1, ImageResolution=[1818, 1146])

print("Exiting")
exit()
print("Exiting - shouldnt be here")

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
