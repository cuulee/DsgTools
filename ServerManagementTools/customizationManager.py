# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DsgTools
                                 A QGIS plugin
 Brazilian Army Cartographic Production Tools
                              -------------------
        begin                : 2016-11-22
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Philipe Borba - Cartographic Engineer @ Brazilian Army
        email                : borba.philipe@eb.mil.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
#General imports
from osgeo import ogr
from uuid import uuid4
import codecs, os, json, binascii

#DSG Tools imports
from DsgTools.Factories.DbFactory.dbFactory import DbFactory 
from DsgTools.CustomWidgets.progressWidget import ProgressWidget
from DsgTools.ServerManagementTools.genericDbManager import GenericDbManager
from DsgTools.Utils.utils import Utils

#PyQt4 imports
from PyQt4.Qt import QObject

class CustomizationManager(GenericDbManager):
    '''
    This class manages the customizations on dsgtools databases.
    '''
    def __init__(self, serverAbstractDb, dbDict, parentWidget = None):
        super(self.__class__,self).__init__(serverAbstractDb, dbDict, parentWidget = None)
    
    def installCustomization(self, customizationName):
        """
        1. Get customization from dsgtools_admindb;
        2. Get sql from dbCustomizer;
        3. For each db try to create custom;
        4. If custom applyied, save it on customization table on db and on dsgtools_admindb;
        """
        pass
    
    def removeCustomization(self, customizationName):
        pass

    def updateCustomization(self, customizationName):
        pass

    def validateJsonProfile(self, inputJsonDict):
        '''
        1. Validates each key and value in inputJsonDict;
        2. If input is ok, returns True;
        3. If one piece of json is not valid, returns False.
        This validator does not validate the name of classes or names of categories. It only checks the format of dsgtools json profile.
        '''
        #TODO
        return True
