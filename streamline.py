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
renderView1.CameraPosition = [-3.558576027625664, -7.019563782211578, 2.5669854037883386]
renderView1.CameraFocalPoint = [-0.1109995009192975, -1.0066034456147703, 1.2205295660629716]
renderView1.CameraViewUp = [0.11692028031091281, 0.1527079468999704, 0.9813306940097276]
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

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=uxdmf,
    SeedType='Point Cloud')
streamTracer1.Vectors = ['POINTS', 'u']
streamTracer1.MaximumStreamlineLength = 24.0

# init the 'Point Cloud' selected for 'SeedType'
streamTracer1.SeedType.Center = [-0.5, 0.0, 1.0]
streamTracer1.SeedType.Radius = 2.4000000000000004

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from uxdmf
uxdmfDisplay = Show(uxdmf, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
uxdmfDisplay.Representation = 'Surface'
uxdmfDisplay.ColorArrayName = [None, '']
uxdmfDisplay.SelectTCoordArray = 'None'
uxdmfDisplay.SelectNormalArray = 'None'
uxdmfDisplay.SelectTangentArray = 'None'
uxdmfDisplay.OSPRayScaleArray = 'u'
uxdmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
uxdmfDisplay.SelectOrientationVectors = 'u'
uxdmfDisplay.ScaleFactor = 2.4000000000000004
uxdmfDisplay.SelectScaleArray = 'None'
uxdmfDisplay.GlyphType = 'Arrow'
uxdmfDisplay.GlyphTableIndexArray = 'None'
uxdmfDisplay.GaussianRadius = 0.12
uxdmfDisplay.SetScaleArray = ['POINTS', 'u']
uxdmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
uxdmfDisplay.OpacityArray = ['POINTS', 'u']
uxdmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'
uxdmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
uxdmfDisplay.PolarAxes = 'PolarAxesRepresentation'
uxdmfDisplay.ScalarOpacityUnitDistance = 0.9281321349868448
uxdmfDisplay.OpacityArrayName = ['POINTS', 'u']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
uxdmfDisplay.ScaleTransferFunction.Points = [-0.0786382332444191, 0.0, 0.5, 0.0, 1.2599570751190186, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
uxdmfDisplay.OpacityTransferFunction.Points = [-0.0786382332444191, 0.0, 0.5, 0.0, 1.2599570751190186, 1.0, 0.5, 0.0]

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = ['POINTS', 'u']
streamTracer1Display.LookupTable = uLUT
streamTracer1Display.SelectTCoordArray = 'None'
streamTracer1Display.SelectNormalArray = 'None'
streamTracer1Display.SelectTangentArray = 'None'
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 2.40007438659668
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.GaussianRadius = 0.12000371932983399
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [-0.033927146572459224, 0.0, 0.5, 0.0, 0.01586547854421267, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [-0.033927146572459224, 0.0, 0.5, 0.0, 0.01586547854421267, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.WindowLocation = 'AnyLocation'
uLUTColorBar.Position = [0.7780906593406592, 0.07417102966841188]
uLUTColorBar.Title = 'u'
uLUTColorBar.ComponentTitle = 'Magnitude'
uLUTColorBar.ScalarBarLength = 0.33000000000000046

# set color bar visibility
uLUTColorBar.Visibility = 1

# show color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'u'
uPWF = GetOpacityTransferFunction('u')
uPWF.Points = [5.054423145490194e-09, 0.0, 0.5, 0.0, 1.2599940299987866, 0.15641026198863983, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(uxdmf)
# ----------------------------------------------------------------

import os.path
from os import path

renderView1.ViewTime = uxdmf.TimestepValues[-1]

sm = servermanager.Fetch(streamTracer1)
r = sm.GetPointData().GetArray('u').GetRange(0)
uLUT = GetColorTransferFunction('u')
uLUT.RescaleTransferFunction(0., r[1])

print("Rendering:", uxdmf.TimestepValues[-1])
SaveScreenshot('./images/streamline.png', renderView1, ImageResolution=[1818, 1146])

print("Exiting")
exit()
print("Exiting - shouldnt be here")

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
