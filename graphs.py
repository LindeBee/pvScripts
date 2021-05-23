# state file generated using paraview version 5.8.1-1634-g6bacce2f26

#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Line Chart View'
error = CreateView('XYChartView')
error.ViewSize = [904, 534]
error.LeftAxisRangeMaximum = 6.66
error.BottomAxisRangeMaximum = 6.66
error.RightAxisRangeMaximum = 6.66
error.TopAxisRangeMaximum = 6.66

# Create a new 'Line Chart View'
mvh = CreateView('XYChartView')
mvh.ViewSize = [904, 534]
mvh.LegendPosition = [728, 229]
mvh.LeftAxisTitle = '<u/u_H>'
mvh.BottomAxisTitle = 'y'

# Create a new 'Line Chart View'
mvv = CreateView('XYChartView')
mvv.ViewSize = [904, 534]
mvv.LegendPosition = [674, 369]
mvv.LeftAxisTitle = 'z'
mvv.BottomAxisTitle = '<u/u_H>'

# Create a new 'Line Chart View'
tke = CreateView('XYChartView')
tke.ViewSize = [904, 534]
tke.LegendPosition = [674, 395]
tke.LeftAxisTitle = 'z'
tke.BottomAxisTitle = '<tke/u_H>'

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.5)
layout1.SplitVertical(1, 0.500000)
layout1.AssignView(3, mvh)
layout1.AssignView(4, error)
layout1.SplitVertical(2, 0.500000)
layout1.AssignView(5, mvv)
layout1.AssignView(6, tke)
layout1.SetSize(1809, 1069)

# ----------------------------------------------------------------
# restore active view
SetActiveView(mvv)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# ABL = '(1/ln((2+0.06)/0.06))*ln((coordsZ+0.06)/0.06)'
ABL = '(1.0*(coordsZ/2.0)^0.25)'

# create a new 'XDMF Reader'
uxdmf = XDMFReader(registrationName='u.xdmf', FileNames=['./results/u.xdmf'])
uxdmf.PointArrayStatus = ['u']
n_steps = len(uxdmf.TimestepValues)
Show(uxdmf)
(xmin,xmax,ymin,ymax,zmin,zmax) = GetActiveSource().GetDataInformation().GetBounds()
Hide(uxdmf)

# create a new 'Line'
lineTVV = Line(registrationName='Line1')
lineTVV.Point1 = [0.0, 0.0, zmin]
lineTVV.Point2 = [0.0, 0.0, zmax]
lineTVV.Resolution = 100

# create a new 'Calculator'
calculatorTVV = Calculator(registrationName='CalculatorMVVtarget', Input=lineTVV)
calculatorTVV.ResultArrayName = 't'
calculatorTVV.Function = ABL

# create a new 'Plot Over Line'
tvv = PlotOverLine(registrationName='tvv', Input=calculatorTVV,
    Source='Line')

# init the 'Line' selected for 'Source'
tvv.Source.Point1 = [0.0, 0.0, zmin]
tvv.Source.Point2 = [0.0, 0.0, zmax]

# create a new 'Line'
lineTVH1 = Line(registrationName='Line2')
lineTVH1.Point1 = [0., ymin, 0.02*zmax]
lineTVH1.Point2 = [0., ymax, 0.02*zmax]

# create a new 'Calculator'
calculatorTVH1 = Calculator(registrationName='CalculatorMVH1', Input=lineTVH1)
calculatorTVH1.ResultArrayName = 'target'
calculatorTVH1.Function = ABL

# create a new 'Plot Over Line'
tvh002 = PlotOverLine(registrationName='tvh0.02', Input=calculatorTVH1,
    Source='Line')

# init the 'Line' selected for 'Source'
tvh002.Source.Point1 = [0., ymin, 0.02*zmax]
tvh002.Source.Point2 = [0., ymax, 0.02*zmax]

# create a new 'Line'
lineTVH2 = Line(registrationName='Line3')
lineTVH2.Point1 = [0., ymin, 0.05*zmax]
lineTVH2.Point2 = [0., ymax, 0.05*zmax]

# create a new 'Calculator'
calculatorTVH2 = Calculator(registrationName='CalculatorMVH2', Input=lineTVH2)
calculatorTVH2.ResultArrayName = 'target'
calculatorTVH2.Function = ABL

# create a new 'Plot Over Line'
tvh005 = PlotOverLine(registrationName='tvh0.05', Input=calculatorTVH2,
    Source='Line')

# init the 'Line' selected for 'Source'
tvh005.Source.Point1 = [0., ymin, 0.05*zmax]
tvh005.Source.Point2 = [0., ymax, 0.05*zmax]

# create a new 'Line'
lineTVH3 = Line(registrationName='Line4')
lineTVH3.Point1 = [0., ymin, 0.1*zmax]
lineTVH3.Point2 = [0., ymax, 0.1*zmax]

# create a new 'Calculator'
calculatorTVH3 = Calculator(registrationName='CalculatorMVH3', Input=lineTVH3)
calculatorTVH3.ResultArrayName = 'target'
calculatorTVH3.Function = ABL

# create a new 'Plot Over Line'
tvh01 = PlotOverLine(registrationName='tvh0.1', Input=calculatorTVH3,
    Source='Line')

# init the 'Line' selected for 'Source'
tvh01.Source.Point1 = [0., ymin, 0.1*zmax]
tvh01.Source.Point2 = [0., ymax, 0.1*zmax]

# create a new 'Line'
lineTVH4 = Line(registrationName='Line5')
lineTVH4.Point1 = [0., ymin, 0.3*zmax]
lineTVH4.Point2 = [0., ymax, 0.3*zmax]

# create a new 'Calculator'
calculatorTVH4 = Calculator(registrationName='Calculator7', Input=lineTVH4)
calculatorTVH4.ResultArrayName = 'target'
calculatorTVH4.Function = ABL

# create a new 'Plot Over Line'
tvh03 = PlotOverLine(registrationName='tvh0.3', Input=calculatorTVH4,
    Source='Line')

# init the 'Line' selected for 'Source'
tvh03.Source.Point1 = [0., ymin, 0.3*zmax]
tvh03.Source.Point2 = [0., ymax, 0.3*zmax]

# create a new 'Line'
lineTVH5 = Line(registrationName='Line6')
lineTVH5.Point1 = [0., ymin, 0.7*zmax]
lineTVH5.Point2 = [0., ymax, 0.7*zmax]

# create a new 'Calculator'
calculatorTVH5 = Calculator(registrationName='Calculator8', Input=lineTVH5)
calculatorTVH5.ResultArrayName = 'target'
calculatorTVH5.Function = ABL

# create a new 'Plot Over Line'
tvh07 = PlotOverLine(registrationName='tvh0.7', Input=calculatorTVH5,
    Source='Line')

# init the 'Line' selected for 'Source'
tvh07.Source.Point1 = [0., ymin, 0.7*zmax]
tvh07.Source.Point2 = [0., ymax, 0.7*zmax]

# create a new 'Temporal Statistics'
standdevstats = TemporalStatistics(registrationName='TemporalStatistics2', Input=uxdmf)
standdevstats.ComputeAverage = 0
standdevstats.ComputeMinimum = 0
standdevstats.ComputeMaximum = 0

# create a new 'Calculator'
calculatorTKE = Calculator(registrationName='Calculator2', Input=standdevstats)
calculatorTKE.ResultArrayName = 'tke'
calculatorTKE.Function = '0.5*(u_stddev_X^2+u_stddev_Y^2+u_stddev_Z^2)'

# create a new 'Plot Over Line'
tke0 = PlotOverLine(registrationName='PlotOverLine3', Input=calculatorTKE,
    Source='Line')

# init the 'Line' selected for 'Source'
tke0.Source.Point1 = [(xmax-xmin)/2, 0.*zmax, zmin]
tke0.Source.Point2 = [(xmax-xmin)/2, 0.*zmax, zmax]

# create a new 'Plot Over Line'
tke025 = PlotOverLine(registrationName='PlotOverLine1', Input=calculatorTKE,
    Source='Line')

# init the 'Line' selected for 'Source'
tke025.Source.Point1 = [(xmax-xmin)/2, 0.25*zmax, zmin]
tke025.Source.Point2 = [(xmax-xmin)/2, 0.25*zmax, zmax]

# create a new 'Plot Over Line'
tke05 = PlotOverLine(registrationName='PlotOverLine4', Input=calculatorTKE,
    Source='Line')

# init the 'Line' selected for 'Source'
tke05.Source.Point1 = [(xmax-xmin)/2, 0.5*zmax, zmin]
tke05.Source.Point2 = [(xmax-xmin)/2, 0.5*zmax, zmax]

# create a new 'Plot Over Line'
tke075 = PlotOverLine(registrationName='PlotOverLine2', Input=calculatorTKE,
    Source='Line')

# init the 'Line' selected for 'Source'
tke075.Source.Point1 = [(xmax-xmin)/2, 0.75*zmax, zmin]
tke075.Source.Point2 = [(xmax-xmin)/2, 0.75*zmax, zmax]


# create a new 'Calculator'
calcStreamwise = Calculator(registrationName='Calculator1', Input=uxdmf)
calcStreamwise.ResultArrayName = 'u_x'
calcStreamwise.Function = 'u_X'

# create a new 'Temporal Statistics'
meanvelstats = TemporalStatistics(registrationName='TemporalStatistics1', Input=calcStreamwise)
meanvelstats.ComputeMinimum = 0
meanvelstats.ComputeMaximum = 0
meanvelstats.ComputeStandardDeviation = 0

# create a new 'Plot Over Line'
mvh002 = PlotOverLine(registrationName='mvh0.02', Input=meanvelstats,
    Source='Line')

# init the 'Line' selected for 'Source'
mvh002.Source.Point1 = [(xmax-xmin)/2, ymin, 0.02*zmax]
mvh002.Source.Point2 = [(xmax-xmin)/2, ymax, 0.02*zmax]

# create a new 'Plot Over Line'
mvh005 = PlotOverLine(registrationName='mvh0.05', Input=meanvelstats,
    Source='Line')

# init the 'Line' selected for 'Source'
mvh005.Source.Point1 = [(xmax-xmin)/2, ymin, 0.05*zmax]
mvh005.Source.Point2 = [(xmax-xmin)/2, ymax, 0.05*zmax]

# create a new 'Plot Over Line'
mvh01 = PlotOverLine(registrationName='mvh0.1', Input=meanvelstats,
    Source='Line')

# init the 'Line' selected for 'Source'
mvh01.Source.Point1 = [(xmax-xmin)/2, ymin, 0.1*zmax]
mvh01.Source.Point2 = [(xmax-xmin)/2, ymax, 0.1*zmax]

# create a new 'Plot Over Line'
mvh03 = PlotOverLine(registrationName='mvh.0.3', Input=meanvelstats,
    Source='Line')

# init the 'Line' selected for 'Source'
mvh03.Source.Point1 = [(xmax-xmin)/2, ymin, 0.3*zmax]
mvh03.Source.Point2 = [(xmax-xmin)/2, ymax, 0.3*zmax]

# create a new 'Plot Over Line'
mvh07 = PlotOverLine(registrationName='mvh.0.7', Input=meanvelstats,
    Source='Line')

# init the 'Line' selected for 'Source'
mvh07.Source.Point1 = [(xmax-xmin)/2, ymin, 0.7*zmax]
mvh07.Source.Point2 = [(xmax-xmin)/2, ymax, 0.7*zmax]

# create a new 'Plot Over Line'
mvv0 = PlotOverLine(registrationName='mvv0', Input=meanvelstats,
    Source='Line')

# init the 'Line' selected for 'Source'
mvv0.Source.Point1 = [(xmax-xmin)/2, 0.0*zmax, zmin]
mvv0.Source.Point2 = [(xmax-xmin)/2, 0.0*zmax, zmax]

# create a new 'Plot Over Line'
mvv025 = PlotOverLine(registrationName='mvv0.25', Input=meanvelstats,
    Source='Line')

# init the 'Line' selected for 'Source'
mvv025.Source.Point1 = [(xmax-xmin)/2, 0.25*zmax, zmin]
mvv025.Source.Point2 = [(xmax-xmin)/2, 0.25*zmax, zmax]

# create a new 'Plot Over Line'
mvv05 = PlotOverLine(registrationName='mvv0.5', Input=meanvelstats,
    Source='Line')

# init the 'Line' selected for 'Source'
mvv05.Source.Point1 = [(xmax-xmin)/2, 0.5*zmax, zmin]
mvv05.Source.Point2 = [(xmax-xmin)/2, 0.5*zmax, zmax]

# create a new 'Plot Over Line'
mvv075 = PlotOverLine(registrationName='mvv0.75', Input=meanvelstats,
    Source='Line')

# init the 'Line' selected for 'Source'
mvv075.Source.Point1 = [(xmax-xmin)/2, 0.75*zmax, zmin]
mvv075.Source.Point2 = [(xmax-xmin)/2, 0.75*zmax, zmax]


# ----------------------------------------------------------------
# setup the visualization in view 'mvh'
# ----------------------------------------------------------------

# show data from mvh002
mvh002Display = Show(mvh002, mvh, 'XYChartRepresentation')

# trace defaults for the display properties.
mvh002Display.CompositeDataSetIndex = [0]
mvh002Display.UseIndexForXAxis = 0
mvh002Display.XArrayName = 'Points_Y'
mvh002Display.SeriesVisibility = ['u_x_average']
mvh002Display.SeriesLabel = ['arc_length', 'arc_length', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_x_average', 'z/H = 0.12', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
mvh002Display.SeriesColor = ['arc_length', '0', '0', '0', 'u_average_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_x_average', '0.6666666666666666', '0.3333333333333333', '1', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
mvh002Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvh002Display.SeriesLabelPrefix = ''
mvh002Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_x_average', '1', 'vtkValidPointMask', '1']
mvh002Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_x_average', '2', 'vtkValidPointMask', '2']
mvh002Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvh002Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_x_average', '4', 'vtkValidPointMask', '4']

# show data from mvh005
mvh005Display = Show(mvh005, mvh, 'XYChartRepresentation')

# trace defaults for the display properties.
mvh005Display.CompositeDataSetIndex = [0]
mvh005Display.UseIndexForXAxis = 0
mvh005Display.XArrayName = 'Points_Y'
mvh005Display.SeriesVisibility = ['u_x_average']
mvh005Display.SeriesLabel = ['arc_length', 'arc_length', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_x_average', 'z/H = 0.3', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
mvh005Display.SeriesColor = ['arc_length', '0', '0', '0', 'u_average_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_x_average', '0', '0.6666666666666666', '1', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
mvh005Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvh005Display.SeriesLabelPrefix = ''
mvh005Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_x_average', '1', 'vtkValidPointMask', '1']
mvh005Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_x_average', '2', 'vtkValidPointMask', '2']
mvh005Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvh005Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_x_average', '4', 'vtkValidPointMask', '4']

# show data from mvh01
mvh01Display = Show(mvh01, mvh, 'XYChartRepresentation')

# trace defaults for the display properties.
mvh01Display.CompositeDataSetIndex = [0]
mvh01Display.UseIndexForXAxis = 0
mvh01Display.XArrayName = 'Points_Y'
mvh01Display.SeriesVisibility = ['u_x_average']
mvh01Display.SeriesLabel = ['arc_length', 'arc_length', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_x_average', 'z/H = 0.6', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
mvh01Display.SeriesColor = ['arc_length', '0', '0', '0', 'u_average_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_x_average', '0.3333333333333333', '0.6666666666666666', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
mvh01Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvh01Display.SeriesLabelPrefix = ''
mvh01Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_x_average', '1', 'vtkValidPointMask', '1']
mvh01Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_x_average', '2', 'vtkValidPointMask', '2']
mvh01Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvh01Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_x_average', '4', 'vtkValidPointMask', '4']

# show data from mvh03
mvh03Display = Show(mvh03, mvh, 'XYChartRepresentation')

# trace defaults for the display properties.
mvh03Display.CompositeDataSetIndex = [0]
mvh03Display.UseIndexForXAxis = 0
mvh03Display.XArrayName = 'Points_Y'
mvh03Display.SeriesVisibility = ['u_x_average']
mvh03Display.SeriesLabel = ['arc_length', 'arc_length', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_x_average', 'z/H = 1.8', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
mvh03Display.SeriesColor = ['arc_length', '0', '0', '0', 'u_average_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_x_average', '1', '0.6666666666666666', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
mvh03Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvh03Display.SeriesLabelPrefix = ''
mvh03Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_x_average', '1', 'vtkValidPointMask', '1']
mvh03Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_x_average', '2', 'vtkValidPointMask', '2']
mvh03Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvh03Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_x_average', '4', 'vtkValidPointMask', '4']

# show data from mvh07
mvh07Display = Show(mvh07, mvh, 'XYChartRepresentation')

# trace defaults for the display properties.
mvh07Display.CompositeDataSetIndex = [0]
mvh07Display.UseIndexForXAxis = 0
mvh07Display.XArrayName = 'Points_Y'
mvh07Display.SeriesVisibility = ['u_x_average']
mvh07Display.SeriesLabel = ['arc_length', 'arc_length', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_x_average', 'z/H = 4.2', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
mvh07Display.SeriesColor = ['arc_length', '0', '0', '0', 'u_average_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_x_average', '1', '0.3333333333333333', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
mvh07Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvh07Display.SeriesLabelPrefix = ''
mvh07Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_x_average', '1', 'vtkValidPointMask', '1']
mvh07Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_x_average', '2', 'vtkValidPointMask', '2']
mvh07Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvh07Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_x_average', '4', 'vtkValidPointMask', '4']

# show data from tvh002
tvh002Display = Show(tvh002, mvh, 'XYChartRepresentation')

# trace defaults for the display properties.
tvh002Display.CompositeDataSetIndex = [0]
tvh002Display.UseIndexForXAxis = 0
tvh002Display.XArrayName = 'Points_Y'
tvh002Display.SeriesVisibility = ['target']
tvh002Display.SeriesLabel = ['arc_length', 'arc_length', 'target', '', 'Texture Coordinates_X', 'Texture Coordinates_X', 'Texture Coordinates_Y', 'Texture Coordinates_Y', 'Texture Coordinates_Magnitude', 'Texture Coordinates_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tvh002Display.SeriesColor = ['arc_length', '0', '0', '0', 'target', '0.6666666666666666', '0.3333333333333333', '1', 'Texture Coordinates_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Texture Coordinates_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Texture Coordinates_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
tvh002Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Texture Coordinates_Magnitude', '0', 'Texture Coordinates_X', '0', 'Texture Coordinates_Y', '0', 'arc_length', '0', 'target', '0', 'vtkValidPointMask', '0']
tvh002Display.SeriesLabelPrefix = ''
tvh002Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Texture Coordinates_Magnitude', '1', 'Texture Coordinates_X', '1', 'Texture Coordinates_Y', '1', 'arc_length', '1', 'target', '2', 'vtkValidPointMask', '1']
tvh002Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Texture Coordinates_Magnitude', '2', 'Texture Coordinates_X', '2', 'Texture Coordinates_Y', '2', 'arc_length', '2', 'target', '2', 'vtkValidPointMask', '2']
tvh002Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Texture Coordinates_Magnitude', '0', 'Texture Coordinates_X', '0', 'Texture Coordinates_Y', '0', 'arc_length', '0', 'target', '0', 'vtkValidPointMask', '0']
tvh002Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Texture Coordinates_Magnitude', '4', 'Texture Coordinates_X', '4', 'Texture Coordinates_Y', '4', 'arc_length', '4', 'target', '4', 'vtkValidPointMask', '4']

# show data from tvh005
tvh005Display = Show(tvh005, mvh, 'XYChartRepresentation')

# trace defaults for the display properties.
tvh005Display.CompositeDataSetIndex = [0]
tvh005Display.UseIndexForXAxis = 0
tvh005Display.XArrayName = 'Points_Y'
tvh005Display.SeriesVisibility = ['target']
tvh005Display.SeriesLabel = ['arc_length', 'arc_length', 'target', '', 'Texture Coordinates_X', 'Texture Coordinates_X', 'Texture Coordinates_Y', 'Texture Coordinates_Y', 'Texture Coordinates_Magnitude', 'Texture Coordinates_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tvh005Display.SeriesColor = ['arc_length', '0', '0', '0', 'target', '0', '0.6666666666666666', '1', 'Texture Coordinates_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Texture Coordinates_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Texture Coordinates_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
tvh005Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Texture Coordinates_Magnitude', '0', 'Texture Coordinates_X', '0', 'Texture Coordinates_Y', '0', 'arc_length', '0', 'target', '0', 'vtkValidPointMask', '0']
tvh005Display.SeriesLabelPrefix = ''
tvh005Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Texture Coordinates_Magnitude', '1', 'Texture Coordinates_X', '1', 'Texture Coordinates_Y', '1', 'arc_length', '1', 'target', '2', 'vtkValidPointMask', '1']
tvh005Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Texture Coordinates_Magnitude', '2', 'Texture Coordinates_X', '2', 'Texture Coordinates_Y', '2', 'arc_length', '2', 'target', '2', 'vtkValidPointMask', '2']
tvh005Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Texture Coordinates_Magnitude', '0', 'Texture Coordinates_X', '0', 'Texture Coordinates_Y', '0', 'arc_length', '0', 'target', '0', 'vtkValidPointMask', '0']
tvh005Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Texture Coordinates_Magnitude', '4', 'Texture Coordinates_X', '4', 'Texture Coordinates_Y', '4', 'arc_length', '4', 'target', '4', 'vtkValidPointMask', '4']

# show data from tvh01
tvh01Display = Show(tvh01, mvh, 'XYChartRepresentation')

# trace defaults for the display properties.
tvh01Display.CompositeDataSetIndex = [0]
tvh01Display.UseIndexForXAxis = 0
tvh01Display.XArrayName = 'Points_Y'
tvh01Display.SeriesVisibility = ['target']
tvh01Display.SeriesLabel = ['arc_length', 'arc_length', 'target', '', 'Texture Coordinates_X', 'Texture Coordinates_X', 'Texture Coordinates_Y', 'Texture Coordinates_Y', 'Texture Coordinates_Magnitude', 'Texture Coordinates_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tvh01Display.SeriesColor = ['arc_length', '0', '0', '0', 'target', '0.3333333333333333', '0.6666666666666666', '0', 'Texture Coordinates_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Texture Coordinates_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Texture Coordinates_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
tvh01Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Texture Coordinates_Magnitude', '0', 'Texture Coordinates_X', '0', 'Texture Coordinates_Y', '0', 'arc_length', '0', 'target', '0', 'vtkValidPointMask', '0']
tvh01Display.SeriesLabelPrefix = ''
tvh01Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Texture Coordinates_Magnitude', '1', 'Texture Coordinates_X', '1', 'Texture Coordinates_Y', '1', 'arc_length', '1', 'target', '2', 'vtkValidPointMask', '1']
tvh01Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Texture Coordinates_Magnitude', '2', 'Texture Coordinates_X', '2', 'Texture Coordinates_Y', '2', 'arc_length', '2', 'target', '2', 'vtkValidPointMask', '2']
tvh01Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Texture Coordinates_Magnitude', '0', 'Texture Coordinates_X', '0', 'Texture Coordinates_Y', '0', 'arc_length', '0', 'target', '0', 'vtkValidPointMask', '0']
tvh01Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Texture Coordinates_Magnitude', '4', 'Texture Coordinates_X', '4', 'Texture Coordinates_Y', '4', 'arc_length', '4', 'target', '4', 'vtkValidPointMask', '4']

# show data from tvh03
tvh03Display = Show(tvh03, mvh, 'XYChartRepresentation')

# trace defaults for the display properties.
tvh03Display.CompositeDataSetIndex = [0]
tvh03Display.UseIndexForXAxis = 0
tvh03Display.XArrayName = 'Points_Y'
tvh03Display.SeriesVisibility = ['target']
tvh03Display.SeriesLabel = ['arc_length', 'arc_length', 'target', '', 'Texture Coordinates_X', 'Texture Coordinates_X', 'Texture Coordinates_Y', 'Texture Coordinates_Y', 'Texture Coordinates_Magnitude', 'Texture Coordinates_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tvh03Display.SeriesColor = ['arc_length', '0', '0', '0', 'target', '1', '0.6666666666666666', '0', 'Texture Coordinates_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Texture Coordinates_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Texture Coordinates_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
tvh03Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Texture Coordinates_Magnitude', '0', 'Texture Coordinates_X', '0', 'Texture Coordinates_Y', '0', 'arc_length', '0', 'target', '0', 'vtkValidPointMask', '0']
tvh03Display.SeriesLabelPrefix = ''
tvh03Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Texture Coordinates_Magnitude', '1', 'Texture Coordinates_X', '1', 'Texture Coordinates_Y', '1', 'arc_length', '1', 'target', '2', 'vtkValidPointMask', '1']
tvh03Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Texture Coordinates_Magnitude', '2', 'Texture Coordinates_X', '2', 'Texture Coordinates_Y', '2', 'arc_length', '2', 'target', '2', 'vtkValidPointMask', '2']
tvh03Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Texture Coordinates_Magnitude', '0', 'Texture Coordinates_X', '0', 'Texture Coordinates_Y', '0', 'arc_length', '0', 'target', '0', 'vtkValidPointMask', '0']
tvh03Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Texture Coordinates_Magnitude', '4', 'Texture Coordinates_X', '4', 'Texture Coordinates_Y', '4', 'arc_length', '4', 'target', '4', 'vtkValidPointMask', '4']

# show data from tvh07
tvh07Display = Show(tvh07, mvh, 'XYChartRepresentation')

# trace defaults for the display properties.
tvh07Display.CompositeDataSetIndex = [0]
tvh07Display.UseIndexForXAxis = 0
tvh07Display.XArrayName = 'Points_Y'
tvh07Display.SeriesVisibility = ['target']
tvh07Display.SeriesLabel = ['arc_length', 'arc_length', 'target', '', 'Texture Coordinates_X', 'Texture Coordinates_X', 'Texture Coordinates_Y', 'Texture Coordinates_Y', 'Texture Coordinates_Magnitude', 'Texture Coordinates_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tvh07Display.SeriesColor = ['arc_length', '0', '0', '0', 'target', '1', '0.3333333333333333', '0', 'Texture Coordinates_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Texture Coordinates_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Texture Coordinates_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
tvh07Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Texture Coordinates_Magnitude', '0', 'Texture Coordinates_X', '0', 'Texture Coordinates_Y', '0', 'arc_length', '0', 'target', '0', 'vtkValidPointMask', '0']
tvh07Display.SeriesLabelPrefix = ''
tvh07Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Texture Coordinates_Magnitude', '1', 'Texture Coordinates_X', '1', 'Texture Coordinates_Y', '1', 'arc_length', '1', 'target', '2', 'vtkValidPointMask', '1']
tvh07Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Texture Coordinates_Magnitude', '2', 'Texture Coordinates_X', '2', 'Texture Coordinates_Y', '2', 'arc_length', '2', 'target', '2', 'vtkValidPointMask', '2']
tvh07Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Texture Coordinates_Magnitude', '0', 'Texture Coordinates_X', '0', 'Texture Coordinates_Y', '0', 'arc_length', '0', 'target', '0', 'vtkValidPointMask', '0']
tvh07Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Texture Coordinates_Magnitude', '4', 'Texture Coordinates_X', '4', 'Texture Coordinates_Y', '4', 'arc_length', '4', 'target', '4', 'vtkValidPointMask', '4']

# ----------------------------------------------------------------
# setup the visualization in view 'mvv'
# ----------------------------------------------------------------

# show data from mvv0
mvv0Display = Show(mvv0, mvv, 'XYChartRepresentation')

# trace defaults for the display properties.
mvv0Display.CompositeDataSetIndex = [0]
mvv0Display.UseIndexForXAxis = 0
mvv0Display.XArrayName = 'u_x_average'
mvv0Display.SeriesVisibility = ['arc_length']
mvv0Display.SeriesLabel = ['arc_length', 'y/H = 0', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_x_average', 'u_x_average', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
mvv0Display.SeriesColor = ['arc_length', '0', '0.6666666666666666', '1', 'u_average_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_x_average', '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
mvv0Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvv0Display.SeriesLabelPrefix = ''
mvv0Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_x_average', '1', 'vtkValidPointMask', '1']
mvv0Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_x_average', '2', 'vtkValidPointMask', '2']
mvv0Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvv0Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_x_average', '4', 'vtkValidPointMask', '4']

# show data from mvv025
mvv025Display = Show(mvv025, mvv, 'XYChartRepresentation')

# trace defaults for the display properties.
mvv025Display.CompositeDataSetIndex = [0]
mvv025Display.UseIndexForXAxis = 0
mvv025Display.XArrayName = 'u_x_average'
mvv025Display.SeriesVisibility = ['arc_length']
mvv025Display.SeriesLabel = ['arc_length', 'y/H = 1.5', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_x_average', 'u_x_average', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
mvv025Display.SeriesColor = ['arc_length', '1', '0.6666666666666666', '0', 'u_average_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_x_average', '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
mvv025Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvv025Display.SeriesLabelPrefix = ''
mvv025Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_x_average', '1', 'vtkValidPointMask', '1']
mvv025Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_x_average', '2', 'vtkValidPointMask', '2']
mvv025Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvv025Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_x_average', '4', 'vtkValidPointMask', '4']

# show data from mvv05
mvv05Display = Show(mvv05, mvv, 'XYChartRepresentation')

# trace defaults for the display properties.
mvv05Display.CompositeDataSetIndex = [0]
mvv05Display.UseIndexForXAxis = 0
mvv05Display.XArrayName = 'u_x_average'
mvv05Display.SeriesVisibility = ['arc_length']
mvv05Display.SeriesLabel = ['arc_length', 'y/H = 3', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_x_average', 'u_x_average', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
mvv05Display.SeriesColor = ['arc_length', '0.6666666666666666', '0.3333333333333333', '1', 'u_average_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_x_average', '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
mvv05Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvv05Display.SeriesLabelPrefix = ''
mvv05Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_x_average', '1', 'vtkValidPointMask', '1']
mvv05Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_x_average', '2', 'vtkValidPointMask', '2']
mvv05Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvv05Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_x_average', '4', 'vtkValidPointMask', '4']

# show data from mvv075
mvv075Display = Show(mvv075, mvv, 'XYChartRepresentation')

# trace defaults for the display properties.
mvv075Display.CompositeDataSetIndex = [0]
mvv075Display.UseIndexForXAxis = 0
mvv075Display.XArrayName = 'u_x_average'
mvv075Display.SeriesVisibility = ['arc_length']
mvv075Display.SeriesLabel = ['arc_length', 'y/H = 4.5', 'u_average_X', 'u_average_X', 'u_average_Y', 'u_average_Y', 'u_average_Z', 'u_average_Z', 'u_average_Magnitude', 'u_average_Magnitude', 'u_x_average', 'u_x_average', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
mvv075Display.SeriesColor = ['arc_length', '0.3333333333333333', '0.6666666666666666', '0', 'u_average_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_average_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_average_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_average_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_x_average', '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
mvv075Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvv075Display.SeriesLabelPrefix = ''
mvv075Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'u_average_Magnitude', '1', 'u_average_X', '1', 'u_average_Y', '1', 'u_average_Z', '1', 'u_x_average', '1', 'vtkValidPointMask', '1']
mvv075Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'u_average_Magnitude', '2', 'u_average_X', '2', 'u_average_Y', '2', 'u_average_Z', '2', 'u_x_average', '2', 'vtkValidPointMask', '2']
mvv075Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'u_average_Magnitude', '0', 'u_average_X', '0', 'u_average_Y', '0', 'u_average_Z', '0', 'u_x_average', '0', 'vtkValidPointMask', '0']
mvv075Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'u_average_Magnitude', '4', 'u_average_X', '4', 'u_average_Y', '4', 'u_average_Z', '4', 'u_x_average', '4', 'vtkValidPointMask', '4']

# show data from tvv
tvvDisplay = Show(tvv, mvv, 'XYChartRepresentation')

# trace defaults for the display properties.
tvvDisplay.CompositeDataSetIndex = [0]
tvvDisplay.UseIndexForXAxis = 0
tvvDisplay.XArrayName = 't'
tvvDisplay.SeriesVisibility = ['arc_length']
tvvDisplay.SeriesLabel = ['arc_length', 'target', 't', 't', 'Texture Coordinates_X', 'Texture Coordinates_X', 'Texture Coordinates_Y', 'Texture Coordinates_Y', 'Texture Coordinates_Magnitude', 'Texture Coordinates_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tvvDisplay.SeriesColor = ['arc_length', '0', '0', '0', 't', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Texture Coordinates_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Texture Coordinates_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Texture Coordinates_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', 'vtkValidPointMask', '1', '0.5000076295109483', '0', 'Points_X', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Y', '0', '0', '0', 'Points_Z', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Magnitude', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
tvvDisplay.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Texture Coordinates_Magnitude', '0', 'Texture Coordinates_X', '0', 'Texture Coordinates_Y', '0', 'arc_length', '0', 't', '0', 'vtkValidPointMask', '0']
tvvDisplay.SeriesLabelPrefix = ''
tvvDisplay.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Texture Coordinates_Magnitude', '1', 'Texture Coordinates_X', '1', 'Texture Coordinates_Y', '1', 'arc_length', '1', 't', '1', 'vtkValidPointMask', '1']
tvvDisplay.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Texture Coordinates_Magnitude', '2', 'Texture Coordinates_X', '2', 'Texture Coordinates_Y', '2', 'arc_length', '2', 't', '2', 'vtkValidPointMask', '2']
tvvDisplay.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Texture Coordinates_Magnitude', '0', 'Texture Coordinates_X', '0', 'Texture Coordinates_Y', '0', 'arc_length', '0', 't', '0', 'vtkValidPointMask', '0']
tvvDisplay.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Texture Coordinates_Magnitude', '4', 'Texture Coordinates_X', '4', 'Texture Coordinates_Y', '4', 'arc_length', '4', 't', '4', 'vtkValidPointMask', '4']

# ----------------------------------------------------------------
# setup the visualization in view 'tke'
# ----------------------------------------------------------------

# show data from tke0
tke0Display = Show(tke0, tke, 'XYChartRepresentation')

# trace defaults for the display properties.
tke0Display.CompositeDataSetIndex = [0]
tke0Display.UseIndexForXAxis = 0
tke0Display.XArrayName = 'tke'
tke0Display.SeriesVisibility = ['arc_length']
tke0Display.SeriesLabel = ['arc_length', 'y/H = 0', 'tke', 'tke', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tke0Display.SeriesColor = ['arc_length', '0', '0.6666666666666666', '1', 'tke', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_stddev_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_stddev_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_stddev_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_stddev_Magnitude', '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
tke0Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'tke', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tke0Display.SeriesLabelPrefix = ''
tke0Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'tke', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
tke0Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'tke', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
tke0Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'tke', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tke0Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'tke', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# show data from tke025
tke025Display = Show(tke025, tke, 'XYChartRepresentation')

# trace defaults for the display properties.
tke025Display.CompositeDataSetIndex = [0]
tke025Display.UseIndexForXAxis = 0
tke025Display.XArrayName = 'tke'
tke025Display.SeriesVisibility = ['arc_length']
tke025Display.SeriesLabel = ['arc_length', 'y/H = 1.5', 'tke', 'tke', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tke025Display.SeriesColor = ['arc_length', '1', '0.6666666666666666', '0', 'tke', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_stddev_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_stddev_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_stddev_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_stddev_Magnitude', '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
tke025Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'tke', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tke025Display.SeriesLabelPrefix = ''
tke025Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'tke', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
tke025Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'tke', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
tke025Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'tke', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tke025Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'tke', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# show data from tke05
tke05Display = Show(tke05, tke, 'XYChartRepresentation')

# trace defaults for the display properties.
tke05Display.CompositeDataSetIndex = [0]
tke05Display.UseIndexForXAxis = 0
tke05Display.XArrayName = 'tke'
tke05Display.SeriesVisibility = ['arc_length']
tke05Display.SeriesLabel = ['arc_length', 'y/H = 3', 'tke', 'tke', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tke05Display.SeriesColor = ['arc_length', '0.3333333333333333', '0', '0.4980392156862745', 'tke', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_stddev_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_stddev_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_stddev_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_stddev_Magnitude', '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
tke05Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'tke', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tke05Display.SeriesLabelPrefix = ''
tke05Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'tke', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
tke05Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'tke', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
tke05Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'tke', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tke05Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'tke', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']
# show data from tke075
tke075Display = Show(tke075, tke, 'XYChartRepresentation')

# trace defaults for the display properties.
tke075Display.CompositeDataSetIndex = [0]
tke075Display.UseIndexForXAxis = 0
tke075Display.XArrayName = 'tke'
tke075Display.SeriesVisibility = ['arc_length']
tke075Display.SeriesLabel = ['arc_length', 'y/H = 4.5', 'tke', 'tke', 'u_stddev_X', 'u_stddev_X', 'u_stddev_Y', 'u_stddev_Y', 'u_stddev_Z', 'u_stddev_Z', 'u_stddev_Magnitude', 'u_stddev_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
tke075Display.SeriesColor = ['arc_length', '0.3333333333333333', '0.6666666666666666', '0', 'tke', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u_stddev_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u_stddev_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u_stddev_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'u_stddev_Magnitude', '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
tke075Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'tke', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tke075Display.SeriesLabelPrefix = ''
tke075Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'tke', '1', 'u_stddev_Magnitude', '1', 'u_stddev_X', '1', 'u_stddev_Y', '1', 'u_stddev_Z', '1', 'vtkValidPointMask', '1']
tke075Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'tke', '2', 'u_stddev_Magnitude', '2', 'u_stddev_X', '2', 'u_stddev_Y', '2', 'u_stddev_Z', '2', 'vtkValidPointMask', '2']
tke075Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'tke', '0', 'u_stddev_Magnitude', '0', 'u_stddev_X', '0', 'u_stddev_Y', '0', 'u_stddev_Z', '0', 'vtkValidPointMask', '0']
tke075Display.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'tke', '4', 'u_stddev_Magnitude', '4', 'u_stddev_X', '4', 'u_stddev_Y', '4', 'u_stddev_Z', '4', 'vtkValidPointMask', '4']

# ----------------------------------------------------------------
# restore active source
SetActiveSource(uxdmf)
# ----------------------------------------------------------------

import os.path
from os import path

print("Writing")
# Get the layout/tab for the active view.
aLayout = GetLayout()
SaveScreenshot("./images/graphs.png", layout=aLayout)
print("Exiting")
exit()
print("Exiting - shouldnt be here")

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='./output')
