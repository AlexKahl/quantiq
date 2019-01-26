
# -*- coding: utf-8 -*-
"""
@title: Py script generic title
@author: vcl2311
@date: Fri Jan 25 10:53:21 2019
@version: 0.01
@description: brief summary
@Details: detailed description
@external file paths:
@key inputs:
@key variables:
@external sources:
@key output:
@comment:
"""


import requests
import pandas as pd
from datetime import datetime

from raphka.settings import config
logger = config.logging.getLogger('debug')
from raphka.classes import Connection

av_settings = config.alphavantage_settings

class Equity():

    def __init__(self,
                 symbol = None,
                 name = None,
                 industry = None,
                 sector = None,
                 exchange = None,
                 datafreq = 'Daily',
                 hasdata = False,
                 data = None,
                 connection = None):

    
        """Equity: object instantiation of class Equity
        
        Description:
        ------------------
        This function creates an instance of class Equity. It will be used to 
        analyse Equity Performance and Risk with data from Alpha Vantage.
        
        Inputs/variables:
        ------------------
        
        symbol : string symbol of instrument
        name: string name of equity
        industry: string industry of equity
        sector = string sector of equity
        exchange: string stock exchange of equity
        datafreq: string indicating data frequency
        hasdata: boolean value indicating if  equity has data
        data: pandas dataframe with equity data
        connection: connection object
    
        methods:
        ------------------
        getData: fetching data for given symbol          
        
        """
                
        self.symbol = symbol
        self.name = name
        self.industry = industry
        self.sector = sector
        self.exchange = exchange
        self.hasdata = hasdata
        self.data = data
        self.connection = connection


    def getData(self,datafreq="Daily",size="full",overwrite=False):
        
        """getData method:fetching data from alpha vantage
        
        Description:
        ------------------
        Loadind data from Alpha vantage method
        Getting static data from source (currently excel)
        
        Inputs/variables:
        ------------------
        
        datafreq : string data frequency
        size: string size of the data 
        overwrite: boolean value indicating whether data should be read again
    
        methods:
        ------------------
        getData: fetching data for given equity          
        
        """
        try:
            
            if (self.hasdata and not overwrite):
                return(True)
            
            if not isinstance(self.connection,Connection):
                raise RuntimeError("Equity object has no connection!")
            
            symbol = self.symbol
            
            eqs = self.connection.get_connection('equitystatic')
            
            statics = eqs.loc[symbol]
            if (statics.shape[0]==0):
                raise ValueError("Symbol {} not found!".format(symbol))
                
            self.name = statics['name']
            self.industry = statics['industry']
            self.sector = statics['sector']
            self.exchange = statics['exchange']
            
            
            # loading data from alpha vantage
            av = self.connection.get_connection('alphavantage')
            av.setDataSize(size)
            av.setSource(datafreq)
            
            self.data = av.getData(symbol)
            self.hasdata = True
            
            return(True)
            
        except Exception as err:
            errstr = "Getting data from Alpha Vantage failed! {}"
            logger.error(errstr.format(err.args[0]))
            raise
            
