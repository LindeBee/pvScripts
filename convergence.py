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
lineChartView1.ViewSize = [2018, 1134]
lineChartView1.LeftAxisTitle = 'mean velocity in area of interest'
lineChartView1.BottomAxisTitle = 'time'
lineChartView1.ShowLegend = 0

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, lineChartView1)
layout1.SetSize(2018, 1134)

# ----------------------------------------------------------------
# restore active view
SetActiveView(lineChartView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'CSV Reader'
mean_vel2csv = CSVReader(registrationName='mean_vel.csv', FileName=['./results/mean_vel.csv'])

# create a new 'Plot Data'
plotData1 = PlotData(registrationName='PlotData1', Input=mean_vel2csv)

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView1'
# ----------------------------------------------------------------

# show data from plotData1
plotData1Display = Show(plotData1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotData1Display.CompositeDataSetIndex = [0]
plotData1Display.AttributeType = 'Row Data'
plotData1Display.UseIndexForXAxis = 0
plotData1Display.XArrayName = 'time'
plotData1Display.SeriesVisibility = ['<U/uH>']
plotData1Display.SeriesLabel = ['<U/uH>', '<U/uH>', 'time', 'time']
plotData1Display.SeriesColor = ['<U/uH>', '0', '0', '0', 'time', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845']
plotData1Display.SeriesPlotCorner = ['<U/uH>', '0', 'time', '0']
plotData1Display.SeriesLabelPrefix = ''
plotData1Display.SeriesLineStyle = ['<U/uH>', '1', 'time', '1']
plotData1Display.SeriesLineThickness = ['<U/uH>', '2', 'time', '2']
plotData1Display.SeriesMarkerStyle = ['<U/uH>', '0', 'time', '0']
plotData1Display.SeriesMarkerSize = ['<U/uH>', '4', 'time', '4']

# ----------------------------------------------------------------
# restore active source
SetActiveSource(plotData1)
# ----------------------------------------------------------------

import os.path
from os import path

print("Rendering: convergence")
SaveScreenshot('./images/convergence.png', lineChartView1, ImageResolution=[2018, 1134])

print("Exiting")
exit()
print("Exiting - shouldnt be here")

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
