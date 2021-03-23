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
renderView1.CameraPosition = [-5.007944914377122, -10.049024226301702, 4.619743236878824]
renderView1.CameraFocalPoint = [0., 0., 1.2]
renderView1.CameraViewUp = [0., 0., 1.]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 18.0
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1
renderView1.Background = [0., 0., 0.]

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
n_steps = len(uxdmf.TimestepValues)
Show(uxdmf)
(xmin,xmax,ymin,ymax,zmin,zmax) = GetActiveSource().GetDataInformation().GetBounds()
Hide(uxdmf)

renderView1.CameraPosition = [-xmax/12., -xmax/6., xmax/12.]
renderView1.CameraFocalPoint = [0., 0., xmax/300]
renderView1.CameraViewUp = [0., 0., 1.]

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=uxdmf)

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=uxdmf,
    SeedType='Point Cloud')
streamTracer1.Vectors = ['POINTS', 'u']
streamTracer1.MaximumStreamlineLength = 24.0

# init the 'Point Cloud' selected for 'SeedType'
streamTracer1.SeedType.Center = [0.0, 0.0, 0.0]
streamTracer1.SeedType.Radius = xmax/50
streamTracer1.SeedType.NumberOfPoints = 400

# create a new 'Clip'
clip3 = Clip(registrationName='Clip3', Input=extractSurface1)
clip3.ClipType = 'Box'
clip3.HyperTreeGridClipper = 'Plane'
clip3.Scalars = ['POINTS', '']

# init the 'Box' selected for 'ClipType'
clip3.ClipType.Position = [-12.0, -12.0, 0.0]
clip3.ClipType.Length = [24.0, 24.0, 5.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip3.HyperTreeGridClipper.Origin = [0.0, 0.0, 6.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from clip3
clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip3Display.Representation = 'Surface'
clip3Display.AmbientColor = [0.3137254901960784, 0.3137254901960784, 0.3137254901960784]
clip3Display.ColorArrayName = [None, '']
clip3Display.DiffuseColor = [0.3137254901960784, 0.3137254901960784, 0.3137254901960784]
clip3Display.SelectTCoordArray = 'None'
clip3Display.SelectNormalArray = 'None'
clip3Display.SelectTangentArray = 'None'
clip3Display.OSPRayScaleArray = 'u'
clip3Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip3Display.SelectOrientationVectors = 'u'
clip3Display.ScaleFactor = 0.2
clip3Display.SelectScaleArray = 'None'
clip3Display.GlyphType = 'Arrow'
clip3Display.GlyphTableIndexArray = 'None'
clip3Display.GaussianRadius = 0.01
clip3Display.SetScaleArray = ['POINTS', 'u']
clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
clip3Display.OpacityArray = ['POINTS', 'u']
clip3Display.OpacityTransferFunction = 'PiecewiseFunction'
clip3Display.DataAxesGrid = 'GridAxesRepresentation'
clip3Display.PolarAxes = 'PolarAxesRepresentation'
clip3Display.ScalarOpacityUnitDistance = 0.306796723923514
clip3Display.OpacityArrayName = ['POINTS', 'u']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip3Display.ScaleTransferFunction.Points = [-0.13641615211963654, 0.0, 0.5, 0.0, 0.8052195310592651, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip3Display.OpacityTransferFunction.Points = [-0.13641615211963654, 0.0, 0.5, 0.0, 0.8052195310592651, 1.0, 0.5, 0.0]

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'u'
uLUT = GetColorTransferFunction('u')
uLUT.RGBPoints = [7.936710681885738e-09, 0.231373, 0.298039, 0.752941, 0.6300376693354819, 0.865003, 0.865003, 0.865003, 1.260075330734253, 0.705882, 0.0156863, 0.14902]
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
streamTracer1Display.ScaleFactor = 2.398476982116699
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.GaussianRadius = 0.11992384910583496
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [-2.219871916053603, 0.0, 0.5, 0.0, 1.6925958278228421, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [-2.219871916053603, 0.0, 0.5, 0.0, 1.6925958278228421, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.Title = 'u'
uLUTColorBar.ComponentTitle = 'Magnitude'

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
uPWF.Points = [7.936710681885738e-09, 0.0, 0.5, 0.0, 1.260075330734253, 1.0, 0.5, 0.0]
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
