import DBConnect
from DataGrid import DataGrid
from DataModel import DataModel
from ImageControlPanel import ImageControlPanel
from Properties import Properties
from ScoreDialog import ScoreDialog
import SortBin
from TileCollection import EVT_TILE_UPDATED
from TrainingSet import TrainingSet
from cStringIO import StringIO
import DirichletIntegrate
import FastGentleBoostingMulticlass
import ImageTools
import MulticlassSQL
import PolyaFit
import numpy
import os
import wx
from ClassifierGUI import *


import time
if __name__ == "__main__":
    app = wx.PySimpleApp()

    p = Properties.getInstance()
    db = DBConnect.DBConnect.getInstance()
    dm = DataModel.getInstance()

#    props = '/Volumes/imaging_analysis/2007_10_19_Gilliland_LeukemiaScreens/Screen3_1Apr09_run3/2007_10_19_Gilliland_LeukemiaScreens_Validation_v2_AllBatches_DuplicatesFiltered_FullBarcode_testSinglePlate.properties'
#    ts = '/Volumes/imaging_analysis/2007_10_19_Gilliland_LeukemiaScreens/Screen3_1Apr09_run3/trainingvalidation3b.txt'
    props = '../Properties/nirht_area_test.properties'
    ts = '/Users/afraser/Desktop/MyTrainingSet.txt'
    p.LoadFile(props)
    classifier = ClassifierGUI(p)
    classifier.Show(True)
    classifier.LoadTrainingSet(ts)
    time.sleep(3)
    classifier.FindRules()
    classifier.ScoreAll()
    
    app.MainLoop()