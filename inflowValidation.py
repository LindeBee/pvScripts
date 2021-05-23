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
lineChartView1.ViewSize = [918, 844]
lineChartView1.LegendPosition = [20, 651]
lineChartView1.LeftAxisUseCustomRange = 1
lineChartView1.LeftAxisRangeMinimum = -0.028823808000000062
lineChartView1.LeftAxisRangeMaximum = 3.0288238080000007
lineChartView1.BottomAxisUseCustomRange = 1
lineChartView1.BottomAxisRangeMinimum = -0.013451110399999994
lineChartView1.BottomAxisRangeMaximum = 1.4134511103999998
lineChartView1.RightAxisUseCustomRange = 1
lineChartView1.RightAxisRangeMinimum = -0.06398885375999996
lineChartView1.RightAxisRangeMaximum = 6.72398885376
lineChartView1.TopAxisUseCustomRange = 1
lineChartView1.TopAxisRangeMinimum = -0.06398885375999996
lineChartView1.TopAxisRangeMaximum = 6.72398885376
lineChartView1.LeftAxisTitle = 'z/H'
lineChartView1.BottomAxisTitle = '<u/u_H>'

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
lineChartView2.ViewSize = [916, 844]
lineChartView2.LegendPosition = [770, 791]
lineChartView2.LeftAxisRangeMaximum = 3.0
lineChartView2.BottomAxisRangeMaximum = 0.04
lineChartView2.RightAxisRangeMaximum = 6.66
lineChartView2.TopAxisRangeMaximum = 6.66
lineChartView1.LeftAxisTitle = 'z/H'
lineChartView1.BottomAxisTitle = '<tke/u_H>'

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.500000)
layout1.AssignView(1, lineChartView1)
layout1.AssignView(2, lineChartView2)
layout1.SetSize(1835, 844)

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

# create a new 'Temporal Statistics'
temporalStatistics1 = TemporalStatistics(registrationName='TemporalStatistics1', Input=uxdmf)
temporalStatistics1.ComputeMinimum = 0
temporalStatistics1.ComputeMaximum = 0

# create a new 'Line'
line1 = Line(registrationName='Line1')
line1.Point1 = [0.0, 0.0, 0.0]
line1.Point2 = [0.0, 0.0, 3.0]
line1.Resolution = 100

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=line1)
calculator1.Function = '((coordsZ*2)/2)^0.25'

# create a new 'Plot Data'
plotData4 = PlotData(registrationName='PlotData4', Input=calculator1)

# create a new 'Box'
box1 = Box(registrationName='Box1')
box1.XLength = 0.5
box1.YLength = 0.5
box1.Center = [0.0, 0.0, 0.5]

# create a new 'CSV Reader'
inflowcsv = CSVReader(registrationName='inflow.csv', FileName=['./pvScripts/inflow.csv'])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(registrationName='TableToPoints1', Input=inflowcsv)
tableToPoints1.XColumn = 'x/H'
tableToPoints1.YColumn = 'y/H'
tableToPoints1.ZColumn = 'z/H'

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=tableToPoints1)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Translate = [0.25, 0.0, 0.0]

# create a new 'Clip'
x125exp = Clip(registrationName='=-1.25(exp)', Input=transform1)
x125exp.ClipType = 'Box'
x125exp.HyperTreeGridClipper = 'Plane'
x125exp.Scalars = ['POINTS', '<tke/uH>']
x125exp.Value = 0.02521

# init the 'Box' selected for 'ClipType'
x125exp.ClipType.Position = [-1.5, -0.5, 0.0]
x125exp.ClipType.Length = [0.5, 1.0, 3.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
x125exp.HyperTreeGridClipper.Origin = [-1.25, 0.0, 1.5025]

# create a new 'Plot Data'
plotData2 = PlotData(registrationName='PlotData2', Input=x125exp)

# create a new 'Plot Data'
tkex125exp = PlotData(registrationName='PlotData8', Input=x125exp)

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=line1)
calculator2.Function = '(1/ln((2+0.06)/0.06))*ln((2*coordsZ+0.06+0.15)/0.06)-0.02'

# create a new 'Plot Data'
plotData5 = PlotData(registrationName='PlotData5', Input=calculator2)

# create a new 'Clip'
x025exp = Clip(registrationName='x=0.25(exp)', Input=transform1)
x025exp.ClipType = 'Box'
x025exp.HyperTreeGridClipper = 'Plane'
x025exp.Scalars = ['POINTS', '<tke/uH>']
x025exp.Value = 0.02521

# init the 'Box' selected for 'ClipType'
x025exp.ClipType.Position = [0.0, -0.5, 0.0]
x025exp.ClipType.Length = [0.5, 1.0, 3.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
x025exp.HyperTreeGridClipper.Origin = [-1.25, 0.0, 1.5025]

# create a new 'Plot Data'
tkex025exp = PlotData(registrationName='PlotData7', Input=x025exp)

# create a new 'Plot Data'
plotData3 = PlotData(registrationName='PlotData3', Input=x025exp)

# create a new 'Clip'
x225exp = Clip(registrationName='x=-2.25(exp)', Input=transform1)
x225exp.ClipType = 'Box'
x225exp.HyperTreeGridClipper = 'Plane'
x225exp.Scalars = ['POINTS', '<tke/uH>']
x225exp.Value = 0.02521

# init the 'Box' selected for 'ClipType'
x225exp.ClipType.Position = [-2.5, -0.5, 0.0]
x225exp.ClipType.Length = [0.5, 1.0, 3.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
x225exp.HyperTreeGridClipper.Origin = [-1.25, 0.0, 1.5025]

# create a new 'Plot Data'
plotData1 = PlotData(registrationName='PlotData1', Input=x225exp)

# create a new 'Plot Data'
tkex225exp = PlotData(registrationName='PlotData6', Input=x225exp)

# create a new 'Transform'
transform2 = Transform(registrationName='Transform2', Input=temporalStatistics1)
transform2.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform2.Transform.Scale = [0.5, 0.5, 0.5]

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=transform2)
calculator3.Function = '0.5*(u_stddev_X^2+u_stddev_Y^2+u_stddev_Z^2)'

# create a new 'Plot Over Line'
tkex125sim = PlotOverLine(registrationName='PlotOverLine2', Input=calculator3,
    Source='Line')

# init the 'Line' selected for 'Source'
tkex125sim.Source.Point1 = [-1.25, 0.0, 0.0]
tkex125sim.Source.Point2 = [-1.25, 0.0, 3.0]

# create a new 'Plot Over Line'
tkex025sim = PlotOverLine(registrationName='PlotOverLine3', Input=calculator3,
    Source='Line')

# init the 'Line' selected for 'Source'
tkex025sim.Source.Point1 = [0.25, 0.0, 0.0]
tkex025sim.Source.Point2 = [0.25, 0.0, 3.0]

# create a new 'Plot Over Line'
tkex225sim = PlotOverLine(registrationName='PlotOverLine1', Input=calculator3,
    Source='Line')

# init the 'Line' selected for 'Source'
tkex225sim.Source.Point1 = [-2.25, 0.0, 0.0]
tkex225sim.Source.Point2 = [-2.25, 0.0, 3.0]

# create a new 'Plot Over Line'
x125sim = PlotOverLine(registrationName='x=-1.25(sim)', Input=transform2,
    Source='Line')

# init the 'Line' selected for 'Source'
x125sim.Source.Point1 = [-1.25, 0.0, 0.0]
x125sim.Source.Point2 = [-1.25, 0.0, 3.0]

# create a new 'Plot Over Line'
x025sim = PlotOverLine(registrationName='x=0.25(sim)', Input=transform2,
    Source='Line')

# init the 'Line' selected for 'Source'
x025sim.Source.Point1 = [0.25, 0.0, 0.0]
x025sim.Source.Point2 = [0.25, 0.0, 3.0]

# create a new 'Plot Over Line'
x225sim = PlotOverLine(registrationName='x=-2.25(sim)', Input=transform2,
    Source='Line')

# init the 'Line' selected for 'Source'
x225sim.Source.Point1 = [-2.25, 0.0, 0.0]
x225sim.Source.Point2 = [-2.25, 0.0, 3.0]

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView1'
# ----------------------------------------------------------------

# show data from plotData1
plotData1Display = Show(plotData1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotData1Display.CompositeDataSetIndex = [0]
plotData1Display.UseIndexForXAxis = 0
plotData1Display.XArrayName = '<u/uH>'
plotData1Display.SeriesVisibility = ['Points_Z']
plotData1Display.SeriesLabel = ['<tke/uH>', '<tke/uH>', '<u/uH>', '<u/uH>', 'nsu', 'nsu', 'nsv', 'nsv', 'nsw', 'nsw', 'ssuv', 'ssuv', 'ssuw', 'ssuw', 'Unsu', 'Unsu', 'Unsv', 'Unsv', 'Unsw', 'Unsw', 'Ussuv', 'Ussuv', 'Ussuw', 'Ussuw', 'Utke', 'Utke', 'Uu', 'Uu', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'x/H = -2.25', 'Points_Magnitude', 'Points_Magnitude']
plotData1Display.SeriesColor = ['<tke/uH>', '0', '0', '0', '<u/uH>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'nsu', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'nsv', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'nsw', '0.6', '0.3100022888532845', '0.6399938963912413', 'ssuv', '1', '0.5000076295109483', '0', 'ssuw', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Unsu', '0', '0', '0', 'Unsv', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Unsw', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Ussuv', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Ussuw', '0.6', '0.3100022888532845', '0.6399938963912413', 'Utke', '1', '0.5000076295109483', '0', 'Uu', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
plotData1Display.SeriesPlotCorner = ['<tke/uH>', '0', '<u/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Unsu', '0', 'Unsv', '0', 'Unsw', '0', 'Ussuv', '0', 'Ussuw', '0', 'Utke', '0', 'Uu', '0', 'nsu', '0', 'nsv', '0', 'nsw', '0', 'ssuv', '0', 'ssuw', '0']
plotData1Display.SeriesLabelPrefix = ''
plotData1Display.SeriesLineStyle = ['<tke/uH>', '1', '<u/uH>', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '0', 'Unsu', '1', 'Unsv', '1', 'Unsw', '1', 'Ussuv', '1', 'Ussuw', '1', 'Utke', '1', 'Uu', '1', 'nsu', '1', 'nsv', '1', 'nsw', '1', 'ssuv', '1', 'ssuw', '1']
plotData1Display.SeriesLineThickness = ['<tke/uH>', '2', '<u/uH>', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Unsu', '2', 'Unsv', '2', 'Unsw', '2', 'Ussuv', '2', 'Ussuw', '2', 'Utke', '2', 'Uu', '2', 'nsu', '2', 'nsv', '2', 'nsw', '2', 'ssuv', '2', 'ssuw', '2']
plotData1Display.SeriesMarkerStyle = ['<tke/uH>', '0', '<u/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '3', 'Unsu', '0', 'Unsv', '0', 'Unsw', '0', 'Ussuv', '0', 'Ussuw', '0', 'Utke', '0', 'Uu', '0', 'nsu', '0', 'nsv', '0', 'nsw', '0', 'ssuv', '0', 'ssuw', '0']
plotData1Display.SeriesMarkerSize = ['<tke/uH>', '4', '<u/uH>', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '9', 'Unsu', '4', 'Unsv', '4', 'Unsw', '4', 'Ussuv', '4', 'Ussuw', '4', 'Utke', '4', 'Uu', '4', 'nsu', '4', 'nsv', '4', 'nsw', '4', 'ssuv', '4', 'ssuw', '4']


# show data from x225sim
x225simDisplay = Show(x225sim, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
x225simDisplay.CompositeDataSetIndex = [0]
x225simDisplay.UseIndexForXAxis = 0
x225simDisplay.XArrayName = 'u_average_Magnitude'
x225simDisplay.SeriesVisibility = ['Points_Z']
x225simDisplay.SeriesLabel = ['arc_length', 'arc_length', 'u_X', 'u_X', 'u_Y', 'u_Y', 'u_Z', 'u_Z', 'u_Magnitude', 'u_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'x/H = -2.25', 'Points_Magnitude', 'Points_Magnitude', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude']
x225simDisplay.SeriesColor = ['arc_length', '0', '0', '0', 'u_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.5372549019607843', '0.7450980392156863', '1', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_average_Z', '1', '0.5000076295109483', '0', 'u_average_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_stddev_X', '0', '0', '0', 'u_stddev_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_stddev_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_stddev_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
x225simDisplay.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_Magnitude', '0', 'u_X', '0', 'u_Y', '0', 'u_Z', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
x225simDisplay.SeriesLabelPrefix = ''
x225simDisplay.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_Magnitude', '1', 'u_X', '1', 'u_Y', '1', 'u_Z', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
x225simDisplay.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_Magnitude', '2', 'u_X', '2', 'u_Y', '2', 'u_Z', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
x225simDisplay.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_Magnitude', '0', 'u_X', '0', 'u_Y', '0', 'u_Z', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
x225simDisplay.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_Magnitude', '4', 'u_X', '4', 'u_Y', '4', 'u_Z', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# show data from plotData2
plotData2Display = Show(plotData2, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotData2Display.CompositeDataSetIndex = [0]
plotData2Display.UseIndexForXAxis = 0
plotData2Display.XArrayName = '<u/uH>'
plotData2Display.SeriesVisibility = ['Points_Z']
plotData2Display.SeriesLabel = ['<tke/uH>', '<tke/uH>', '<u/uH>', '<u/uH>', 'nsu', 'nsu', 'nsv', 'nsv', 'nsw', 'nsw', 'ssuv', 'ssuv', 'ssuw', 'ssuw', 'Unsu', 'Unsu', 'Unsv', 'Unsv', 'Unsw', 'Unsw', 'Ussuv', 'Ussuv', 'Ussuw', 'Ussuw', 'Utke', 'Utke', 'Uu', 'Uu', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'x/H = -1.25', 'Points_Magnitude', 'Points_Magnitude']
plotData2Display.SeriesColor = ['<tke/uH>', '0', '0', '0', '<u/uH>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'nsu', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'nsv', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'nsw', '0.6', '0.3100022888532845', '0.6399938963912413', 'ssuv', '1', '0.5000076295109483', '0', 'ssuw', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Unsu', '0', '0', '0', 'Unsv', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Unsw', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Ussuv', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Ussuw', '0.6', '0.3100022888532845', '0.6399938963912413', 'Utke', '1', '0.5000076295109483', '0', 'Uu', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.3333333333333333', '0', '0.4980392156862745', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
plotData2Display.SeriesPlotCorner = ['<tke/uH>', '0', '<u/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Unsu', '0', 'Unsv', '0', 'Unsw', '0', 'Ussuv', '0', 'Ussuw', '0', 'Utke', '0', 'Uu', '0', 'nsu', '0', 'nsv', '0', 'nsw', '0', 'ssuv', '0', 'ssuw', '0']
plotData2Display.SeriesLabelPrefix = ''
plotData2Display.SeriesLineStyle = ['<tke/uH>', '1', '<u/uH>', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '0', 'Unsu', '1', 'Unsv', '1', 'Unsw', '1', 'Ussuv', '1', 'Ussuw', '1', 'Utke', '1', 'Uu', '1', 'nsu', '1', 'nsv', '1', 'nsw', '1', 'ssuv', '1', 'ssuw', '1']
plotData2Display.SeriesLineThickness = ['<tke/uH>', '2', '<u/uH>', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Unsu', '2', 'Unsv', '2', 'Unsw', '2', 'Ussuv', '2', 'Ussuw', '2', 'Utke', '2', 'Uu', '2', 'nsu', '2', 'nsv', '2', 'nsw', '2', 'ssuv', '2', 'ssuw', '2']
plotData2Display.SeriesMarkerStyle = ['<tke/uH>', '0', '<u/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '5', 'Unsu', '0', 'Unsv', '0', 'Unsw', '0', 'Ussuv', '0', 'Ussuw', '0', 'Utke', '0', 'Uu', '0', 'nsu', '0', 'nsv', '0', 'nsw', '0', 'ssuv', '0', 'ssuw', '0']
plotData2Display.SeriesMarkerSize = ['<tke/uH>', '4', '<u/uH>', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '9', 'Unsu', '4', 'Unsv', '4', 'Unsw', '4', 'Ussuv', '4', 'Ussuw', '4', 'Utke', '4', 'Uu', '4', 'nsu', '4', 'nsv', '4', 'nsw', '4', 'ssuv', '4', 'ssuw', '4']

# show data from x125sim
x125simDisplay = Show(x125sim, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
x125simDisplay.CompositeDataSetIndex = [0]
x125simDisplay.UseIndexForXAxis = 0
x125simDisplay.XArrayName = 'u_average_Magnitude'
x125simDisplay.SeriesVisibility = ['Points_Z']
x125simDisplay.SeriesLabel = ['arc_length', 'arc_length', 'u_X', 'u_X', 'u_Y', 'u_Y', 'u_Z', 'u_Z', 'u_Magnitude', 'u_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'x/H= -1.25', 'Points_Magnitude', 'Points_Magnitude', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude']
x125simDisplay.SeriesColor = ['arc_length', '0', '0', '0', 'u_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.6666666666666666', '0.3333333333333333', '1', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_average_Z', '1', '0.5000076295109483', '0', 'u_average_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_stddev_X', '0', '0', '0', 'u_stddev_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_stddev_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_stddev_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
x125simDisplay.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_Magnitude', '0', 'u_X', '0', 'u_Y', '0', 'u_Z', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
x125simDisplay.SeriesLabelPrefix = ''
x125simDisplay.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_Magnitude', '1', 'u_X', '1', 'u_Y', '1', 'u_Z', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
x125simDisplay.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_Magnitude', '2', 'u_X', '2', 'u_Y', '2', 'u_Z', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
x125simDisplay.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_Magnitude', '0', 'u_X', '0', 'u_Y', '0', 'u_Z', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
x125simDisplay.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_Magnitude', '4', 'u_X', '4', 'u_Y', '4', 'u_Z', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# show data from plotData3
plotData3Display = Show(plotData3, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotData3Display.CompositeDataSetIndex = [0]
plotData3Display.UseIndexForXAxis = 0
plotData3Display.XArrayName = '<u/uH>'
plotData3Display.SeriesVisibility = ['Points_Z']
plotData3Display.SeriesLabel = ['<tke/uH>', '<tke/uH>', '<u/uH>', '<u/uH>', 'nsu', 'nsu', 'nsv', 'nsv', 'nsw', 'nsw', 'ssuv', 'ssuv', 'ssuw', 'ssuw', 'Unsu', 'Unsu', 'Unsv', 'Unsv', 'Unsw', 'Unsw', 'Ussuv', 'Ussuv', 'Ussuw', 'Ussuw', 'Utke', 'Utke', 'Uu', 'Uu', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'x/H =0.25', 'Points_Magnitude', 'Points_Magnitude']
plotData3Display.SeriesColor = ['<tke/uH>', '0', '0', '0', '<u/uH>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'nsu', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'nsv', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'nsw', '0.6', '0.3100022888532845', '0.6399938963912413', 'ssuv', '1', '0.5000076295109483', '0', 'ssuw', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Unsu', '0', '0', '0', 'Unsv', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Unsw', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Ussuv', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Ussuw', '0.6', '0.3100022888532845', '0.6399938963912413', 'Utke', '1', '0.5000076295109483', '0', 'Uu', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.3333333333333333', '0.6666666666666666', '0', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
plotData3Display.SeriesPlotCorner = ['<tke/uH>', '0', '<u/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Unsu', '0', 'Unsv', '0', 'Unsw', '0', 'Ussuv', '0', 'Ussuw', '0', 'Utke', '0', 'Uu', '0', 'nsu', '0', 'nsv', '0', 'nsw', '0', 'ssuv', '0', 'ssuw', '0']
plotData3Display.SeriesLabelPrefix = ''
plotData3Display.SeriesLineStyle = ['<tke/uH>', '1', '<u/uH>', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '0', 'Unsu', '1', 'Unsv', '1', 'Unsw', '1', 'Ussuv', '1', 'Ussuw', '1', 'Utke', '1', 'Uu', '1', 'nsu', '1', 'nsv', '1', 'nsw', '1', 'ssuv', '1', 'ssuw', '1']
plotData3Display.SeriesLineThickness = ['<tke/uH>', '2', '<u/uH>', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Unsu', '2', 'Unsv', '2', 'Unsw', '2', 'Ussuv', '2', 'Ussuw', '2', 'Utke', '2', 'Uu', '2', 'nsu', '2', 'nsv', '2', 'nsw', '2', 'ssuv', '2', 'ssuw', '2']
plotData3Display.SeriesMarkerStyle = ['<tke/uH>', '0', '<u/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '4', 'Unsu', '0', 'Unsv', '0', 'Unsw', '0', 'Ussuv', '0', 'Ussuw', '0', 'Utke', '0', 'Uu', '0', 'nsu', '0', 'nsv', '0', 'nsw', '0', 'ssuv', '0', 'ssuw', '0']
plotData3Display.SeriesMarkerSize = ['<tke/uH>', '4', '<u/uH>', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '9', 'Unsu', '4', 'Unsv', '4', 'Unsw', '4', 'Ussuv', '4', 'Ussuw', '4', 'Utke', '4', 'Uu', '4', 'nsu', '4', 'nsv', '4', 'nsw', '4', 'ssuv', '4', 'ssuw', '4']

# show data from x025sim
x025simDisplay = Show(x025sim, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
x025simDisplay.CompositeDataSetIndex = [0]
x025simDisplay.UseIndexForXAxis = 0
x025simDisplay.XArrayName = 'u_average_Magnitude'
x025simDisplay.SeriesVisibility = ['Points_Z']
x025simDisplay.SeriesLabel = ['arc_length', 'arc_length', 'u_X', 'u_X', 'u_Y', 'u_Y', 'u_Z', 'u_Z', 'u_Magnitude', 'u_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'x/H = 0.25', 'Points_Magnitude', 'Points_Magnitude', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude']
x025simDisplay.SeriesColor = ['arc_length', '0', '0', '0', 'u_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.5647058823529412', '0.7568627450980392', '0.43529411764705883', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Y', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_average_Z', '1', '0.5000076295109483', '0', 'u_average_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_stddev_X', '0', '0', '0', 'u_stddev_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_stddev_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_stddev_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
x025simDisplay.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_Magnitude', '0', 'u_X', '0', 'u_Y', '0', 'u_Z', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
x025simDisplay.SeriesLabelPrefix = ''
x025simDisplay.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_Magnitude', '1', 'u_X', '1', 'u_Y', '1', 'u_Z', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
x025simDisplay.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_Magnitude', '2', 'u_X', '2', 'u_Y', '2', 'u_Z', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
x025simDisplay.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_Magnitude', '0', 'u_X', '0', 'u_Y', '0', 'u_Z', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
x025simDisplay.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_Magnitude', '4', 'u_X', '4', 'u_Y', '4', 'u_Z', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView2'
# ----------------------------------------------------------------

# show data from tkex225exp
tkex225expDisplay = Show(tkex225exp, lineChartView2, 'XYChartRepresentation')

# trace defaults for the display properties.
tkex225expDisplay.CompositeDataSetIndex = [0]
tkex225expDisplay.UseIndexForXAxis = 0
tkex225expDisplay.XArrayName = '<tke/uH>'
tkex225expDisplay.SeriesVisibility = ['Points_Z']
tkex225expDisplay.SeriesLabel = ['<tke/uH>', '<tke/uH>', '<u/uH>', '<u/uH>', 'nsu', 'nsu', 'nsv', 'nsv', 'nsw', 'nsw', 'ssuv', 'ssuv', 'ssuw', 'ssuw', 'Unsu', 'Unsu', 'Unsv', 'Unsv', 'Unsw', 'Unsw', 'Ussuv', 'Ussuv', 'Ussuw', 'Ussuw', 'Utke', 'Utke', 'Uu', 'Uu', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tkex225expDisplay.SeriesColor = ['<tke/uH>', '0', '0', '0', '<u/uH>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'nsu', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'nsv', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'nsw', '0.6', '0.3100022888532845', '0.6399938963912413', 'ssuv', '1', '0.5000076295109483', '0', 'ssuw', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Unsu', '0', '0', '0', 'Unsv', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Unsw', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Ussuv', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Ussuw', '0.6', '0.3100022888532845', '0.6399938963912413', 'Utke', '1', '0.5000076295109483', '0', 'Uu', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
tkex225expDisplay.SeriesPlotCorner = ['<tke/uH>', '0', '<u/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Unsu', '0', 'Unsv', '0', 'Unsw', '0', 'Ussuv', '0', 'Ussuw', '0', 'Utke', '0', 'Uu', '0', 'nsu', '0', 'nsv', '0', 'nsw', '0', 'ssuv', '0', 'ssuw', '0']
tkex225expDisplay.SeriesLabelPrefix = ''
tkex225expDisplay.SeriesLineStyle = ['<tke/uH>', '1', '<u/uH>', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '0', 'Unsu', '1', 'Unsv', '1', 'Unsw', '1', 'Ussuv', '1', 'Ussuw', '1', 'Utke', '1', 'Uu', '1', 'nsu', '1', 'nsv', '1', 'nsw', '1', 'ssuv', '1', 'ssuw', '1']
tkex225expDisplay.SeriesLineThickness = ['<tke/uH>', '2', '<u/uH>', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Unsu', '2', 'Unsv', '2', 'Unsw', '2', 'Ussuv', '2', 'Ussuw', '2', 'Utke', '2', 'Uu', '2', 'nsu', '2', 'nsv', '2', 'nsw', '2', 'ssuv', '2', 'ssuw', '2']
tkex225expDisplay.SeriesMarkerStyle = ['<tke/uH>', '0', '<u/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '3', 'Unsu', '0', 'Unsv', '0', 'Unsw', '0', 'Ussuv', '0', 'Ussuw', '0', 'Utke', '0', 'Uu', '0', 'nsu', '0', 'nsv', '0', 'nsw', '0', 'ssuv', '0', 'ssuw', '0']
tkex225expDisplay.SeriesMarkerSize = ['<tke/uH>', '4', '<u/uH>', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '9', 'Unsu', '4', 'Unsv', '4', 'Unsw', '4', 'Ussuv', '4', 'Ussuw', '4', 'Utke', '4', 'Uu', '4', 'nsu', '4', 'nsv', '4', 'nsw', '4', 'ssuv', '4', 'ssuw', '4']

# show data from tkex225sim
tkex225simDisplay = Show(tkex225sim, lineChartView2, 'XYChartRepresentation')

# trace defaults for the display properties.
tkex225simDisplay.CompositeDataSetIndex = [0]
tkex225simDisplay.UseIndexForXAxis = 0
tkex225simDisplay.XArrayName = 'Result'
tkex225simDisplay.SeriesVisibility = ['Points_Z']
tkex225simDisplay.SeriesLabel = ['arc_length', 'arc_length', 'Result', 'Result', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tkex225simDisplay.SeriesColor = ['arc_length', '0', '0', '0', 'Result', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_average_Magnitude', '1', '0.5000076295109483', '0', 'u_stddev_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_stddev_Y', '0', '0', '0', 'u_stddev_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_stddev_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'vtkValidPointMask', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Y', '1', '0.5000076295109483', '0', 'Points_Z', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Magnitude', '0', '0', '0']
tkex225simDisplay.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Result', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tkex225simDisplay.SeriesLabelPrefix = ''
tkex225simDisplay.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Result', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
tkex225simDisplay.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Result', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
tkex225simDisplay.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Result', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tkex225simDisplay.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Result', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# show data from tkex125exp
tkex125expDisplay = Show(tkex125exp, lineChartView2, 'XYChartRepresentation')

# trace defaults for the display properties.
tkex125expDisplay.CompositeDataSetIndex = [0]
tkex125expDisplay.UseIndexForXAxis = 0
tkex125expDisplay.XArrayName = '<tke/uH>'
tkex125expDisplay.SeriesVisibility = ['Points_Z']
tkex125expDisplay.SeriesLabel = ['<tke/uH>', '<tke/uH>', '<u/uH>', '<u/uH>', 'nsu', 'nsu', 'nsv', 'nsv', 'nsw', 'nsw', 'ssuv', 'ssuv', 'ssuw', 'ssuw', 'Unsu', 'Unsu', 'Unsv', 'Unsv', 'Unsw', 'Unsw', 'Ussuv', 'Ussuv', 'Ussuw', 'Ussuw', 'Utke', 'Utke', 'Uu', 'Uu', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tkex125expDisplay.SeriesColor = ['<tke/uH>', '0', '0', '0', '<u/uH>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'nsu', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'nsv', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'nsw', '0.6', '0.3100022888532845', '0.6399938963912413', 'ssuv', '1', '0.5000076295109483', '0', 'ssuw', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Unsu', '0', '0', '0', 'Unsv', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Unsw', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Ussuv', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Ussuw', '0.6', '0.3100022888532845', '0.6399938963912413', 'Utke', '1', '0.5000076295109483', '0', 'Uu', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.3333333333333333', '0', '0.4980392156862745', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
tkex125expDisplay.SeriesPlotCorner = ['<tke/uH>', '0', '<u/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Unsu', '0', 'Unsv', '0', 'Unsw', '0', 'Ussuv', '0', 'Ussuw', '0', 'Utke', '0', 'Uu', '0', 'nsu', '0', 'nsv', '0', 'nsw', '0', 'ssuv', '0', 'ssuw', '0']
tkex125expDisplay.SeriesLabelPrefix = ''
tkex125expDisplay.SeriesLineStyle = ['<tke/uH>', '1', '<u/uH>', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '0', 'Unsu', '1', 'Unsv', '1', 'Unsw', '1', 'Ussuv', '1', 'Ussuw', '1', 'Utke', '1', 'Uu', '1', 'nsu', '1', 'nsv', '1', 'nsw', '1', 'ssuv', '1', 'ssuw', '1']
tkex125expDisplay.SeriesLineThickness = ['<tke/uH>', '2', '<u/uH>', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Unsu', '2', 'Unsv', '2', 'Unsw', '2', 'Ussuv', '2', 'Ussuw', '2', 'Utke', '2', 'Uu', '2', 'nsu', '2', 'nsv', '2', 'nsw', '2', 'ssuv', '2', 'ssuw', '2']
tkex125expDisplay.SeriesMarkerStyle = ['<tke/uH>', '0', '<u/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '5', 'Unsu', '0', 'Unsv', '0', 'Unsw', '0', 'Ussuv', '0', 'Ussuw', '0', 'Utke', '0', 'Uu', '0', 'nsu', '0', 'nsv', '0', 'nsw', '0', 'ssuv', '0', 'ssuw', '0']
tkex125expDisplay.SeriesMarkerSize = ['<tke/uH>', '4', '<u/uH>', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '9', 'Unsu', '4', 'Unsv', '4', 'Unsw', '4', 'Ussuv', '4', 'Ussuw', '4', 'Utke', '4', 'Uu', '4', 'nsu', '4', 'nsv', '4', 'nsw', '4', 'ssuv', '4', 'ssuw', '4']

# show data from tkex125sim
tkex125simDisplay = Show(tkex125sim, lineChartView2, 'XYChartRepresentation')

# trace defaults for the display properties.
tkex125simDisplay.CompositeDataSetIndex = [0]
tkex125simDisplay.UseIndexForXAxis = 0
tkex125simDisplay.XArrayName = 'Result'
tkex125simDisplay.SeriesVisibility = ['Points_Z']
tkex125simDisplay.SeriesLabel = ['arc_length', 'arc_length', 'Result', 'Result', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tkex125simDisplay.SeriesColor = ['arc_length', '0', '0', '0', 'Result', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_average_Magnitude', '1', '0.5000076295109483', '0', 'u_stddev_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_stddev_Y', '0', '0', '0', 'u_stddev_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_stddev_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'vtkValidPointMask', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Y', '1', '0.5000076295109483', '0', 'Points_Z', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Magnitude', '0', '0', '0']
tkex125simDisplay.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Result', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tkex125simDisplay.SeriesLabelPrefix = ''
tkex125simDisplay.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Result', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
tkex125simDisplay.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Result', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
tkex125simDisplay.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Result', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tkex125simDisplay.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Result', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# show data from tkex025exp
tkex025expDisplay = Show(tkex025exp, lineChartView2, 'XYChartRepresentation')

# trace defaults for the display properties.
tkex025expDisplay.CompositeDataSetIndex = [0]
tkex025expDisplay.UseIndexForXAxis = 0
tkex025expDisplay.XArrayName = '<tke/uH>'
tkex025expDisplay.SeriesVisibility = ['Points_Z']
tkex025expDisplay.SeriesLabel = ['<tke/uH>', '<tke/uH>', '<u/uH>', '<u/uH>', 'nsu', 'nsu', 'nsv', 'nsv', 'nsw', 'nsw', 'ssuv', 'ssuv', 'ssuw', 'ssuw', 'Unsu', 'Unsu', 'Unsv', 'Unsv', 'Unsw', 'Unsw', 'Ussuv', 'Ussuv', 'Ussuw', 'Ussuw', 'Utke', 'Utke', 'Uu', 'Uu', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tkex025expDisplay.SeriesColor = ['<tke/uH>', '0', '0', '0', '<u/uH>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'nsu', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'nsv', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'nsw', '0.6', '0.3100022888532845', '0.6399938963912413', 'ssuv', '1', '0.5000076295109483', '0', 'ssuw', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Unsu', '0', '0', '0', 'Unsv', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Unsw', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Ussuv', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Ussuw', '0.6', '0.3100022888532845', '0.6399938963912413', 'Utke', '1', '0.5000076295109483', '0', 'Uu', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.3333333333333333', '0.6666666666666666', '0', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
tkex025expDisplay.SeriesPlotCorner = ['<tke/uH>', '0', '<u/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Unsu', '0', 'Unsv', '0', 'Unsw', '0', 'Ussuv', '0', 'Ussuw', '0', 'Utke', '0', 'Uu', '0', 'nsu', '0', 'nsv', '0', 'nsw', '0', 'ssuv', '0', 'ssuw', '0']
tkex025expDisplay.SeriesLabelPrefix = ''
tkex025expDisplay.SeriesLineStyle = ['<tke/uH>', '1', '<u/uH>', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '0', 'Unsu', '1', 'Unsv', '1', 'Unsw', '1', 'Ussuv', '1', 'Ussuw', '1', 'Utke', '1', 'Uu', '1', 'nsu', '1', 'nsv', '1', 'nsw', '1', 'ssuv', '1', 'ssuw', '1']
tkex025expDisplay.SeriesLineThickness = ['<tke/uH>', '2', '<u/uH>', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Unsu', '2', 'Unsv', '2', 'Unsw', '2', 'Ussuv', '2', 'Ussuw', '2', 'Utke', '2', 'Uu', '2', 'nsu', '2', 'nsv', '2', 'nsw', '2', 'ssuv', '2', 'ssuw', '2']
tkex025expDisplay.SeriesMarkerStyle = ['<tke/uH>', '0', '<u/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '4', 'Unsu', '0', 'Unsv', '0', 'Unsw', '0', 'Ussuv', '0', 'Ussuw', '0', 'Utke', '0', 'Uu', '0', 'nsu', '0', 'nsv', '0', 'nsw', '0', 'ssuv', '0', 'ssuw', '0']
tkex025expDisplay.SeriesMarkerSize = ['<tke/uH>', '4', '<u/uH>', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '9', 'Unsu', '4', 'Unsv', '4', 'Unsw', '4', 'Ussuv', '4', 'Ussuw', '4', 'Utke', '4', 'Uu', '4', 'nsu', '4', 'nsv', '4', 'nsw', '4', 'ssuv', '4', 'ssuw', '4']

# show data from tkex025sim
tkex025simDisplay = Show(tkex025sim, lineChartView2, 'XYChartRepresentation')

# trace defaults for the display properties.
tkex025simDisplay.CompositeDataSetIndex = [0]
tkex025simDisplay.UseIndexForXAxis = 0
tkex025simDisplay.XArrayName = 'Result'
tkex025simDisplay.SeriesVisibility = ['Points_Z']
tkex025simDisplay.SeriesLabel = ['arc_length', 'arc_length', 'Result', 'Result', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tkex025simDisplay.SeriesColor = ['arc_length', '0', '0', '0', 'Result', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_average_Magnitude', '1', '0.5000076295109483', '0', 'u_stddev_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_stddev_Y', '0', '0', '0', 'u_stddev_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_stddev_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'vtkValidPointMask', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Y', '1', '0.5000076295109483', '0', 'Points_Z', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Magnitude', '0', '0', '0']
tkex025simDisplay.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Result', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tkex025simDisplay.SeriesLabelPrefix = ''
tkex025simDisplay.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Result', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
tkex025simDisplay.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Result', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
tkex025simDisplay.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Result', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tkex025simDisplay.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Result', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# ----------------------------------------------------------------
# restore active source
SetActiveSource(tkex025sim)
# ----------------------------------------------------------------

print("Writing u_mag")

aLayout = GetLayout()
SaveScreenshot("./images/inflowValidation.png", layout=aLayout)


print("Exiting")
exit()
print("Exiting - shouldnt be here")

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
