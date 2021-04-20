# state file generated using paraview version 5.8.1-1634-g6bacce2f26

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

u_h = 2
u_w = 1
u_l = 1

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [1824, 260]
lineChartView1.LegendPosition = [1678, 67]

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
lineChartView2.ViewSize = [1824, 272]
lineChartView2.ShowLegend = 0
lineChartView2.LegendPosition = [1716, 219]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [920, 446]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.75, 0.0, 0.75]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-3.577469775664388, -4.473655711748439, 1.1137085481439672]
renderView1.CameraFocalPoint = [0.75, -8.815605700987314e-16, 0.750000000000001]
renderView1.CameraViewUp = [0.0553614520192397, 0.027591988872621594, 0.998085062397176]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.9525624189766635
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = 'M2'
spreadSheetView1.BlockSize = 1024
spreadSheetView1.HiddenColumnLabels = ['Block Number', 'Cardinality', 'Row ID', 'Block Name', 'M2', 'M3', 'M4']
spreadSheetView1.FieldAssociation = 'Row Data'

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.430233)
layout1.SplitHorizontal(1, 0.509804)
layout1.AssignView(3, renderView1)
layout1.AssignView(4, spreadSheetView1)
layout1.SplitVertical(2, 0.488235)
layout1.AssignView(5, lineChartView1)
layout1.AssignView(6, lineChartView2)
layout1.SetSize(1824, 980)

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

# create a new 'Calculator'
rescaleResults = Calculator(registrationName='RescaleResults', Input=uxdmf)
rescaleResults.CoordinateResults = 1
rescaleResults.Function = 'iHat*(coordsX/2) +jHat*(coordsY/2) +kHat*(coordsZ/2)' # divide coords by height building

writer = CreateWriter("./dataset.csv")
writer.FieldAssociation = "Point Data"
writer.UpdatePipeline()

# create a new 'CSV Reader'
caseHcsv = CSVReader(registrationName='CaseH_u.csv', FileName=['./pvScripts/CaseH_u.csv'])

# create a new 'Table To Points'
valiToPoints = TableToPoints(registrationName='ValiToPoints', Input=caseHcsv)
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
translatePoints.Function = 'coords+iHat*0.25' #translate points so that origin aligns with origin in results

# read results back in through csv file
datasetcsv = CSVReader(registrationName='dataset.csv', FileName=['./dataset.csv'])

# create a new 'Table To Points'
resToPoints = TableToPoints(registrationName='ResToPoints', Input=datasetcsv)
resToPoints.XColumn = 'Points:0'
resToPoints.YColumn = 'Points:1'
resToPoints.ZColumn = 'Points:2'

# get mean and standard deviation of the results
temporalStatistics1 = TemporalStatistics(registrationName='TemporalStatistics1', Input=resToPoints)
temporalStatistics1.ComputeMinimum = 0
temporalStatistics1.ComputeMaximum = 0

# calculate turbulence kinetic energy
calculator_TKE = Calculator(registrationName='Calculator_TKE', Input=temporalStatistics1)
calculator_TKE.ResultArrayName = 'k'
calculator_TKE.Function = 'sqrt(u:0_stddev^2+u:1_stddev^2+u:2_stddev^2)'

# interpolate results at points from validation data
pointDatasetInterpolator1 = PointDatasetInterpolator(registrationName='PointDatasetInterpolator1', Input=calculator_TKE,
    Source=translatePoints)
pointDatasetInterpolator1.Kernel = 'LinearKernel'
pointDatasetInterpolator1.Locator = 'Static Point Locator'

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[pointDatasetInterpolator1, translatePoints])

# calcultate magnitude of average flow
umagCalculator = Calculator(registrationName = 'UmagCalculator', Input = appendAttributes1)
umagErrorCalculator.ResultArrayName = 'u_mag'
umagErrorCalculator.Function = 'sqrt(u:0_average^2 + u:1_average^2 + u:2_average^2)'

# calculate error on magnitude
umagErrorCalculator = Calculator(registrationName='UmagErrorCalculator', Input=umagCalculator)
umagErrorCalculator.ResultArrayName = 'error'
umagErrorCalculator.Function = 'abs(mag(<U/uH>)-u_mag)/mag(<U/uH>)'

# create a new 'Mask Points'
maskPoints1 = MaskPoints(registrationName='MaskPoints1', Input=umagErrorCalculator)
maskPoints1.OnRatio = 1
maskPoints1.RandomSampling = True
maskPoints1.RandomSamplingMode = 1

# create a new 'Plot Data'
plotData3 = PlotData(registrationName='PlotData3', Input=maskPoints1)

# create a new 'Plot Data'
plotData1 = PlotData(registrationName='PlotData1', Input=maskPoints1)

# create a new 'Descriptive Statistics'
descriptiveStatistics1 = DescriptiveStatistics(registrationName='DescriptiveStatistics1', Input=umagErrorCalculator,
    ModelInput=None)
descriptiveStatistics1.VariablesofInterest = ['error']

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView1'
# ----------------------------------------------------------------

# show data from plotData3
plotData3Display = Show(plotData3, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotData3Display.CompositeDataSetIndex = [0]
plotData3Display.XArrayName = '<c>(ppm)'
plotData3Display.SeriesVisibility = ['<u/uH>', '<v/uH>', '<w/uH>', 'u:0_average', 'u:1_average', 'u:2_average']
plotData3Display.SeriesLabel = ['<c>(ppm)', '<c>(ppm)', '<c>/Co', '<c>/Co', '<k/uH2>', '<k/uH2>', '<U/uH>_X', '<U/uH>_X', '<U/uH>_Y', '<U/uH>_Y', '<U/uH>_Z', '<U/uH>_Z', '<U/uH>_Magnitude', '<U/uH>_Magnitude', '<u/uH>', '<u/uH>', '<uref-u>', '<uref-u>', '<uref-v>', '<uref-v>', '<uref-w>', '<uref-w>', '<urms/uH>', '<urms/uH>', '<v/uH>', '<v/uH>', '<vrms/uH>', '<vrms/uH>', '<w/uH>', '<w/uH>', '<wrms/uH>', '<wrms/uH>', 'error', 'error', 'k', 'k', 'Point ID_average', 'Point ID_average', 'Point ID_stddev', 'Point ID_stddev', 'Points_Magnitude_average', 'Points_Magnitude_average', 'Points_Magnitude_stddev', 'Points_Magnitude_stddev', 'u:0_average', '<u/uH>', 'u:0_stddev', 'u:0_stddev', 'u:1_average', '<v/uH>', 'u:1_stddev', 'u:1_stddev', 'u:2_average', '<w/uH>', 'u:2_stddev', 'u:2_stddev', 'u_mag', 'u_mag', 'x(mm)', 'x(mm)', 'y(mm)', 'y(mm)', 'z(mm)', 'z(mm)', 'ÏC(ppm)', 'ÏC(ppm)', 'ÏC/Co', 'ÏC/Co', 'Point ID', 'Point ID', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotData3Display.SeriesColor = ['<c>(ppm)', '0', '0', '0', '<c>/Co', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', '<k/uH2>', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', '<U/uH>_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', '<U/uH>_Y', '0.6', '0.3100022888532845', '0.6399938963912413', '<U/uH>_Z', '1', '0.5000076295109483', '0', '<U/uH>_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', '<u/uH>', '1', '0', '0', '<uref-u>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', '<uref-v>', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', '<uref-w>', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', '<urms/uH>', '0.6', '0.3100022888532845', '0.6399938963912413', '<v/uH>', '0', '0.3333333333333333', '1', '<vrms/uH>', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', '<w/uH>', '0.3333333333333333', '0.6666666666666666', '0', '<wrms/uH>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'error', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'k', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Point ID_average', '0.6', '0.3100022888532845', '0.6399938963912413', 'Point ID_stddev', '1', '0.5000076295109483', '0', 'Points_Magnitude_average', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Magnitude_stddev', '0', '0', '0', 'u:0_average', '1', '0.6078431372549019', '0.6078431372549019', 'u:0_stddev', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u:1_average', '0.6078431372549019', '0.8705882352941177', '1', 'u:1_stddev', '0.6', '0.3100022888532845', '0.6399938963912413', 'u:2_average', '0.6235294117647059', '0.7764705882352941', '0.47058823529411764', 'u:2_stddev', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_mag', '0', '0', '0', 'x(mm)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'y(mm)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'z(mm)', '0.6', '0.3100022888532845', '0.6399938963912413', 'ÏC(ppm)', '1', '0.5000076295109483', '0', 'ÏC/Co', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Point ID', '0', '0', '0', 'Points_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413']
plotData3Display.SeriesPlotCorner = ['<U/uH>_Magnitude', '0', '<U/uH>_X', '0', '<U/uH>_Y', '0', '<U/uH>_Z', '0', '<c>(ppm)', '0', '<c>/Co', '0', '<k/uH2>', '0', '<u/uH>', '0', '<uref-u>', '0', '<uref-v>', '0', '<uref-w>', '0', '<urms/uH>', '0', '<v/uH>', '0', '<vrms/uH>', '0', '<w/uH>', '0', '<wrms/uH>', '0', 'Point ID', '0', 'Point ID_average', '0', 'Point ID_stddev', '0', 'Points_Magnitude', '0', 'Points_Magnitude_average', '0', 'Points_Magnitude_stddev', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'error', '0', 'k', '0', 'u:0_average', '0', 'u:0_stddev', '0', 'u:1_average', '0', 'u:1_stddev', '0', 'u:2_average', '0', 'u:2_stddev', '0', 'u_mag', '0',  'x(mm)', '0', 'y(mm)', '0', 'z(mm)', '0', 'ÏC(ppm)', '0', 'ÏC/Co', '0']
plotData3Display.SeriesLabelPrefix = ''
plotData3Display.SeriesLineStyle = ['<U/uH>_Magnitude', '1', '<U/uH>_X', '1', '<U/uH>_Y', '1', '<U/uH>_Z', '1', '<c>(ppm)', '1', '<c>/Co', '1', '<k/uH2>', '1', '<u/uH>', '0', '<uref-u>', '1', '<uref-v>', '1', '<uref-w>', '1', '<urms/uH>', '1', '<v/uH>', '0', '<vrms/uH>', '1', '<w/uH>', '0', '<wrms/uH>', '1', 'Point ID', '1', 'Point ID_average', '1', 'Point ID_stddev', '1', 'Points_Magnitude', '1', 'Points_Magnitude_average', '1', 'Points_Magnitude_stddev', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'error', '1', 'k', '1', 'u:0_average', '1', 'u:0_stddev', '1', 'u:1_average', '1', 'u:1_stddev', '1', 'u:2_average', '1', 'u:2_stddev', '1', 'u_mag', '1', 'x(mm)', '1', 'y(mm)', '1', 'z(mm)', '1', 'ÏC(ppm)', '1', 'ÏC/Co', '1']
plotData3Display.SeriesLineThickness = ['<U/uH>_Magnitude', '2', '<U/uH>_X', '2', '<U/uH>_Y', '2', '<U/uH>_Z', '2', '<c>(ppm)', '2', '<c>/Co', '2', '<k/uH2>', '2', '<u/uH>', '2', '<uref-u>', '2', '<uref-v>', '2', '<uref-w>', '2', '<urms/uH>', '2', '<v/uH>', '2', '<vrms/uH>', '2', '<w/uH>', '2', '<wrms/uH>', '2', 'Point ID', '2', 'Point ID_average', '2', 'Point ID_stddev', '2', 'Points_Magnitude', '2', 'Points_Magnitude_average', '2', 'Points_Magnitude_stddev', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'error', '2', 'k', '2', 'u:0_average', '2', 'u:0_stddev', '2', 'u:1_average', '2', 'u:1_stddev', '2', 'u:2_average', '2', 'u:2_stddev', '2', 'u_mag', '2', 'x(mm)', '2', 'y(mm)', '2', 'z(mm)', '2', 'ÏC(ppm)', '2', 'ÏC/Co', '2']
plotData3Display.SeriesMarkerStyle = ['<U/uH>_Magnitude', '0', '<U/uH>_X', '0', '<U/uH>_Y', '0', '<U/uH>_Z', '0', '<c>(ppm)', '0', '<c>/Co', '0', '<k/uH2>', '0', '<u/uH>', '4', '<uref-u>', '0', '<uref-v>', '0', '<uref-w>', '0', '<urms/uH>', '0', '<v/uH>', '2', '<vrms/uH>', '0', '<w/uH>', '1', '<wrms/uH>', '0', 'Point ID', '0', 'Point ID_average', '0', 'Point ID_stddev', '0', 'Points_Magnitude', '0', 'Points_Magnitude_average', '0', 'Points_Magnitude_stddev', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'error', '0', 'k', '0', 'u:0_average', '0', 'u:0_stddev', '0', 'u:1_average', '0', 'u:1_stddev', '0', 'u:2_average', '0', 'u:2_stddev', '0', 'u_mag', '0', 'x(mm)', '0', 'y(mm)', '0', 'z(mm)', '0', 'ÏC(ppm)', '0', 'ÏC/Co', '0']
plotData3Display.SeriesMarkerSize = ['<U/uH>_Magnitude', '4', '<U/uH>_X', '4', '<U/uH>_Y', '4', '<U/uH>_Z', '4', '<c>(ppm)', '4', '<c>/Co', '4', '<k/uH2>', '4', '<u/uH>', '4', '<uref-u>', '4', '<uref-v>', '4', '<uref-w>', '4', '<urms/uH>', '4', '<v/uH>', '4', '<vrms/uH>', '4', '<w/uH>', '4', '<wrms/uH>', '4', 'Point ID', '4', 'Point ID_average', '4', 'Point ID_stddev', '4', 'Points_Magnitude', '4', 'Points_Magnitude_average', '4', 'Points_Magnitude_stddev', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'error', '4', 'k', '4', 'u:0_average', '4', 'u:0_stddev', '4', 'u:1_average', '4', 'u:1_stddev', '4', 'u:2_average', '4', 'u:2_stddev', '4', 'u_mag', '4', 'x(mm)', '4', 'y(mm)', '4', 'z(mm)', '4', 'ÏC(ppm)', '4', 'ÏC/Co', '4']

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView2'
# ----------------------------------------------------------------

# show data from plotData3
plotData3Display_1 = Show(plotData3, lineChartView2, 'XYChartRepresentation')

# trace defaults for the display properties.
plotData3Display_1.CompositeDataSetIndex = [0]
plotData3Display_1.XArrayName = '<c>(ppm)'
plotData3Display_1.SeriesVisibility = []
plotData3Display_1.SeriesLabel = ['<c>(ppm)', '<c>(ppm)', '<c>/Co', '<c>/Co', '<k/uH2>', '<k/uH2>', '<U/uH>_X', '<U/uH>_X', '<U/uH>_Y', '<U/uH>_Y', '<U/uH>_Z', '<U/uH>_Z', '<U/uH>_Magnitude', '<U/uH>_Magnitude', '<u/uH>', '<u/uH>', '<uref-u>', '<uref-u>', '<uref-v>', '<uref-v>', '<uref-w>', '<uref-w>', '<urms/uH>', '<urms/uH>', '<v/uH>', '<v/uH>', '<vrms/uH>', '<vrms/uH>', '<w/uH>', '<w/uH>', '<wrms/uH>', '<wrms/uH>', 'error', 'error on magnitude <U>', 'k', 'k', 'Point ID_average', 'Point ID_average', 'Point ID_stddev', 'Point ID_stddev', 'Points_Magnitude_average', 'Points_Magnitude_average', 'Points_Magnitude_stddev', 'Points_Magnitude_stddev', 'u:0_average', 'u:0_average', 'u:0_stddev', 'u:0_stddev', 'u:1_average', 'u:1_average', 'u:1_stddev', 'u:1_stddev', 'u:2_average', 'u:2_average', 'u:2_stddev', 'u:2_stddev', 'u_mag', 'u_mag', 'x(mm)', 'x(mm)', 'y(mm)', 'y(mm)', 'z(mm)', 'z(mm)', 'ÏC(ppm)', 'ÏC(ppm)', 'ÏC/Co', 'ÏC/Co', 'Point ID', 'Point ID', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotData3Display_1.SeriesColor = ['<c>(ppm)', '0', '0', '0', '<c>/Co', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', '<k/uH2>', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', '<U/uH>_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', '<U/uH>_Y', '0.6', '0.3100022888532845', '0.6399938963912413', '<U/uH>_Z', '1', '0.5000076295109483', '0', '<U/uH>_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', '<u/uH>', '0', '0', '0', '<uref-u>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', '<uref-v>', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', '<uref-w>', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', '<urms/uH>', '0.6', '0.3100022888532845', '0.6399938963912413', '<v/uH>', '1', '0.5000076295109483', '0', '<vrms/uH>', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', '<w/uH>', '0', '0', '0', '<wrms/uH>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'error', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'k', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Point ID_average', '0.6', '0.3100022888532845', '0.6399938963912413', 'Point ID_stddev', '1', '0.5000076295109483', '0', 'Points_Magnitude_average', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Magnitude_stddev', '0', '0', '0', 'u:0_average', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u:0_stddev', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u:1_average', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u:1_stddev', '0.6', '0.3100022888532845', '0.6399938963912413', 'u:2_average', '1', '0.5000076295109483', '0', 'u:2_stddev', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_mag', '0', '0', '0', 'x(mm)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'y(mm)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'z(mm)', '0.6', '0.3100022888532845', '0.6399938963912413', 'ÏC(ppm)', '1', '0.5000076295109483', '0', 'ÏC/Co', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Point ID', '0', '0', '0', 'Points_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413']
plotData3Display_1.SeriesPlotCorner = ['<U/uH>_Magnitude', '0', '<U/uH>_X', '0', '<U/uH>_Y', '0', '<U/uH>_Z', '0', '<c>(ppm)', '0', '<c>/Co', '0', '<k/uH2>', '0', '<u/uH>', '0', '<uref-u>', '0', '<uref-v>', '0', '<uref-w>', '0', '<urms/uH>', '0', '<v/uH>', '0', '<vrms/uH>', '0', '<w/uH>', '0', '<wrms/uH>', '0', 'Point ID', '0', 'Point ID_average', '0', 'Point ID_stddev', '0', 'Points_Magnitude', '0', 'Points_Magnitude_average', '0', 'Points_Magnitude_stddev', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'error', '0', 'k', '0', 'u:0_average', '0', 'u:0_stddev', '0', 'u:1_average', '0', 'u:1_stddev', '0', 'u:2_average', '0', 'u:2_stddev', '0', 'u_mag', '0', 'x(mm)', '0', 'y(mm)', '0', 'z(mm)', '0', 'ÏC(ppm)', '0', 'ÏC/Co', '0']
plotData3Display_1.SeriesLabelPrefix = ''
plotData3Display_1.SeriesLineStyle = ['<U/uH>_Magnitude', '1', '<U/uH>_X', '1', '<U/uH>_Y', '1', '<U/uH>_Z', '1', '<c>(ppm)', '1', '<c>/Co', '1', '<k/uH2>', '1', '<u/uH>', '1', '<uref-u>', '1', '<uref-v>', '1', '<uref-w>', '1', '<urms/uH>', '1', '<v/uH>', '1', '<vrms/uH>', '1', '<w/uH>', '1', '<wrms/uH>', '1', 'Point ID', '1', 'Point ID_average', '1', 'Point ID_stddev', '1', 'Points_Magnitude', '1', 'Points_Magnitude_average', '1', 'Points_Magnitude_stddev', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'error', '1', 'k', '1', 'u:0_average', '1', 'u:0_stddev', '1', 'u:1_average', '1', 'u:1_stddev', '1', 'u:2_average', '1', 'u:2_stddev', '1', 'u_mag', '1', 'x(mm)', '1', 'y(mm)', '1', 'z(mm)', '1', 'ÏC(ppm)', '1', 'ÏC/Co', '1']
plotData3Display_1.SeriesLineThickness = ['<U/uH>_Magnitude', '2', '<U/uH>_X', '2', '<U/uH>_Y', '2', '<U/uH>_Z', '2', '<c>(ppm)', '2', '<c>/Co', '2', '<k/uH2>', '2', '<u/uH>', '2', '<uref-u>', '2', '<uref-v>', '2', '<uref-w>', '2', '<urms/uH>', '2', '<v/uH>', '2', '<vrms/uH>', '2', '<w/uH>', '2', '<wrms/uH>', '2', 'Point ID', '2', 'Point ID_average', '2', 'Point ID_stddev', '2', 'Points_Magnitude', '2', 'Points_Magnitude_average', '2', 'Points_Magnitude_stddev', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'error', '2', 'k', '2', 'u:0_average', '2', 'u:0_stddev', '2', 'u:1_average', '2', 'u:1_stddev', '2', 'u:2_average', '2', 'u:2_stddev', '2', 'u_mag', '2', 'x(mm)', '2', 'y(mm)', '2', 'z(mm)', '2', 'ÏC(ppm)', '2', 'ÏC/Co', '2']
plotData3Display_1.SeriesMarkerStyle = ['<U/uH>_Magnitude', '0', '<U/uH>_X', '0', '<U/uH>_Y', '0', '<U/uH>_Z', '0', '<c>(ppm)', '0', '<c>/Co', '0', '<k/uH2>', '0', '<u/uH>', '0', '<uref-u>', '0', '<uref-v>', '0', '<uref-w>', '0', '<urms/uH>', '0', '<v/uH>', '0', '<vrms/uH>', '0', '<w/uH>', '0', '<wrms/uH>', '0', 'Point ID', '0', 'Point ID_average', '0', 'Point ID_stddev', '0', 'Points_Magnitude', '0', 'Points_Magnitude_average', '0', 'Points_Magnitude_stddev', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'error', '0', 'k', '0', 'u:0_average', '0', 'u:0_stddev', '0', 'u:1_average', '0', 'u:1_stddev', '0', 'u:2_average', '0', 'u:2_stddev', '0', 'u_mag', '0', 'x(mm)', '0', 'y(mm)', '0', 'z(mm)', '0', 'ÏC(ppm)', '0', 'ÏC/Co', '0']
plotData3Display_1.SeriesMarkerSize = ['<U/uH>_Magnitude', '4', '<U/uH>_X', '4', '<U/uH>_Y', '4', '<U/uH>_Z', '4', '<c>(ppm)', '4', '<c>/Co', '4', '<k/uH2>', '4', '<u/uH>', '4', '<uref-u>', '4', '<uref-v>', '4', '<uref-w>', '4', '<urms/uH>', '4', '<v/uH>', '4', '<vrms/uH>', '4', '<w/uH>', '4', '<wrms/uH>', '4', 'Point ID', '4', 'Point ID_average', '4', 'Point ID_stddev', '4', 'Points_Magnitude', '4', 'Points_Magnitude_average', '4', 'Points_Magnitude_stddev', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'error', '4', 'k', '4', 'u:0_average', '4', 'u:0_stddev', '4', 'u:1_average', '4', 'u:1_stddev', '4', 'u:2_average', '4', 'u:2_stddev', '4', 'u_mag', '4', 'x(mm)', '4', 'y(mm)', '4', 'z(mm)', '4', 'ÏC(ppm)', '4', 'ÏC/Co', '4']

# show data from plotData1
plotData1Display = Show(plotData1, lineChartView2, 'XYChartRepresentation')

# trace defaults for the display properties.
plotData1Display.CompositeDataSetIndex = [0]
plotData1Display.XArrayName = '<c>(ppm)'
plotData1Display.SeriesVisibility = ['error']
plotData1Display.SeriesLabel = ['<c>(ppm)', '<c>(ppm)', '<c>/Co', '<c>/Co', '<k/uH2>', '<k/uH2>', '<U/uH>_X', '<U/uH>_X', '<U/uH>_Y', '<U/uH>_Y', '<U/uH>_Z', '<U/uH>_Z', '<U/uH>_Magnitude', '<U/uH>_Magnitude', '<u/uH>', '<u/uH>', '<uref-u>', '<uref-u>', '<uref-v>', '<uref-v>', '<uref-w>', '<uref-w>', '<urms/uH>', '<urms/uH>', '<v/uH>', '<v/uH>', '<vrms/uH>', '<vrms/uH>', '<w/uH>', '<w/uH>', '<wrms/uH>', '<wrms/uH>', 'error', 'error', 'k', 'k', 'Point ID_average', 'Point ID_average', 'Point ID_stddev', 'Point ID_stddev', 'Points_Magnitude_average', 'Points_Magnitude_average', 'Points_Magnitude_stddev', 'Points_Magnitude_stddev', 'u:0_average', 'u:0_average', 'u:0_stddev', 'u:0_stddev', 'u:1_average', 'u:1_average', 'u:1_stddev', 'u:1_stddev', 'u:2_average', 'u:2_average', 'u:2_stddev', 'u:2_stddev', 'u_mag', 'u_mag', 'x(mm)', 'x(mm)', 'y(mm)', 'y(mm)', 'z(mm)', 'z(mm)', 'ÏC(ppm)', 'ÏC(ppm)', 'ÏC/Co', 'ÏC/Co', 'Point ID', 'Point ID', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotData1Display.SeriesColor = ['<c>(ppm)', '0', '0', '0', '<c>/Co', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', '<k/uH2>', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', '<U/uH>_X', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', '<U/uH>_Y', '0.6', '0.3100022888532845', '0.6399938963912413', '<U/uH>_Z', '1', '0.5000076295109483', '0', '<U/uH>_Magnitude', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', '<u/uH>', '0', '0', '0', '<uref-u>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', '<uref-v>', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', '<uref-w>', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', '<urms/uH>', '0.6', '0.3100022888532845', '0.6399938963912413', '<v/uH>', '1', '0.5000076295109483', '0', '<vrms/uH>', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', '<w/uH>', '0', '0', '0', '<wrms/uH>', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'error', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'k', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Point ID_average', '0.6', '0.3100022888532845', '0.6399938963912413', 'Point ID_stddev', '1', '0.5000076295109483', '0', 'Points_Magnitude_average', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_Magnitude_stddev', '0', '0', '0', 'u:0_average', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'u:0_stddev', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'u:1_average', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'u:1_stddev', '0.6', '0.3100022888532845', '0.6399938963912413', 'u:2_average', '1', '0.5000076295109483', '0', 'u:2_stddev', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'u_mag', '0', '0', '0', 'x(mm)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'y(mm)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'z(mm)', '0.6', '0.3100022888532845', '0.6399938963912413', 'ÏC(ppm)', '1', '0.5000076295109483', '0', 'ÏC/Co', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Point ID', '0', '0', '0', 'Points_X', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Y', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Z', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'Points_Magnitude', '0.6', '0.3100022888532845', '0.6399938963912413']
plotData1Display.SeriesPlotCorner = ['<U/uH>_Magnitude', '0', '<U/uH>_X', '0', '<U/uH>_Y', '0', '<U/uH>_Z', '0', '<c>(ppm)', '0', '<c>/Co', '0', '<k/uH2>', '0', '<u/uH>', '0', '<uref-u>', '0', '<uref-v>', '0', '<uref-w>', '0', '<urms/uH>', '0', '<v/uH>', '0', '<vrms/uH>', '0', '<w/uH>', '0', '<wrms/uH>', '0', 'Point ID', '0', 'Point ID_average', '0', 'Point ID_stddev', '0', 'Points_Magnitude', '0', 'Points_Magnitude_average', '0', 'Points_Magnitude_stddev', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'error', '0', 'k', '0', 'u:0_average', '0', 'u:0_stddev', '0', 'u:1_average', '0', 'u:1_stddev', '0', 'u:2_average', '0', 'u:2_stddev', '0', 'u_mag', '0', 'x(mm)', '0', 'y(mm)', '0', 'z(mm)', '0', 'ÏC(ppm)', '0', 'ÏC/Co', '0']
plotData1Display.SeriesLabelPrefix = ''
plotData1Display.SeriesLineStyle = ['<U/uH>_Magnitude', '1', '<U/uH>_X', '1', '<U/uH>_Y', '1', '<U/uH>_Z', '1', '<c>(ppm)', '1', '<c>/Co', '1', '<k/uH2>', '1', '<u/uH>', '1', '<uref-u>', '1', '<uref-v>', '1', '<uref-w>', '1', '<urms/uH>', '1', '<v/uH>', '1', '<vrms/uH>', '1', '<w/uH>', '1', '<wrms/uH>', '1', 'Point ID', '1', 'Point ID_average', '1', 'Point ID_stddev', '1', 'Points_Magnitude', '1', 'Points_Magnitude_average', '1', 'Points_Magnitude_stddev', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'error', '0', 'k', '1', 'u:0_average', '1', 'u:0_stddev', '1', 'u:1_average', '1', 'u:1_stddev', '1', 'u:2_average', '1', 'u:2_stddev', '1', 'u_mag', '1', 'x(mm)', '1', 'y(mm)', '1', 'z(mm)', '1', 'ÏC(ppm)', '1', 'ÏC/Co', '1']
plotData1Display.SeriesLineThickness = ['<U/uH>_Magnitude', '2', '<U/uH>_X', '2', '<U/uH>_Y', '2', '<U/uH>_Z', '2', '<c>(ppm)', '2', '<c>/Co', '2', '<k/uH2>', '2', '<u/uH>', '2', '<uref-u>', '2', '<uref-v>', '2', '<uref-w>', '2', '<urms/uH>', '2', '<v/uH>', '2', '<vrms/uH>', '2', '<w/uH>', '2', '<wrms/uH>', '2', 'Point ID', '2', 'Point ID_average', '2', 'Point ID_stddev', '2', 'Points_Magnitude', '2', 'Points_Magnitude_average', '2', 'Points_Magnitude_stddev', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'error', '2', 'k', '2', 'u:0_average', '2', 'u:0_stddev', '2', 'u:1_average', '2', 'u:1_stddev', '2', 'u:2_average', '2', 'u:2_stddev', '2', 'u_mag', '2', 'x(mm)', '2', 'y(mm)', '2', 'z(mm)', '2', 'ÏC(ppm)', '2', 'ÏC/Co', '2']
plotData1Display.SeriesMarkerStyle = ['<U/uH>_Magnitude', '0', '<U/uH>_X', '0', '<U/uH>_Y', '0', '<U/uH>_Z', '0', '<c>(ppm)', '0', '<c>/Co', '0', '<k/uH2>', '0', '<u/uH>', '0', '<uref-u>', '0', '<uref-v>', '0', '<uref-w>', '0', '<urms/uH>', '0', '<v/uH>', '0', '<vrms/uH>', '0', '<w/uH>', '0', '<wrms/uH>', '0', 'Point ID', '0', 'Point ID_average', '0', 'Point ID_stddev', '0', 'Points_Magnitude', '0', 'Points_Magnitude_average', '0', 'Points_Magnitude_stddev', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'error', '1', 'k', '0', 'u:0_average', '0', 'u:0_stddev', '0', 'u:1_average', '0', 'u:1_stddev', '0', 'u:2_average', '0', 'u:2_stddev', '0', 'u_mag', '0', 'x(mm)', '0', 'y(mm)', '0', 'z(mm)', '0', 'ÏC(ppm)', '0', 'ÏC/Co', '0']
plotData1Display.SeriesMarkerSize = ['<U/uH>_Magnitude', '4', '<U/uH>_X', '4', '<U/uH>_Y', '4', '<U/uH>_Z', '4', '<c>(ppm)', '4', '<c>/Co', '4', '<k/uH2>', '4', '<u/uH>', '4', '<uref-u>', '4', '<uref-v>', '4', '<uref-w>', '4', '<urms/uH>', '4', '<v/uH>', '4', '<vrms/uH>', '4', '<w/uH>', '4', '<wrms/uH>', '4', 'Point ID', '4', 'Point ID_average', '4', 'Point ID_stddev', '4', 'Points_Magnitude', '4', 'Points_Magnitude_average', '4', 'Points_Magnitude_stddev', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'error', '8', 'k', '4', 'u:0_average', '4', 'u:0_stddev', '4', 'u:1_average', '4', 'u:1_stddev', '4', 'u:2_average', '4', 'u:2_stddev', '4', 'u_mag', '4', 'x(mm)', '4', 'y(mm)', '4', 'z(mm)', '4', 'ÏC(ppm)', '4', 'ÏC/Co', '4']

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
# setup the visualization in view 'spreadSheetView1'
# ----------------------------------------------------------------

# show data from descriptiveStatistics1
descriptiveStatistics1Display = Show(descriptiveStatistics1, spreadSheetView1, 'SpreadSheetRepresentation')

# trace defaults for the display properties.
descriptiveStatistics1Display.CompositeDataSetIndex = [1]

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
SetActiveSource(plotData1)
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
