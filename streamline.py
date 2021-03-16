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
renderView1.ViewSize = [1038, 1146]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0, 0.0, 6.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-2.1033534243788226, 0.7699484635215007, 58.07906457633338]
renderView1.CameraFocalPoint = [-2.588180975391351e-16, -1.9723723984878918e-15, 5.999999999999979]
renderView1.CameraViewUp = [0.9984946417947729, 0.037774625349561816, 0.03976842952429157]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 19.872832369942195
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [1820, 1146]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.CenterOfRotation = [0.0, 0.0, 6.0]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [-4.050978022032497, -7.153926966984052, 3.851165127259245]
renderView2.CameraFocalPoint = [-0.6138937616395742, -1.4365029371846683, 1.537740503379831]
renderView2.CameraViewUp = [0.17234925284202615, 0.27867937474504884, 0.9447928562052658]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 18.0
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1038, 1146)

# create new layout object 'Layout #2'
layout2 = CreateLayout(name='Layout #2')
layout2.AssignView(0, renderView2)
layout2.SetSize(1820, 1146)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView2)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XDMF Reader'
uxdmf = XDMFReader(registrationName='u.xdmf', FileNames=['./results/u.xdmf'])
uxdmf.PointArrayStatus = ['u']

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=uxdmf)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.0, 0.0, 6.0]
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.0, 0.0, 6.0]

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=uxdmf,
    SeedType='Point Cloud')
streamTracer1.Vectors = ['POINTS', 'u']
streamTracer1.MaximumStreamlineLength = 24.0

# init the 'Point Cloud' selected for 'SeedType'
streamTracer1.SeedType.NumberOfPoints = 400
streamTracer1.SeedType.Radius = 3.0

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from uxdmf
uxdmfDisplay = Show(uxdmf, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
uxdmfDisplay.Representation = 'Surface'
uxdmfDisplay.ColorArrayName = [None, '']
uxdmfDisplay.SelectTCoordArray = 'None'
uxdmfDisplay.SelectNormalArray = 'None'
uxdmfDisplay.SelectTangentArray = 'None'
uxdmfDisplay.EdgeColor = [0.7935606927595941, 0.8056763561455711, 0.7833981841763943]
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
uxdmfDisplay.ScalarOpacityUnitDistance = 0.8150460051846975
uxdmfDisplay.OpacityArrayName = ['POINTS', 'u']
#uxdmfDisplay.SelectInputVectors = ['POINTS', 'u']
#uxdmfDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
uxdmfDisplay.ScaleTransferFunction.Points = [-0.14477217197418213, 0.0, 0.5, 0.0, 1.2599972486495972, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
uxdmfDisplay.OpacityTransferFunction.Points = [-0.14477217197418213, 0.0, 0.5, 0.0, 1.2599972486495972, 1.0, 0.5, 0.0]

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView2, 'GeometryRepresentation')

# get color transfer function/color map for 'u'
uLUT = GetColorTransferFunction('u')
uLUT.RGBPoints = [5.054423145490194e-09, 0.231373, 0.298039, 0.752941, 0.6299970175266045, 0.865003, 0.865003, 0.865003, 1.2599940299987866, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

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
streamTracer1Display.ScaleFactor = 2.3915340423583986
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.GaussianRadius = 0.11957670211791993
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'
#streamTracer1Display.SelectInputVectors = ['POINTS', 'Normals']
#streamTracer1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [-1.914056412475803, 0.0, 0.5, 0.0, 1.4226255094723481, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [-1.914056412475803, 0.0, 0.5, 0.0, 1.4226255094723481, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView2
uLUTColorBar = GetScalarBar(uLUT, renderView2)
uLUTColorBar.WindowLocation = 'AnyLocation'
uLUTColorBar.Position = [0.7780906593406592, 0.07417102966841188]
uLUTColorBar.Title = 'u'
uLUTColorBar.ComponentTitle = 'Magnitude'
uLUTColorBar.ScalarBarLength = 0.33000000000000046

# set color bar visibility
uLUTColorBar.Visibility = 1

# show color legend
streamTracer1Display.SetScalarBarVisibility(renderView2, True)

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
uLUT.RescaleTransferFunction(r[0], r[1])

SaveScreenshot('./images/streamline.png', renderView2, ImageResolution=[1038, 1146])

print("Exiting")
exit()
print("Exiting - shouldnt be here")

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
