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
renderView1.ViewSize = [902, 532]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.5, 0.0, 1.4999999701976776]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [1.4991918301650995, -0.012445815457466258, 8.878299560610031]
renderView1.CameraFocalPoint = [1.4991918301651004, -0.012445815457466258, 1.3395418071160599]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 5.060843066171858
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [902, 532]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.CenterOfRotation = [1.5, 0.0, 0.5]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [1.5, 0.0, 9.202045680183359]
renderView2.CameraFocalPoint = [1.5, 0.0, -0.3128647630381646]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 3.605551275463989
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [902, 532]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.CenterOfRotation = [1.5, 0.0, 1.0]
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [1.5, 0.0, 9.710049847538174]
renderView3.CameraFocalPoint = [1.5, 0.0, 0.3635780020486169]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 5.185437617384842
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [902, 532]
renderView4.InteractionMode = '2D'
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.CenterOfRotation = [1.4999999999999998, 0.0, 1.4999999701976776]
renderView4.StereoType = 'Crystal Eyes'
renderView4.CameraPosition = [1.4999999999999998, -19.094218151784567, 1.4999999701976776]
renderView4.CameraFocalPoint = [1.4999999999999998, 0.0, 1.4999999701976776]
renderView4.CameraViewUp = [0.0, 0.0, 1.0]
renderView4.CameraFocalDisk = 1.0
renderView4.CameraParallelScale = 1.9053346217085732
renderView4.BackEnd = 'OSPRay raycaster'
renderView4.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.500000)
layout1.SplitHorizontal(1, 0.500000)
layout1.AssignView(3, renderView1)
layout1.AssignView(4, renderView4)
layout1.SplitHorizontal(2, 0.500000)
layout1.AssignView(5, renderView2)
layout1.AssignView(6, renderView3)
layout1.SetSize(1805, 1065)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView3)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Text'
text2 = Text(registrationName='Text2')
text2.Text = 'y/H = 0'

# create a new 'Text'
text1 = Text(registrationName='Text1')
text1.Text = 'z/H = 0.0625'

# create a new 'XDMF Reader'
uxdmf = XDMFReader(registrationName='u.xdmf', FileNames=['./results/u.xdmf'])
uxdmf.PointArrayStatus = ['u']

# create a new 'Text'
text3 = Text(registrationName='Text3')
text3.Text = 'z/H = 0.25'

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=uxdmf)
clip1.ClipType = 'Box'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', '']
clip1.Exact = 1

# init the 'Box' selected for 'ClipType'
clip1.ClipType.Position = [-1.5, -2.0, 0.0]
clip1.ClipType.Length = [6.0, 4.0, 3.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [10.0, 0.0, 6.0]

# create a new 'Slice'
slice3 = Slice(registrationName='Slice3', Input=clip1)
slice3.SliceType = 'Plane'
slice3.HyperTreeGridSlicer = 'Plane'
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [1.5, 0.0, 0.5]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice3.HyperTreeGridSlicer.Origin = [1.5, 0.0, 1.5]

# create a new 'Slice'
slice2 = Slice(registrationName='Slice2', Input=clip1)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [1.5, 0.0, 1.5]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice2.HyperTreeGridSlicer.Origin = [1.5, 0.0, 1.5]

# create a new 'Slice'
slice4 = Slice(registrationName='Slice4', Input=clip1)
slice4.SliceType = 'Plane'
slice4.HyperTreeGridSlicer = 'Plane'
slice4.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice4.SliceType.Origin = [1.5, 0.0, 1.0]
slice4.SliceType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice4.HyperTreeGridSlicer.Origin = [1.5, 0.0, 1.5]

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=clip1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [1.5, 0.0, 0.125]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [1.5, 0.0, 1.5]

# create a new 'Text'
text4 = Text(registrationName='Text4')
text4.Text = 'z/H = 0.5'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from slice1
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'u'
uLUT = GetColorTransferFunction('u')
uLUT.RGBPoints = [0.019010998064402217, 0.231373, 0.298039, 0.752941, 2.7801894613254925, 0.865003, 0.865003, 0.865003, 5.541367924586583, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

uLUT_1 = GetColorTransferFunction('u')
uLUT_1.RGBPoints = [0.019010998064402217, 0.231373, 0.298039, 0.752941, 2.7801894613254925, 0.865003, 0.865003, 0.865003, 5.541367924586583, 0.705882, 0.0156863, 0.14902]
uLUT_1.ScalarRangeInitialized = 1.0

uLUT_2 = GetColorTransferFunction('u')
uLUT_2.RGBPoints = [0.019010998064402217, 0.231373, 0.298039, 0.752941, 2.7801894613254925, 0.865003, 0.865003, 0.865003, 5.541367924586583, 0.705882, 0.0156863, 0.14902]
uLUT_2.ScalarRangeInitialized = 1.0

uLUT_3 = GetColorTransferFunction('u')
uLUT_3.RGBPoints = [0.019010998064402217, 0.231373, 0.298039, 0.752941, 2.7801894613254925, 0.865003, 0.865003, 0.865003, 5.541367924586583, 0.705882, 0.0156863, 0.14902]
uLUT_3.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'u']
slice1Display.LookupTable = uLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'u'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'u'
slice1Display.ScaleFactor = 0.6000000000000001
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.GaussianRadius = 0.03
slice1Display.SetScaleArray = ['POINTS', 'u']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'u']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.3046239912509918, 0.0, 0.5, 0.0, 0.5841284990310669, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.3046239912509918, 0.0, 0.5, 0.0, 0.5841284990310669, 1.0, 0.5, 0.0]

# show data from text1
text1Display = Show(text1, renderView1, 'TextSourceRepresentation')

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.WindowLocation = 'UpperRightCorner'
uLUTColorBar.Title = 'u'
uLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
uLUTColorBar.Visibility = 1

# show color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from slice3
slice3Display = Show(slice3, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
slice3Display.Representation = 'Surface'
slice3Display.ColorArrayName = ['POINTS', 'u']
slice3Display.LookupTable = uLUT_1
slice3Display.SelectTCoordArray = 'None'
slice3Display.SelectNormalArray = 'None'
slice3Display.SelectTangentArray = 'None'
slice3Display.OSPRayScaleArray = 'u'
slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display.SelectOrientationVectors = 'u'
slice3Display.ScaleFactor = 0.6000000000000001
slice3Display.SelectScaleArray = 'None'
slice3Display.GlyphType = 'Arrow'
slice3Display.GlyphTableIndexArray = 'None'
slice3Display.GaussianRadius = 0.03
slice3Display.SetScaleArray = ['POINTS', 'u']
slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display.OpacityArray = ['POINTS', 'u']
slice3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice3Display.DataAxesGrid = 'GridAxesRepresentation'
slice3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice3Display.ScaleTransferFunction.Points = [0.9434093832969666, 0.0, 0.5, 0.0, 1.2103792428970337, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice3Display.OpacityTransferFunction.Points = [0.9434093832969666, 0.0, 0.5, 0.0, 1.2103792428970337, 1.0, 0.5, 0.0]

# show data from text3
text3Display = Show(text3, renderView2, 'TextSourceRepresentation')

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView2
uLUTColorBar_1 = GetScalarBar(uLUT_1, renderView2)
uLUTColorBar_1.Title = 'u'
uLUTColorBar_1.ComponentTitle = 'Magnitude'

# set color bar visibility
uLUTColorBar_1.Visibility = 1

# show color legend
slice3Display.SetScalarBarVisibility(renderView2, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from slice4
slice4Display = Show(slice4, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
slice4Display.Representation = 'Surface'
slice4Display.ColorArrayName = ['POINTS', 'u']
slice4Display.LookupTable = uLUT_2
slice4Display.SelectTCoordArray = 'None'
slice4Display.SelectNormalArray = 'None'
slice4Display.SelectTangentArray = 'None'
slice4Display.OSPRayScaleArray = 'u'
slice4Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice4Display.SelectOrientationVectors = 'u'
slice4Display.ScaleFactor = 0.6000000000000001
slice4Display.SelectScaleArray = 'None'
slice4Display.GlyphType = 'Arrow'
slice4Display.GlyphTableIndexArray = 'None'
slice4Display.GaussianRadius = 0.03
slice4Display.SetScaleArray = ['POINTS', 'u']
slice4Display.ScaleTransferFunction = 'PiecewiseFunction'
slice4Display.OpacityArray = ['POINTS', 'u']
slice4Display.OpacityTransferFunction = 'PiecewiseFunction'
slice4Display.DataAxesGrid = 'GridAxesRepresentation'
slice4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice4Display.ScaleTransferFunction.Points = [1.759818434715271, 0.0, 0.5, 0.0, 2.091660737991333, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice4Display.OpacityTransferFunction.Points = [1.759818434715271, 0.0, 0.5, 0.0, 2.091660737991333, 1.0, 0.5, 0.0]

# show data from text4
text4Display = Show(text4, renderView3, 'TextSourceRepresentation')

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView3
uLUTColorBar_2 = GetScalarBar(uLUT_2, renderView3)
uLUTColorBar_2.Title = 'u'
uLUTColorBar_2.ComponentTitle = 'Magnitude'

# set color bar visibility
uLUTColorBar_2.Visibility = 1

# show color legend
slice4Display.SetScalarBarVisibility(renderView3, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# show data from slice2
slice2Display = Show(slice2, renderView4, 'GeometryRepresentation')

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['POINTS', 'u']
slice2Display.LookupTable = uLUT_3
slice2Display.SelectTCoordArray = 'None'
slice2Display.SelectNormalArray = 'None'
slice2Display.SelectTangentArray = 'None'
slice2Display.OSPRayScaleArray = 'u'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'u'
slice2Display.ScaleFactor = 0.6000000000000001
slice2Display.SelectScaleArray = 'None'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'None'
slice2Display.GaussianRadius = 0.03
slice2Display.SetScaleArray = ['POINTS', 'u']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'u']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [0.0941123366355896, 0.0, 0.5, 0.0, 4.149954319000244, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [0.0941123366355896, 0.0, 0.5, 0.0, 4.149954319000244, 1.0, 0.5, 0.0]

# show data from text2
text2Display = Show(text2, renderView4, 'TextSourceRepresentation')

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView4
uLUTColorBar_3 = GetScalarBar(uLUT_3, renderView4)
uLUTColorBar_3.WindowLocation = 'AnyLocation'
uLUTColorBar_3.Position = [0.7606707317073171, 0.6259398496240601]
uLUTColorBar_3.Title = 'u'
uLUTColorBar_3.ComponentTitle = 'Magnitude'
uLUTColorBar_3.ScalarBarLength = 0.33000000000000007

# set color bar visibility
uLUTColorBar_3.Visibility = 1

# show color legend
slice2Display.SetScalarBarVisibility(renderView4, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'u'
uPWF = GetOpacityTransferFunction('u')
uPWF.Points = [0.019010998064402217, 0.0, 0.5, 0.0, 5.541367924586583, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(text4)
# ----------------------------------------------------------------
t = uxdmf.TimestepValues[-1]
renderView1.ViewTime = t
renderView2.ViewTime = t
renderView3.ViewTime = t
renderView4.ViewTime = t

import os.path
from os import path

SetActiveView(renderView2)
SetActiveSource(slice1)
sm = servermanager.Fetch(slice1)
r = sm.GetPointData().GetArray('u').GetRange(0)
uLUT = GetColorTransferFunction('u')
uLUT.RescaleTransferFunction(0., r[1])
SetActiveSource(slice3)
sm = servermanager.Fetch(slice3)
r = sm.GetPointData().GetArray('u').GetRange(0)
uLUT_1 = GetColorTransferFunction('u')
uLUT_1.RescaleTransferFunction(0., r[1])
SetActiveSource(slice4)
sm = servermanager.Fetch(slice4)
r = sm.GetPointData().GetArray('u').GetRange(0)
uLUT_2 = GetColorTransferFunction('u')
uLUT_2.RescaleTransferFunction(0., r[1])
SetActiveSource(slice2)
sm = servermanager.Fetch(slice2)
r = sm.GetPointData().GetArray('u').GetRange(0)
uLUT_3 = GetColorTransferFunction('u')
uLUT_3.RescaleTransferFunction(0., r[1])

print("Rendering", t)
# Get the layout/tab for the active view.
aLayout = GetLayout()
SaveScreenshot("./images/slices.png", layout=aLayout)
print("Exiting")
exit()
print("Exiting - shouldnt be here")




if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
