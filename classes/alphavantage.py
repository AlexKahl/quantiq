# -*- coding: utf-8 -*-
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


import raphka
from raphka.settings import config

av_settings = config.alphavantage_settings

class AlphaVantage():

    def __init__(self,
                 apikey = av_settings['api-key'],
                 source = 'Daily',
                 fields = av_settings['eodfields'],
                 intradayfreq = '1min',
                 datasize ='full'):

    
        """AlphaVantage: object instantiation of class Alpha Vantage
        
        Description:
        ------------------
        This function creates an instance of class AlphaVatange. It will be used to 
        load Alpha Vantage data.
        
        Inputs/variables:
        ------------------
        
        apikey : string api-key
        source: string indicating what data to be retrieved
        fields: list of fields to be retrieved
        intradayfreq = string indicating frequency
        datasize: string indicating length of history
    
        methods:
        ------------------
        getData: fetching data for given ticker          
        
        """
                
        self.apikey = apikey
        self.__source = source
        self.fields = fields
        self.intradayfreq = intradayfreq
        self.__datasize = datasize

    def setSource(self,frequency):
        
        try:
            if (frequency not in ['Daily','Intraday']):
                raise ValueError("wrong frequency")
            self.source = frequency    
            return (True)
        except Exception as err:
            errstr = "set frequency! {}"
            logger.error(errstr.format(err.args[0]))
            raise

    def setDataSize(self,size):
        
        try:
            self.__datasize = size    
            return (True)
        except Exception as err:
            errstr = "setting size! {}"
            logger.error(errstr.format(err.args[0]))
            raise



    def getData(self,symbol,source=None,interval=None,
                datasize=None,convertdatetime=True,convertnumeric=True):
        
        """getData method:fetching data from alpha vantage
        
        Description:
        ------------------
        Loadind data from Alpha vantage method
        
        Inputs/variables:
        ------------------
        
        symbol : string
        source: string indicating what data to be retrieved
        interval = string indicating frequency
        datasize: string indicating length of history
    
        methods:
        ------------------
        getData: fetching data for given ticker          
        
        """
        try:
        
            if (source is None):
                source = self.__source
            
            fields = self.fields
            
            if (interval is None):
                interval = self.intradayfreq
            if (datasize is None):
                datasize = self.__datasize

            # setting parameters for different sources
            if (source.lower()=='daily'):
                function = av_settings['eodfunction']
                jsonstr = "Time Series (Daily)"
                dateconstr = "%Y-%m-%d"
                
            elif (source.lower()=='intraday'):                
                function = av_settings['intradayfunction']
                jsonstr = "Time Series ({})".format(interval)
                fields = av_settings['intradayfields']
                dateconstr = "%Y-%m-%d %H:%M:%S"
                
            url = av_settings['url']
            api_key = self.apikey
            
            params = {"function": function, "symbol": symbol,
                      "outputsize": datasize,"apikey": api_key}
            
            if (source.lower() == "intraday"):
                params['interval'] = interval
            
            page = requests.get(url, params = params)
            data = page.json()
            
            if 'Error Message' in data.keys():
                raise ValueError(data['Error Message'])
            
            data = data[jsonstr]
            data = pd.DataFrame.from_dict(data,orient="index")
            data.columns = fields
            
            if (convertdatetime):                
                dateidx = [datetime.strptime(idx,dateconstr) 
                            for idx in data.index]
                data.index = dateidx
            
            if (convertnumeric):
                data = data.astype(float)
            
            return data
                        
        except Exception as err:
            errstr = "Getting data from Alpha Vantage failed! {}"
            logger.error(errstr.format(err.args[0]))
            raise
            