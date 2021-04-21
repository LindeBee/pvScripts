# state file generated using paraview version 5.8.1-1634-g6bacce2f26

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Box Chart View'
boxChartView1 = CreateView('BoxChartView')
boxChartView1.ViewSize = [306, 532]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [1988, 350]
lineChartView1.LegendPosition = [1842, 33]

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
lineChartView2.ViewSize = [1988, 250]
lineChartView2.ShowLegend = 0
lineChartView2.LegendPosition = [1880, 173]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1662, 532]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [10.0, 0.0, 6.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-3.969623302439624, -3.520366066724904, 1.7659974869258992]
renderView1.CameraFocalPoint = [11.455785523886236, 8.644365015643286, -2.056574169094034]
renderView1.CameraViewUp = [0.15123571982314135, 0.11667476824609015, 0.9815878745707372]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 23.80126047082381
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.469965)
layout1.SplitHorizontal(1, 0.840000)
layout1.AssignView(3, renderView1)
layout1.AssignView(4, boxChartView1)
layout1.SplitVertical(2, 0.583333)
layout1.AssignView(5, lineChartView1)
layout1.AssignView(6, lineChartView2)
layout1.SetSize(1988, 1134)

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

# create a new 'Calculator'
rescaleResults = Calculator(registrationName='RescaleResults', Input=uxdmf)
rescaleResults.CoordinateResults = 1
rescaleResults.Function = 'iHat*(coordsX/2) +jHat*(coordsY/2) +kHat*(coordsZ/2)'

writer = CreateWriter("./dataset.csv")
writer.FieldAssociation = "Point Data"
writer.UpdatePipeline()


# create a new 'CSV Reader'
caseH_ucsv = CSVReader(registrationName='CaseH_u.csv', FileName=['./pvScripts/CaseH_u.csv'])

# create a new 'Table To Points'
valiToPoints = TableToPoints(registrationName='ValiToPoints', Input=caseH_ucsv)
valiToPoints.XColumn = 'x/H'
valiToPoints.YColumn = 'y/H'
valiToPoints.ZColumn = 'z/H'

# create a new 'Calculator'
makeUVector = Calculator(registrationName='MakeUVector', Input=valiToPoints)
makeUVector.ResultArrayName = '<U/uH>'
makeUVector.Function = 'iHat*<u/uH>+jHat*<v/uH>+kHat*<w/uH>'

# create a new 'Calculator'
translatePoints = Calculator(registrationName='TranslatePoints', Input=makeUVector)
translatePoints.CoordinateResults = 1
translatePoints.Function = 'coords+iHat*0.25'

# create a new 'CSV Reader'
datasetcsv = CSVReader(registrationName='dataset.csv', FileName=['./dataset.csv'])

# create a new 'Table To Points'
resToPoints = TableToPoints(registrationName='ResToPoints', Input=datasetcsv)
resToPoints.XColumn = 'Points:0'
resToPoints.YColumn = 'Points:1'
resToPoints.ZColumn = 'Points:2'

# create a new 'Temporal Statistics'
temporalStatistics1 = TemporalStatistics(registrationName='TemporalStatistics1', Input=resToPoints)
temporalStatistics1.ComputeMinimum = 0
temporalStatistics1.ComputeMaximum = 0

# create a new 'Calculator'
calculator_TKE = Calculator(registrationName='Calculator_TKE', Input=temporalStatistics1)
calculator_TKE.ResultArrayName = 'k'
calculator_TKE.Function = 'sqrt(u:0_stddev^2+u:1_stddev^2+u:2_stddev^2)'

# create a new 'Point Dataset Interpolator'
pointDatasetInterpolator1 = PointDatasetInterpolator(registrationName='PointDatasetInterpolator1', Input=calculator_TKE,
    Source=translatePoints)
pointDatasetInterpolator1.Kernel = 'LinearKernel'
pointDatasetInterpolator1.Locator = 'Static Point Locator'

# init the 'LinearKernel' selected for 'Kernel'
pointDatasetInterpolator1.Kernel.KernelFootprint = 'N Closest'
pointDatasetInterpolator1.Kernel.NumberOfPoints = 3

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[pointDatasetInterpolator1, translatePoints])

# create a new 'Calculator'
umagCalculator = Calculator(registrationName='UmagCalculator', Input=appendAttributes1)
umagCalculator.ResultArrayName = 'U'
umagCalculator.Function = 'iHat*u:0_average + jHat*u:1_average + kHat*u:2_average'

# create a new 'Calculator'
umagErrorCalculator = Calculator(registrationName='UmagErrorCalculator', Input=umagCalculator)
umagErrorCalculator.ResultArrayName = 'error'
umagErrorCalculator.Function = 'abs(mag(<U/uH>)-mag(U))/mag(<U/uH>)'

# create a new 'Compute Quartiles'
computeQuartiles1 = ComputeQuartiles(registrationName='ComputeQuartiles1', Input=umagErrorCalculator)

# create a new 'Mask Points'
maskPoints1 = MaskPoints(registrationName='MaskPoints1', Input=umagErrorCalculator)
maskPoints1.OnRatio = 1

# create a new 'Plot Data'
plotData1 = PlotData(registrationName='PlotData1', Input=maskPoints1)

# create a new 'Plot Data'
plotData2 = PlotData(registrationName='PlotData2', Input=maskPoints1)

# ----------------------------------------------------------------
# setup the visualization in view 'boxChartView1'
# ----------------------------------------------------------------

# show data from computeQuartiles1
computeQuartiles1Display = Show(computeQuartiles1, boxChartView1, 'BoxChartRepresentation')

# trace defaults for the display properties.
computeQuartiles1Display.CompositeDataSetIndex = 0
computeQuartiles1Display.FieldAssociation = 'Row Data'
computeQuartiles1Display.SeriesVisibility = ['error']
computeQuartiles1Display.SeriesColor = ['<k/uH2>', '0', '0', '0', '<u/uH>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', '<uref-u>', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', '<uref-v>', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', '<urms/uH>', '0.6', '0.3100022888532845', '0.6399938963912413', '<v/uH>', '1', '0.5000076295109483', '0', '<vrms/uH>', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', '<w/uH>', '0', '0', '0', '<wrms/uH>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'error', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'k', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u:0_average', '0.6', '0.3100022888532845', '0.6399938963912413', 'u:0_stddev', '1', '0.5000076295109483', '0', 'u:1_average', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u:1_stddev', '0', '0', '0', 'u:2_average', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u:2_stddev', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'x(mm)', '0.6', '0.3100022888532845', '0.6399938963912413', 'y(mm)', '1', '0.5000076295109483', '0', 'z(mm)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867']

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView1'
# ----------------------------------------------------------------

# show data from plotData1
plotData1Display = Show(plotData1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotData1Display.CompositeDataSetIndex = [0]
plotData1Display.XArrayName = '<k/uH2>'
plotData1Display.SeriesVisibility = ['<u/uH>', '<v/uH>', '<w/uH>', 'u:0_average', 'u:1_average', 'u:2_average']
plotData1Display.SeriesLabel = ['<k/uH2>', '<k/uH2>', '<U/uH>_X', '<U/uH>_X', '<U/uH>_Y', '<U/uH>_Y', '<U/uH>_Z', '<U/uH>_Z', '<U/uH>_Magnitude', '<U/uH>_Magnitude', '<u/uH>', '<u/uH>', '<uref-u>', '<uref-u>', '<uref-v>', '<uref-v>', '<uref-w>', '<uref-w>', '<urms/uH>', '<urms/uH>', '<v/uH>', '<v/uH>', '<vrms/uH>', '<vrms/uH>', '<w/uH>', '<w/uH>', '<wrms/uH>', '<wrms/uH>', 'k', 'k', 'u:0_average', '<u/uH>', 'u:0_stddev', 'u:0_stddev', 'u:1_average', '<v/uH>', 'u:1_stddev', '', 'u:2_average', '<w/uH>', 'u:2_stddev', '', 'U', 'U', 'y(mm)', 'y(mm)', 'z(mm)', 'z(mm)', 'x(mm)', 'x(mm)', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude', 'error', 'error', 'x(mm)', 'x(mm)']
plotData1Display.SeriesColor = ['<k/uH2>', '0', '0', '0', '<U/uH>_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', '<U/uH>_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', '<U/uH>_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', '<U/uH>_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', '<u/uH>', '1', '0', '0', '<uref-u>', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', '<uref-v>', '0', '0', '0', '<uref-w>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', '<urms/uH>', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', '<v/uH>', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', '<vrms/uH>', '0.6', '0.3100022888532845', '0.6399938963912413', '<w/uH>', '0', '0.3333333333333333', '1', '<wrms/uH>', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'k', '0', '0', '0', 'u:0_average', '1', '0.6078431372549019', '0.6078431372549019', 'u:0_stddev', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u:1_average', '0.6196078431372549', '0.803921568627451', '0.615686274509804', 'u:1_stddev', '0.6', '0.3100022888532845', '0.6399938963912413', 'u:2_average', '0.6078431372549019', '0.7372549019607844', '1', 'u:2_stddev', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U', '0', '0', '0', 'y(mm)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'z(mm)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'x(mm)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_X', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_Y', '1', '0.5000076295109483', '0', 'Points_Z', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Magnitude', '0', '0', '0', 'error', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'x(mm)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
plotData1Display.SeriesPlotCorner = ['<U/uH>_Magnitude', '0', '<U/uH>_X', '0', '<U/uH>_Y', '0', '<U/uH>_Z', '0', '<k/uH2>', '0', '<u/uH>', '0', '<uref-u>', '0', '<uref-v>', '0', '<uref-w>', '0', '<urms/uH>', '0', '<v/uH>', '0', '<vrms/uH>', '0', '<w/uH>', '0', '<wrms/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'error', '0', 'k', '0', 'u:0_average', '0', 'u:0_stddev', '0', 'u:1_average', '0', 'u:1_stddev', '0', 'u:2_average', '0', 'u:2_stddev', '0', 'U', '0', 'x(mm)', '0', 'y(mm)', '0', 'z(mm)', '0']
plotData1Display.SeriesLabelPrefix = ''
plotData1Display.SeriesLineStyle = ['<U/uH>_Magnitude', '1', '<U/uH>_X', '1', '<U/uH>_Y', '1', '<U/uH>_Z', '1', '<k/uH2>', '1', '<u/uH>', '0', '<uref-u>', '1', '<uref-v>', '1', '<uref-w>', '1', '<urms/uH>', '1', '<v/uH>', '0', '<vrms/uH>', '1', '<w/uH>', '0', '<wrms/uH>', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'error', '1', 'k', '1', 'u:0_average', '1', 'u:0_stddev', '1', 'u:1_average', '1', 'u:1_stddev', '1', 'u:2_average', '1', 'u:2_stddev', '1', 'U', '1', 'x(mm)', '1', 'y(mm)', '1', 'z(mm)', '1']
plotData1Display.SeriesLineThickness = ['<U/uH>_Magnitude', '2', '<U/uH>_X', '2', '<U/uH>_Y', '2', '<U/uH>_Z', '2', '<k/uH2>', '2', '<u/uH>', '2', '<uref-u>', '2', '<uref-v>', '2', '<uref-w>', '2', '<urms/uH>', '2', '<v/uH>', '2', '<vrms/uH>', '2', '<w/uH>', '2', '<wrms/uH>', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'error', '2', 'k', '2', 'u:0_average', '2', 'u:0_stddev', '2', 'u:1_average', '2', 'u:1_stddev', '2', 'u:2_average', '2', 'u:2_stddev', '2', 'U', '2', 'x(mm)', '2', 'y(mm)', '2', 'z(mm)', '2']
plotData1Display.SeriesMarkerStyle = ['<U/uH>_Magnitude', '0', '<U/uH>_X', '0', '<U/uH>_Y', '0', '<U/uH>_Z', '0', '<k/uH2>', '0', '<u/uH>', '4', '<uref-u>', '0', '<uref-v>', '0', '<uref-w>', '0', '<urms/uH>', '0', '<v/uH>', '1', '<vrms/uH>', '0', '<w/uH>', '2', '<wrms/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'error', '0', 'k', '0', 'u:0_average', '0', 'u:0_stddev', '0', 'u:1_average', '0', 'u:1_stddev', '0', 'u:2_average', '0', 'u:2_stddev', '0', 'U', '0', 'x(mm)', '0', 'y(mm)', '0', 'z(mm)', '0']
plotData1Display.SeriesMarkerSize = ['<U/uH>_Magnitude', '4', '<U/uH>_X', '4', '<U/uH>_Y', '4', '<U/uH>_Z', '4', '<k/uH2>', '4', '<u/uH>', '4', '<uref-u>', '4', '<uref-v>', '4', '<uref-w>', '4', '<urms/uH>', '4', '<v/uH>', '4', '<vrms/uH>', '4', '<w/uH>', '4', '<wrms/uH>', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'error', '4', 'k', '4', 'u:0_average', '4', 'u:0_stddev', '4', 'u:1_average', '4', 'u:1_stddev', '4', 'u:2_average', '4', 'u:2_stddev', '4', 'U', '4', 'x(mm)', '4', 'y(mm)', '4', 'z(mm)', '4']

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView2'
# ----------------------------------------------------------------

# show data from plotData2
plotData2Display = Show(plotData2, lineChartView2, 'XYChartRepresentation')

# trace defaults for the display properties.
plotData2Display.CompositeDataSetIndex = [0]
plotData2Display.XArrayName = '<k/uH2>'
plotData2Display.SeriesVisibility = ['error']
plotData2Display.SeriesLabel = ['<k/uH2>', '<k/uH2>', '<U/uH>_X', '<U/uH>_X', '<U/uH>_Y', '<U/uH>_Y', '<U/uH>_Z', '<U/uH>_Z', '<U/uH>_Magnitude', '<U/uH>_Magnitude', '<u/uH>', '<u/uH>', '<uref-u>', '<uref-u>', '<uref-v>', '<uref-v>', '<uref-w>', '<uref-w>', '<urms/uH>', '<urms/uH>', '<v/uH>', '<v/uH>', '<vrms/uH>', '<vrms/uH>', '<w/uH>', '<w/uH>', '<wrms/uH>', '<wrms/uH>', 'error', 'error', 'k', 'k', 'u:0_average', 'u:0_average', 'u:0_stddev', 'u:0_stddev', 'u:1_average', 'u:1_average', 'u:1_stddev', 'u:1_stddev', 'u:2_average', 'u:2_average', 'u:2_stddev', 'u:2_stddev', 'U', 'U', 'y(mm)', 'y(mm)', 'z(mm)', 'z(mm)', 'x(mm)', 'x(mm)', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotData2Display.SeriesColor = ['<k/uH2>', '0', '0', '0', '<U/uH>_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', '<U/uH>_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', '<U/uH>_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', '<U/uH>_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413', '<u/uH>', '1', '0.5000076295109483', '0', '<uref-u>', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', '<uref-v>', '0', '0', '0', '<uref-w>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', '<urms/uH>', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', '<v/uH>', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', '<vrms/uH>', '0.6', '0.3100022888532845', '0.6399938963912413', '<w/uH>', '1', '0.5000076295109483', '0', '<wrms/uH>', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'error', '0.3333333333333333', '0.3333333333333333', '1', 'k', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u:0_average', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u:0_stddev', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u:1_average', '0.6', '0.3100022888532845', '0.6399938963912413', 'u:1_stddev', '1', '0.5000076295109483', '0', 'u:2_average', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u:2_stddev', '0', '0', '0', 'U', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'y(mm)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'z(mm)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'x(mm)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Points_X', '1', '0.5000076295109483', '0', 'Points_Y', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotData2Display.SeriesPlotCorner = ['<U/uH>_Magnitude', '0', '<U/uH>_X', '0', '<U/uH>_Y', '0', '<U/uH>_Z', '0', '<k/uH2>', '0', '<u/uH>', '0', '<uref-u>', '0', '<uref-v>', '0', '<uref-w>', '0', '<urms/uH>', '0', '<v/uH>', '0', '<vrms/uH>', '0', '<w/uH>', '0', '<wrms/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'error', '0', 'k', '0', 'u:0_average', '0', 'u:0_stddev', '0', 'u:1_average', '0', 'u:1_stddev', '0', 'u:2_average', '0', 'u:2_stddev', '0', 'U', '0', 'x(mm)', '0', 'y(mm)', '0', 'z(mm)', '0']
plotData2Display.SeriesLabelPrefix = ''
plotData2Display.SeriesLineStyle = ['<U/uH>_Magnitude', '1', '<U/uH>_X', '1', '<U/uH>_Y', '1', '<U/uH>_Z', '1', '<k/uH2>', '1', '<u/uH>', '1', '<uref-u>', '1', '<uref-v>', '1', '<uref-w>', '1', '<urms/uH>', '1', '<v/uH>', '1', '<vrms/uH>', '1', '<w/uH>', '1', '<wrms/uH>', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'error', '0', 'k', '1', 'u:0_average', '1', 'u:0_stddev', '1', 'u:1_average', '1', 'u:1_stddev', '1', 'u:2_average', '1', 'u:2_stddev', '1', 'U', '1', 'x(mm)', '1', 'y(mm)', '1', 'z(mm)', '1']
plotData2Display.SeriesLineThickness = ['<U/uH>_Magnitude', '2', '<U/uH>_X', '2', '<U/uH>_Y', '2', '<U/uH>_Z', '2', '<k/uH2>', '2', '<u/uH>', '2', '<uref-u>', '2', '<uref-v>', '2', '<uref-w>', '2', '<urms/uH>', '2', '<v/uH>', '2', '<vrms/uH>', '2', '<w/uH>', '2', '<wrms/uH>', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'error', '2', 'k', '2', 'u:0_average', '2', 'u:0_stddev', '2', 'u:1_average', '2', 'u:1_stddev', '2', 'u:2_average', '2', 'u:2_stddev', '2', 'U', '2', 'x(mm)', '2', 'y(mm)', '2', 'z(mm)', '2']
plotData2Display.SeriesMarkerStyle = ['<U/uH>_Magnitude', '0', '<U/uH>_X', '0', '<U/uH>_Y', '0', '<U/uH>_Z', '0', '<k/uH2>', '0', '<u/uH>', '0', '<uref-u>', '0', '<uref-v>', '0', '<uref-w>', '0', '<urms/uH>', '0', '<v/uH>', '0', '<vrms/uH>', '0', '<w/uH>', '0', '<wrms/uH>', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'error', '1', 'k', '0', 'u:0_average', '0', 'u:0_stddev', '0', 'u:1_average', '0', 'u:1_stddev', '0', 'u:2_average', '0', 'u:2_stddev', '0', 'U', '0', 'x(mm)', '0', 'y(mm)', '0', 'z(mm)', '0']
plotData2Display.SeriesMarkerSize = ['<U/uH>_Magnitude', '4', '<U/uH>_X', '4', '<U/uH>_Y', '4', '<U/uH>_Z', '4', '<k/uH2>', '4', '<u/uH>', '4', '<uref-u>', '4', '<uref-v>', '4', '<uref-w>', '4', '<urms/uH>', '4', '<v/uH>', '4', '<vrms/uH>', '4', '<w/uH>', '4', '<wrms/uH>', '4', 'Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'error', '4', 'k', '4', 'u:0_average', '4', 'u:0_stddev', '4', 'u:1_average', '4', 'u:1_stddev', '4', 'u:2_average', '4', 'u:2_stddev', '4', 'U', '4', 'x(mm)', '4', 'y(mm)', '4', 'z(mm)', '4']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------


# show data from umagErrorCalculator
umagErrorCalculatorDisplay = Show(umagErrorCalculator, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'error'
sm = servermanager.Fetch(umagErrorCalculator)
r = sm.GetPointData().GetArray('error').GetRange(0)
errorLUT = GetColorTransferFunction('error')
errorLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 25.15632408749082, 0.865003, 0.865003, 0.865003, 50.312648174981646, 0.705882, 0.0156863, 0.14902]
errorLUT.ScalarRangeInitialized = 1.0
errorLUT.RescaleTransferFunction(r[0], r[1])

# trace defaults for the display properties.
umagErrorCalculatorDisplay.Representation = 'Points'
umagErrorCalculatorDisplay.ColorArrayName = ['POINTS', 'error']
umagErrorCalculatorDisplay.LookupTable = errorLUT
umagErrorCalculatorDisplay.PointSize = 5.0
umagErrorCalculatorDisplay.SelectTCoordArray = 'None'
umagErrorCalculatorDisplay.SelectNormalArray = 'None'
umagErrorCalculatorDisplay.SelectTangentArray = 'None'
umagErrorCalculatorDisplay.OSPRayScaleArray = 'error'
umagErrorCalculatorDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
umagErrorCalculatorDisplay.SelectOrientationVectors = '<U/uH>'
umagErrorCalculatorDisplay.ScaleFactor = 0.30000000000000004
umagErrorCalculatorDisplay.SelectScaleArray = 'error'
umagErrorCalculatorDisplay.GlyphType = 'Arrow'
umagErrorCalculatorDisplay.GlyphTableIndexArray = 'error'
umagErrorCalculatorDisplay.GaussianRadius = 0.015
umagErrorCalculatorDisplay.SetScaleArray = ['POINTS', 'error']
umagErrorCalculatorDisplay.ScaleTransferFunction = 'PiecewiseFunction'
umagErrorCalculatorDisplay.OpacityArray = ['POINTS', 'error']
umagErrorCalculatorDisplay.OpacityTransferFunction = 'PiecewiseFunction'
umagErrorCalculatorDisplay.DataAxesGrid = 'GridAxesRepresentation'
umagErrorCalculatorDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
umagErrorCalculatorDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 5541.1793652352535, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
umagErrorCalculatorDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 5541.1793652352535, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for errorLUT in view renderView1
errorLUTColorBar = GetScalarBar(errorLUT, renderView1)
errorLUTColorBar.WindowLocation = 'UpperRightCorner'
errorLUTColorBar.Title = 'error'
errorLUTColorBar.ComponentTitle = ''

# set color bar visibility
errorLUTColorBar.Visibility = 1

# show color legend
umagErrorCalculatorDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'error'
errorPWF = GetOpacityTransferFunction('error')
errorPWF.Points = [0.0, 0.0, 0.5, 0.0, 50.312648174981646, 1.0, 0.5, 0.0]
errorPWF.ScalarRangeInitialized = 1


# ----------------------------------------------------------------
# restore active source
SetActiveSource(pointDatasetInterpolator1)
# ----------------------------------------------------------------

import os.path
from os import path

print("Writing")
# Get the layout/tab for the active view.
aLayout = GetLayout()
SaveScreenshot("./images/validation.png", layout=aLayout)
print("Exiting")
exit()
print("Exiting - shouldnt be here")


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
