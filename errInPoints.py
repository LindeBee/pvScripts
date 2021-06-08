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
renderView1.ViewSize = [810, 550]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.125, 0.5, 0.7525]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-1.7765343543886039, 5.048498189992232, 3.443498640868411]
renderView1.CameraFocalPoint = [-0.6192201452150498, 0.3526996232857304, 0.6908845162162577]
renderView1.CameraViewUp = [0.1463914003631166, -0.473158286933658, 0.8687294132270025]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.4402712418152352
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1
renderView1.Background = [0.0, 0.0, 0.0]

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [810, 550]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.CenterOfRotation = [0.125, 0.5, 0.7525]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [-1.7765343543886039, 5.048498189992232, 3.443498640868411]
renderView2.CameraFocalPoint = [-0.6192201452150498, 0.3526996232857304, 0.6908845162162577]
renderView2.CameraViewUp = [0.1463914003631166, -0.473158286933658, 0.8687294132270025]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 1.4402712418152352
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1
renderView2.Background = [0.0, 0.0, 0.0]

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.AssignView(2, renderView2)
layout1.SetSize(1621, 550)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------



# create a new 'CSV Reader'
a112isocsv = CSVReader(registrationName='112iso.csv', FileName=['./pvScripts/112iso.csv'])

# create a new 'XDMF Reader'
uxdmf = XDMFReader(registrationName='u.xdmf', FileNames=['./results/u.xdmf'])
uxdmf.PointArrayStatus = ['u']

# create a new 'Temporal Statistics'
temporalStatistics1 = TemporalStatistics(registrationName='TemporalStatistics1', Input=uxdmf)
temporalStatistics1.ComputeMinimum = 0
temporalStatistics1.ComputeMaximum = 0
temporalStatistics1.ComputeStandardDeviation = 0

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=temporalStatistics1)
calculator1.CoordinateResults = 1
calculator1.Function = '(coordsX/2-0.25)*iHat+(coordsY/2)*jHat+(coordsZ/2)*kHat'

writer = CreateWriter("./res.csv")
writer.FieldAssociation = "Point Data"
writer.UpdatePipeline()

# create a new 'CSV Reader'
rescsv = CSVReader(registrationName='res.csv', FileName=['./res.csv'])

# create a new 'Table To Points'
tableToPoints2 = TableToPoints(registrationName='TableToPoints2', Input=rescsv)
tableToPoints2.XColumn = 'Points:0'
tableToPoints2.YColumn = 'Points:1'
tableToPoints2.ZColumn = 'Points:2'

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(registrationName='TableToPoints1', Input=a112isocsv)
tableToPoints1.XColumn = 'x/H'
tableToPoints1.YColumn = 'y/H'
tableToPoints1.ZColumn = 'z/H'

# create a new 'Point Dataset Interpolator'
pointDatasetInterpolator1 = PointDatasetInterpolator(registrationName='PointDatasetInterpolator1', Input=tableToPoints2,
    Source=tableToPoints1)
pointDatasetInterpolator1.Kernel = 'LinearKernel'
pointDatasetInterpolator1.Locator = 'Static Point Locator'

# init the 'LinearKernel' selected for 'Kernel'
pointDatasetInterpolator1.Kernel.KernelFootprint = 'N Closest'
pointDatasetInterpolator1.Kernel.NumberOfPoints = 4

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[tableToPoints1, pointDatasetInterpolator1])

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=appendAttributes1)
calculator2.ResultArrayName = '<U/uH>'
calculator2.Function = 'sqrt(<u/uH>^2+<v/uH>^2+<w/uH>^2)'

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=calculator2)
calculator3.ResultArrayName = 'u_average:Magnitude'
calculator3.Function = 'sqrt(u_average:0^2+u_average:1^2+u_average:2^2)'

# create a new 'Calculator'
distanceError = Calculator(registrationName='DistanceError', Input=calculator3)
distanceError.ResultArrayName = 'distance'
distanceError.Function = 'sqrt((max(abs(<u/uH>-u_average:0)-Uu,0))^2+(max(abs(<v/uH>-u_average:1)-Uv,0))^2+(max(abs(<w/uH>-u_average:2)-Uw,0))^2)'

# create a new 'Calculator'
magError = Calculator(registrationName='MagError', Input=distanceError)
magError.ResultArrayName = 'errorMag'
magError.Function = '(<U/uH>-u_average:Magnitude)'

# create a new 'Compute Quartiles'
computeQuartiles1 = ComputeQuartiles(registrationName='ComputeQuartiles1', Input=magError)

# create a new 'Descriptive Statistics'
descriptiveStatistics1 = DescriptiveStatistics(registrationName='DescriptiveStatistics1', Input=magError,
    ModelInput=None)
descriptiveStatistics1.VariablesofInterest = ['<U/uH>', 'distance', 'errorMag', 'u_average:Magnitude']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from magError
magErrorDisplay = Show(magError, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'errorMag'
errorMagLUT = GetColorTransferFunction('errorMag')
errorMagLUT.AutomaticRescaleRangeMode = 'Never'
errorMagLUT.RGBPoints = [-1.0, 0.23137254902, 0.298039215686, 0.752941176471, 0.0, 0.865, 0.865, 0.865, 1.0, 0.705882352941, 0.0156862745098, 0.149019607843]
errorMagLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
magErrorDisplay.Representation = 'Points'
magErrorDisplay.ColorArrayName = ['POINTS', 'errorMag']
magErrorDisplay.LookupTable = errorMagLUT
magErrorDisplay.PointSize = 4.0
magErrorDisplay.SelectTCoordArray = 'None'
magErrorDisplay.SelectNormalArray = 'None'
magErrorDisplay.SelectTangentArray = 'None'
magErrorDisplay.OSPRayScaleArray = '<U/uH>'
magErrorDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
magErrorDisplay.SelectOrientationVectors = '<U/uH>'
magErrorDisplay.ScaleFactor = 0.225
magErrorDisplay.SelectScaleArray = '<U/uH>'
magErrorDisplay.GlyphType = 'Arrow'
magErrorDisplay.GlyphTableIndexArray = '<U/uH>'
magErrorDisplay.GaussianRadius = 0.01125
magErrorDisplay.SetScaleArray = ['POINTS', '<U/uH>']
magErrorDisplay.ScaleTransferFunction = 'PiecewiseFunction'
magErrorDisplay.OpacityArray = ['POINTS', '<U/uH>']
magErrorDisplay.OpacityTransferFunction = 'PiecewiseFunction'
magErrorDisplay.DataAxesGrid = 'GridAxesRepresentation'
magErrorDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
magErrorDisplay.ScaleTransferFunction.Points = [0.020904544960366873, 0.0, 0.5, 0.0, 1.2458912472603698, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
magErrorDisplay.OpacityTransferFunction.Points = [0.020904544960366873, 0.0, 0.5, 0.0, 1.2458912472603698, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for errorMagLUT in view renderView1
errorMagLUTColorBar = GetScalarBar(errorMagLUT, renderView1)
errorMagLUTColorBar.WindowLocation = 'AnyLocation'
errorMagLUTColorBar.Position = [0.8, 0.12]
errorMagLUTColorBar.Title = 'error magnitude'
errorMagLUTColorBar.ComponentTitle = ''
errorMagLUTColorBar.ScalarBarLength = 0.3300000000000004

# set color bar visibility
errorMagLUTColorBar.Visibility = 1

# show color legend
magErrorDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from distanceError
distanceErrorDisplay = Show(distanceError, renderView2, 'GeometryRepresentation')

# get color transfer function/color map for 'distance'
distanceLUT = GetColorTransferFunction('distance')
distanceLUT.AutomaticRescaleRangeMode = 'Never'
distanceLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
distanceErrorDisplay.Representation = 'Points'
distanceErrorDisplay.ColorArrayName = ['POINTS', 'distance']
distanceErrorDisplay.LookupTable = distanceLUT
distanceErrorDisplay.PointSize = 4.0
distanceErrorDisplay.SelectTCoordArray = 'None'
distanceErrorDisplay.SelectNormalArray = 'None'
distanceErrorDisplay.SelectTangentArray = 'None'
distanceErrorDisplay.OSPRayScaleArray = 'distance'
distanceErrorDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
distanceErrorDisplay.SelectOrientationVectors = '<U/uH>'
distanceErrorDisplay.ScaleFactor = 0.225
distanceErrorDisplay.SelectScaleArray = 'distance'
distanceErrorDisplay.GlyphType = 'Arrow'
distanceErrorDisplay.GlyphTableIndexArray = 'distance'
distanceErrorDisplay.GaussianRadius = 0.01125
distanceErrorDisplay.SetScaleArray = ['POINTS', 'distance']
distanceErrorDisplay.ScaleTransferFunction = 'PiecewiseFunction'
distanceErrorDisplay.OpacityArray = ['POINTS', 'distance']
distanceErrorDisplay.OpacityTransferFunction = 'PiecewiseFunction'
distanceErrorDisplay.DataAxesGrid = 'GridAxesRepresentation'
distanceErrorDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
distanceErrorDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.8078163308033927, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
distanceErrorDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.8078163308033927, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for distanceLUT in view renderView2
distanceLUTColorBar = GetScalarBar(distanceLUT, renderView2)
distanceLUTColorBar.WindowLocation = 'AnyLocation'
distanceLUTColorBar.Position = [0.8, 0.12]
distanceLUTColorBar.Title = 'error distance'
distanceLUTColorBar.ComponentTitle = ''
distanceLUTColorBar.ScalarBarLength = 0.3299999999999996

# set color bar visibility
distanceLUTColorBar.Visibility = 1

# show color legend
distanceErrorDisplay.SetScalarBarVisibility(renderView2, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'errorMag'
errorMagPWF = GetOpacityTransferFunction('errorMag')
errorMagPWF.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
errorMagPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'distance'
distancePWF = GetOpacityTransferFunction('distance')
distancePWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(distanceError)
# ----------------------------------------------------------------

import os.path
from os import path

print("Writing")
# Get the layout/tab for the active view.
aLayout = GetLayout()
SaveScreenshot("./images/errorinpoints.png", layout=aLayout)
print("Exiting")
exit()
print("Exiting - shouldnt be here")

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
