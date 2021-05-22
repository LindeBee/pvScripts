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
renderView1.ViewSize = [766, 538]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [1.0000000000000002, 0.0, 0.4370164772309544]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [1.02358674731548, -7.139517645467244, 1.5111334247359134]
renderView1.CameraFocalPoint = [1.02358674731548, 0.0, 1.5111334247359134]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.946657309763115
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [718, 538]
renderView2.InteractionMode = '2D'
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [1.0, 0.0, 0.4220393001668623]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [1.0, 0.13347232752204993, 10000.125]
renderView2.CameraFocalPoint = [1.0, 0.13347232752204993, 0.125]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 2.2440035064644643
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [850, 538]
renderView3.InteractionMode = '2D'
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [1.0, 0.0, 1.4999999701976776]
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [10001.0, 0.0, 1.6096320098410104]
renderView3.CameraFocalPoint = [1.0, 0.0, 1.6096320098410104]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 1.6383894804017636
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [848, 538]
renderView4.InteractionMode = '2D'
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.OrientationAxesVisibility = 0
renderView4.CenterOfRotation = [1.0595090366015283, 0.0, 1.4999999701976776]
renderView4.StereoType = 'Crystal Eyes'
renderView4.CameraPosition = [10001.5, 0.0, 1.6110096847381452]
renderView4.CameraFocalPoint = [1.5, 0.0, 1.6110096847381452]
renderView4.CameraViewUp = [0.0, 0.0, 1.0]
renderView4.CameraFocalDisk = 1.0
renderView4.CameraParallelScale = 1.6589780663644933
renderView4.BackEnd = 'OSPRay raycaster'
renderView4.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView5 = CreateView('RenderView')
renderView5.ViewSize = [194, 538]
renderView5.AxesGrid = 'GridAxes3DActor'
renderView5.OrientationAxesVisibility = 0
renderView5.CenterOfRotation = [1.0, 0.0, 1.5]
renderView5.StereoType = 'Crystal Eyes'
renderView5.CameraPosition = [1.0, 0.0, 14.763608510004255]
renderView5.CameraFocalPoint = [1.0, 0.0, 1.5]
renderView5.CameraFocalDisk = 1.0
renderView5.CameraParallelScale = 3.4670524780161247
renderView5.BackEnd = 'OSPRay raycaster'
renderView5.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.500000)
layout1.SplitHorizontal(1, 0.450771)
layout1.AssignView(3, renderView1)
layout1.SplitHorizontal(4, 0.778261)
layout1.AssignView(9, renderView2)
layout1.AssignView(10, renderView5)
layout1.SplitHorizontal(2, 0.500000)
layout1.AssignView(5, renderView3)
layout1.AssignView(6, renderView4)
layout1.SetSize(1699, 1077)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView2)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Text'
text3 = Text(registrationName='Text3')
text3.Text = 'x/H = 0.5'

# create a new 'XDMF Reader'
uxdmf = XDMFReader(registrationName='u.xdmf', FileNames=['./results/u.xdmf'])
uxdmf.PointArrayStatus = ['u']

# create a new 'Text'
text2 = Text(registrationName='Text2')
text2.Text = 'z/H = 0.0625'

# create a new 'Text'
text1 = Text(registrationName='Text1')
text1.Text = 'y/H = 0'

# create a new 'Text'
text4 = Text(registrationName='Text4')
text4.Text = 'x/H = 0.75'

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=uxdmf)
clip1.ClipType = 'Box'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', '']
clip1.Exact = 1

# init the 'Box' selected for 'ClipType'
clip1.ClipType.Position = [-1.5, -2.0, 0.0]
clip1.ClipType.Length = [5.0, 4.0, 3.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [10.0, 0.0, 6.0]

# create a new 'Temporal Statistics'
temporalStatistics2 = TemporalStatistics(registrationName='TemporalStatistics2', Input=clip1)
temporalStatistics2.ComputeMinimum = 0
temporalStatistics2.ComputeMaximum = 0
temporalStatistics2.ComputeStandardDeviation = 0

# create a new 'Slice'
slice3 = Slice(registrationName='Slice3', Input=temporalStatistics2)
slice3.SliceType = 'Plane'
slice3.HyperTreeGridSlicer = 'Plane'
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [1.0, 0.0, 0.125]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice3.HyperTreeGridSlicer.Origin = [1.0, 0.0, 1.5]

# create a new 'Slice'
slice5 = Slice(registrationName='Slice5', Input=temporalStatistics2)
slice5.SliceType = 'Plane'
slice5.HyperTreeGridSlicer = 'Plane'
slice5.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice5.SliceType.Origin = [1.5, 0.0, 1.5]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice5.HyperTreeGridSlicer.Origin = [1.0, 0.0, 1.5]

# create a new 'Slice'
slice2 = Slice(registrationName='Slice2', Input=temporalStatistics2)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [1.0, 0.0, 1.5]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice2.HyperTreeGridSlicer.Origin = [1.0, 0.0, 1.5]

# create a new 'Slice'
slice4 = Slice(registrationName='Slice4', Input=temporalStatistics2)
slice4.SliceType = 'Plane'
slice4.HyperTreeGridSlicer = 'Plane'
slice4.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice4.SliceType.Origin = [1.0, 0.0, 1.5]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice4.HyperTreeGridSlicer.Origin = [1.0, 0.0, 1.5]

## create a new 'Calculator'
#calculator1 = Calculator(registrationName='Calculator1', Input=clip1)
#calculator1.ResultArrayName = 'magU'
#calculator1.Function = 'mag(u)'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from slice2
slice2Display = Show(slice2, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'u_average'
u_averageLUT = GetColorTransferFunction('u_average')
u_averageLUT.AutomaticRescaleRangeMode = 'Never'
u_averageLUT.RGBPoints = [-0.05, 0.019607, 0.07853, 0.60784, 0.0, 0.019607, 0.07853, 0.60784, 0.1, 0.023529, 0.207843, 0.66667, 0.2, 0.141176, 0.37647, 0.73725, 0.3, 0.23137, 0.55294, 0.7882, 0.4, 0.28627, 0.64706, 0.63137, 0.5, 0.32941, 0.72549, 0.415686, 0.6, 0.3686, 0.79216, 0.26667, 0.7, 0.4196, 0.8549, 0.2588, 0.8, 0.5804, 0.898, 0.2784, 0.9, 0.8118, 0.949, 0.3059, 1.0, 0.9882, 0.9176, 0.3098, 1.1, 0.949, 0.6314, 0.2314, 1.2, 0.9294, 0.3608, 0.1647, 1.25, 0.9216, 0.1961, 0.1373]
u_averageLUT.ColorSpace = 'Step'
u_averageLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['POINTS', 'u_average']
slice2Display.LookupTable = u_averageLUT
slice2Display.SelectTCoordArray = 'None'
slice2Display.SelectNormalArray = 'None'
slice2Display.SelectTangentArray = 'None'
slice2Display.OSPRayScaleArray = 'magU_average'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'None'
slice2Display.ScaleFactor = 0.5
slice2Display.SelectScaleArray = 'None'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'None'
slice2Display.GaussianRadius = 0.025
slice2Display.SetScaleArray = ['POINTS', 'magU_average']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'magU_average']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [0.017403111010631273, 0.0, 0.5, 0.0, 1.3700774213128823, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [0.017403111010631273, 0.0, 0.5, 0.0, 1.3700774213128823, 1.0, 0.5, 0.0]

# show data from text1
text1Display = Show(text1, renderView1, 'TextSourceRepresentation')

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from slice3
slice3Display = Show(slice3, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
slice3Display.Representation = 'Surface'
slice3Display.ColorArrayName = ['POINTS', 'u_average']
slice3Display.LookupTable = u_averageLUT
slice3Display.SelectTCoordArray = 'None'
slice3Display.SelectNormalArray = 'None'
slice3Display.SelectTangentArray = 'None'
slice3Display.OSPRayScaleArray = 'magU_average'
slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display.SelectOrientationVectors = 'None'
slice3Display.ScaleFactor = 0.5
slice3Display.SelectScaleArray = 'None'
slice3Display.GlyphType = 'Arrow'
slice3Display.GlyphTableIndexArray = 'None'
slice3Display.GaussianRadius = 0.025
slice3Display.SetScaleArray = ['POINTS', 'magU_average']
slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display.OpacityArray = ['POINTS', 'magU_average']
slice3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice3Display.DataAxesGrid = 'GridAxesRepresentation'
slice3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice3Display.ScaleTransferFunction.Points = [0.031401138495663616, 0.0, 0.5, 0.0, 1.0085701502592839, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice3Display.OpacityTransferFunction.Points = [0.031401138495663616, 0.0, 0.5, 0.0, 1.0085701502592839, 1.0, 0.5, 0.0]

# show data from text2
text2Display = Show(text2, renderView2, 'TextSourceRepresentation')

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from slice4
slice4Display = Show(slice4, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
slice4Display.Representation = 'Surface'
slice4Display.ColorArrayName = ['POINTS', 'u_average']
slice4Display.LookupTable = u_averageLUT
slice4Display.SelectTCoordArray = 'None'
slice4Display.SelectNormalArray = 'None'
slice4Display.SelectTangentArray = 'None'
slice4Display.OSPRayScaleArray = 'magU_average'
slice4Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice4Display.SelectOrientationVectors = 'None'
slice4Display.ScaleFactor = 0.4
slice4Display.SelectScaleArray = 'None'
slice4Display.GlyphType = 'Arrow'
slice4Display.GlyphTableIndexArray = 'None'
slice4Display.GaussianRadius = 0.02
slice4Display.SetScaleArray = ['POINTS', 'magU_average']
slice4Display.ScaleTransferFunction = 'PiecewiseFunction'
slice4Display.OpacityArray = ['POINTS', 'magU_average']
slice4Display.OpacityTransferFunction = 'PiecewiseFunction'
slice4Display.DataAxesGrid = 'GridAxesRepresentation'
slice4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice4Display.ScaleTransferFunction.Points = [0.1035263935878075, 0.0, 0.5, 0.0, 1.1645821825741625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice4Display.OpacityTransferFunction.Points = [0.1035263935878075, 0.0, 0.5, 0.0, 1.1645821825741625, 1.0, 0.5, 0.0]

# show data from text3
text3Display = Show(text3, renderView3, 'TextSourceRepresentation')

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# show data from slice5
slice5Display = Show(slice5, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
slice5Display.Representation = 'Surface'
slice5Display.ColorArrayName = ['POINTS', 'u_average']
slice5Display.LookupTable = u_averageLUT
slice5Display.SelectTCoordArray = 'None'
slice5Display.SelectNormalArray = 'None'
slice5Display.SelectTangentArray = 'None'
slice5Display.OSPRayScaleArray = 'magU_average'
slice5Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice5Display.SelectOrientationVectors = 'None'
slice5Display.ScaleFactor = 0.4
slice5Display.SelectScaleArray = 'None'
slice5Display.GlyphType = 'Arrow'
slice5Display.GlyphTableIndexArray = 'None'
slice5Display.GaussianRadius = 0.02
slice5Display.SetScaleArray = ['POINTS', 'magU_average']
slice5Display.ScaleTransferFunction = 'PiecewiseFunction'
slice5Display.OpacityArray = ['POINTS', 'magU_average']
slice5Display.OpacityTransferFunction = 'PiecewiseFunction'
slice5Display.DataAxesGrid = 'GridAxesRepresentation'
slice5Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice5Display.ScaleTransferFunction.Points = [0.09844907414822635, 0.0, 0.5, 0.0, 1.1504232991215768, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice5Display.OpacityTransferFunction.Points = [0.09844907414822635, 0.0, 0.5, 0.0, 1.1504232991215768, 1.0, 0.5, 0.0]

# show data from text4
text4Display = Show(text4, renderView4, 'TextSourceRepresentation')

# ----------------------------------------------------------------
# setup the visualization in view 'renderView5'
# ----------------------------------------------------------------

# show data from slice2
slice2Display_1 = Show(slice2, renderView5, 'GeometryRepresentation')

# get color transfer function/color map for 'magU_average'
magU_averageLUT = GetColorTransferFunction('magU_average')
magU_averageLUT.AutomaticRescaleRangeMode = 'Never'
magU_averageLUT.RGBPoints = [-0.05, 0.019607, 0.07853, 0.60784, 0.0, 0.019607, 0.07853, 0.60784, 0.09999999999999999, 0.023529, 0.207843, 0.66667, 0.19999999999999996, 0.141176, 0.37647, 0.73725, 0.29999999999999993, 0.23137, 0.55294, 0.7882, 0.39999999999999997, 0.28627, 0.64706, 0.63137, 0.5, 0.32941, 0.72549, 0.415686, 0.6, 0.3686, 0.79216, 0.26667, 0.7, 0.4196, 0.8549, 0.2588, 0.8, 0.5804, 0.898, 0.2784, 0.8999999999999999, 0.8118, 0.949, 0.3059, 0.9999999999999998, 0.9882, 0.9176, 0.3098, 1.1, 0.949, 0.6314, 0.2314, 1.2, 0.9294, 0.3608, 0.1647, 1.25, 0.9216, 0.1961, 0.1373]
magU_averageLUT.ColorSpace = 'Step'
magU_averageLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice2Display_1.Representation = 'Surface'
slice2Display_1.ColorArrayName = ['POINTS', 'magU_average']
slice2Display_1.LookupTable = magU_averageLUT
slice2Display_1.SelectTCoordArray = 'None'
slice2Display_1.SelectNormalArray = 'None'
slice2Display_1.SelectTangentArray = 'None'
slice2Display_1.OSPRayScaleArray = 'magU_average'
slice2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display_1.SelectOrientationVectors = 'None'
slice2Display_1.ScaleFactor = 0.5
slice2Display_1.SelectScaleArray = 'None'
slice2Display_1.GlyphType = 'Arrow'
slice2Display_1.GlyphTableIndexArray = 'None'
slice2Display_1.GaussianRadius = 0.025
slice2Display_1.SetScaleArray = ['POINTS', 'magU_average']
slice2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display_1.OpacityArray = ['POINTS', 'magU_average']
slice2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display_1.DataAxesGrid = 'GridAxesRepresentation'
slice2Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display_1.ScaleTransferFunction.Points = [0.017403111010631273, 0.0, 0.5, 0.0, 1.3700774213128823, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display_1.OpacityTransferFunction.Points = [0.017403111010631273, 0.0, 0.5, 0.0, 1.3700774213128823, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for magU_averageLUT in view renderView5
magU_averageLUTColorBar = GetScalarBar(magU_averageLUT, renderView5)
magU_averageLUTColorBar.WindowLocation = 'AnyLocation'
magU_averageLUTColorBar.Position = [0.03625110766504214, 0.04272276670046187]
magU_averageLUTColorBar.Title = 'magU_average'
magU_averageLUTColorBar.ComponentTitle = ''
magU_averageLUTColorBar.ScalarBarLength = 0.9072220344711065

# set color bar visibility
magU_averageLUTColorBar.Visibility = 1

# show color legend
slice2Display_1.SetScalarBarVisibility(renderView5, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'magU_average'
magU_averagePWF = GetOpacityTransferFunction('magU_average')
magU_averagePWF.Points = [-0.05, 0.0, 0.5, 0.0, 1.25, 1.0, 0.5, 0.0]
magU_averagePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'u_average'
u_averagePWF = GetOpacityTransferFunction('u_average')
u_averagePWF.Points = [-0.05, 0.0, 0.5, 0.0, 1.25, 1.0, 0.5, 0.0]
u_averagePWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(text4)
# ----------------------------------------------------------------

print("Writing")
# Get the layout/tab for the active view.
aLayout = GetLayout()
SaveScreenshot("./images/contourSlices.png", layout=aLayout)
print("Exiting")
exit()
print("Exiting - shouldnt be here")


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
