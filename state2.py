# state file generated using paraview version 5.8.1-1634-g6bacce2f26

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [646, 534]
lineChartView1.LegendPosition = [20, 453]
lineChartView1.LeftAxisTitle = 'z'
lineChartView1.LeftAxisUseCustomRange = 1
lineChartView1.LeftAxisRangeMaximum = 12.0
lineChartView1.BottomAxisTitle = 'Mean velocity'
lineChartView1.BottomAxisUseCustomRange = 1
lineChartView1.BottomAxisRangeMaximum = 6.0
lineChartView1.RightAxisUseCustomRange = 1
lineChartView1.RightAxisRangeMaximum = 6.66
lineChartView1.TopAxisUseCustomRange = 0

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
lineChartView2.ViewSize = [646, 534]
lineChartView2.LegendPosition = [429, 453]
lineChartView2.LeftAxisTitle = 'z'
lineChartView2.BottomAxisTitle = 'Turbulence Kinetic Energy'
lineChartView2.LeftAxisUseCustomRange = 0
lineChartView2.RightAxisUseCustomRange = 0
lineChartView2.TopAxisUseCustomRange = 0

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1312, 534]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0., 0., 0.]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0., -50., 0.]
renderView1.CameraFocalPoint = [0., 0., 0.]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 21.095023109728988
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.SplitHorizontal(2, 0.500000)
layout1.AssignView(5, lineChartView1)
layout1.AssignView(6, lineChartView2)
layout1.SetSize(1312, 1069)

# ----------------------------------------------------------------
# restore active view
SetActiveView(lineChartView1)
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

renderView1.CameraPosition = [0., -30., 2]
renderView1.CameraFocalPoint = [(xmax+xmin)/2, (ymax+ymin)/2, 2]

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=uxdmf)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [(xmax+xmin)/2, (ymax+ymin)/2, (zmax+zmin)/2]
slice1.SliceType.Normal = [0., 1., 0.]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [(xmax+xmin)/2, (ymax+ymin)/2, (zmax+zmin)/2]
slice1.HyperTreeGridSlicer.Normal = [0., 1., 0.]

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=slice1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'u']
glyph1.ScaleArray = ['POINTS', 'u']
glyph1.ScaleFactor = 0.5
glyph1.GlyphTransform = 'Transform2'

# create a new 'Extract Time Steps'
extractTimeSteps1 = ExtractTimeSteps(registrationName='ExtractTimeSteps1', Input=uxdmf)
extractTimeSteps1.SelectionMode = 'Select Time Range'
extractTimeSteps1.TimeStepIndices = [0]
# get last 25% of timesteps
a = int(3*(n_steps-1)/4)
b = n_steps-1
extractTimeSteps1.TimeStepRange = [a, b]

# create a new 'Temporal Statistics'
temporalStatistics1 = TemporalStatistics(registrationName='TemporalStatistics1', Input=extractTimeSteps1)
temporalStatistics1.ComputeMinimum = 0
temporalStatistics1.ComputeMaximum = 0

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=temporalStatistics1)
calculator1.ResultArrayName = 'TKE'
calculator1.Function = '0.5*(u_stddev_X^2+u_stddev_Y^2+u_stddev_Z^2)'

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=calculator1,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine1.Source.Point1 = [(xmax+xmin)/2, (ymax+ymin)/2, zmin]
plotOverLine1.Source.Point2 = [(xmax+xmin)/2, (ymax+ymin)/2, zmax]

# create a new 'Plot Over Line'
plotOverLine2 = PlotOverLine(registrationName='PlotOverLine2', Input=calculator1,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine2.Source.Point1 = [(xmax+xmin)/2, ymin+3*(ymax-ymin)/4, zmin]
plotOverLine2.Source.Point2 = [(xmax+xmin)/2, ymin+3*(ymin-ymin)/4, zmax]

# create a new 'Plot Over Line'
plotOverLine3 = PlotOverLine(registrationName='PlotOverLine3', Input=temporalStatistics1,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine3.Source.Point1 = [(xmax+xmin)/2, (ymax+ymin)/2, zmin]
plotOverLine3.Source.Point2 = [(xmax+xmin)/2, (ymax+ymin)/2, zmax]

# create a new 'Plot Over Line'
plotOverLine4 = PlotOverLine(registrationName='PlotOverLine4', Input=temporalStatistics1,
    Source='Line')

# init the 'Line' selected for 'Source'
plotOverLine4.Source.Point1 = [(xmax+xmin)/2, ymin+3*(ymax-ymin)/4, zmin]
plotOverLine4.Source.Point2 = [(xmax+xmin)/2, ymin+3*(ymin-ymin)/4, zmax]

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView1'
# ----------------------------------------------------------------

# show data from plotOverLine3
plotOverLine3Display = Show(plotOverLine3, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine3Display.CompositeDataSetIndex = [0]
plotOverLine3Display.UseIndexForXAxis = 0
plotOverLine3Display.XArrayName = 'u_average_Magnitude'
plotOverLine3Display.SeriesVisibility = ['Points_Z']
plotOverLine3Display.SeriesLabel = ['arc_length', 'arc_length', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'y/ymax = 0.5', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine3Display.SeriesColor = ['arc_length', '0', '0', '0', 'u_average_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_stddev_X', '1', '0.5000076295109483', '0', 'u_stddev_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_stddev_Z', '0', '0', '0', 'u_stddev_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'vtkValidPointMask', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Z', '0', '0.3333333333333333', '1', 'Points_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867']
plotOverLine3Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
plotOverLine3Display.SeriesLabelPrefix = ''
plotOverLine3Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
plotOverLine3Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
plotOverLine3Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
plotOverLine3Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# show data from plotOverLine4
plotOverLine4Display = Show(plotOverLine4, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine4Display.CompositeDataSetIndex = [0]
plotOverLine4Display.UseIndexForXAxis = 0
plotOverLine4Display.XArrayName = 'u_average_Magnitude'
plotOverLine4Display.SeriesVisibility = ['Points_Z']
plotOverLine4Display.SeriesLabel = ['arc_length', 'arc_length', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'y/ymax = 0.75', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine4Display.SeriesColor = ['arc_length', '0', '0', '0', 'u_average_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Magnitude', '1', '0', '0', 'u_stddev_X', '1', '0.5000076295109483', '0', 'u_stddev_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_stddev_Z', '0', '0', '0', 'u_stddev_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'vtkValidPointMask', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Z', '1', '0', '0.4980392156862745', 'Points_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867']
plotOverLine4Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
plotOverLine4Display.SeriesLabelPrefix = ''
plotOverLine4Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
plotOverLine4Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
plotOverLine4Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
plotOverLine4Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView2'
# ----------------------------------------------------------------

# show data from plotOverLine1
plotOverLine1Display = Show(plotOverLine1, lineChartView2, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.CompositeDataSetIndex = [0]
plotOverLine1Display.UseIndexForXAxis = 0
plotOverLine1Display.XArrayName = 'TKE'
plotOverLine1Display.SeriesVisibility = ['Points_Z']
plotOverLine1Display.SeriesLabel = ['arc_length', 'arc_length', 'TKE', 'TKE', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'y/ymax = 0.5', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'TKE', '0.3333333333333333', '0', '0.4980392156862745', 'u_average_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_average_Magnitude', '0.6666666666666666', '0.6666666666666666', '1', 'u_stddev_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_stddev_Y', '0', '0', '0', 'u_stddev_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_stddev_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'vtkValidPointMask', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Y', '1', '0.5000076295109483', '0', 'Points_Z', '0', '0.3333333333333333', '1', 'Points_Magnitude', '0', '0', '0']
plotOverLine1Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'TKE', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesLabelPrefix = ''
plotOverLine1Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'TKE', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
plotOverLine1Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'TKE', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
plotOverLine1Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'TKE', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'TKE', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# show data from plotOverLine2
plotOverLine2Display = Show(plotOverLine2, lineChartView2, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine2Display.CompositeDataSetIndex = [0]
plotOverLine2Display.UseIndexForXAxis = 0
plotOverLine2Display.XArrayName = 'TKE'
plotOverLine2Display.SeriesVisibility = ['Points_Z']
plotOverLine2Display.SeriesLabel = ['arc_length', 'arc_length', 'TKE', 'TKE', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'y/ymax = 0.75', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine2Display.SeriesColor = ['arc_length', '0', '0', '0', 'TKE', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_average_Magnitude', '1', '0.5000076295109483', '0', 'u_stddev_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_stddev_Y', '0', '0', '0', 'u_stddev_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_stddev_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'vtkValidPointMask', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Y', '1', '0.5000076295109483', '0', 'Points_Z', '1', '0', '0.4980392156862745', 'Points_Magnitude', '0', '0', '0']
plotOverLine2Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'TKE', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
plotOverLine2Display.SeriesLabelPrefix = ''
plotOverLine2Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'TKE', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
plotOverLine2Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'TKE', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
plotOverLine2Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'TKE', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
plotOverLine2Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'TKE', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from slice1
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'u'
uLUT = GetColorTransferFunction('u')
uLUT.RGBPoints = [0.0021724951797631314, 0.231373, 0.298039, 0.752941, 3.4459606324397205, 0.865003, 0.865003, 0.865003, 6.889748769699677, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

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
slice1Display.ScaleFactor = 4.0
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.GaussianRadius = 0.2
slice1Display.SetScaleArray = ['POINTS', 'u']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'u']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-1.3126041889190674, 0.0, 0.5, 0.0, 0.8793625831604004, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-1.3126041889190674, 0.0, 0.5, 0.0, 0.8793625831604004, 1.0, 0.5, 0.0]

# show data from glyph1
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', '']
glyph1Display.LookupTable = uLUT
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'None'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'u'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'u'
glyph1Display.ScaleFactor = 4.704085850715638
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.23520429253578187
glyph1Display.SetScaleArray = ['POINTS', 'u']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'u']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [-1.3126041889190674, 0.0, 0.5, 0.0, 0.8793625831604004, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [-1.3126041889190674, 0.0, 0.5, 0.0, 0.8793625831604004, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.Orientation = 'Horizontal'
uLUTColorBar.WindowLocation = 'AnyLocation'
uLUTColorBar.Position = [0.31811359867330014, 0.029850746268656716]
uLUTColorBar.Title = 'u'
uLUTColorBar.ComponentTitle = 'Magnitude'
uLUTColorBar.ScalarBarLength = 0.32999999999999996

# set color bar visibility
uLUTColorBar.Visibility = 1

# show color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'u'
uPWF = GetOpacityTransferFunction('u')
uPWF.Points = [0.0021724951797631314, 0.0, 0.5, 0.0, 6.889748769699677, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(uxdmf)
# ----------------------------------------------------------------

import os.path
from os import path

i = 0
for t in extractTimeSteps1.TimestepValues:
    renderView1.ViewTime = t
    
    sm = servermanager.Fetch(slice1)
    r = sm.GetPointData().GetArray('u').GetRange(0)
    uLUT = GetColorTransferFunction('u')
    uLUT.RescaleTransferFunction(0, r[1]-r[1]/4)
    
    if not path.exists('./images/rv%3.3d.png' % (i)):
        print("Rendering:", t)
        SaveScreenshot('./images/rv%3.3d.png' % (i), renderView1, ImageResolution=[1312, 534])
    else:
        print("Skipping, rendered")
    i += 1
    
# save temporal statistics
SaveScreenshot('./images/mv.png', lineChartView1, ImageResolution=[646, 534])
SaveScreenshot('./images/tke.png', lineChartView2, ImageResolution=[646, 534])

print("Exiting")
exit()
print("Exiting - shouldnt be here")

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='./output')
