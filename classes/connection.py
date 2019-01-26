# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
@title: Py script generic title
@author: vcl2311
@date: Sat Jan 26 20:08:43 2019
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

from raphka.classes import EquityStatic,AlphaVantage
from raphka.settings import config

logger = config.logging.getLogger('debug')

class Connection():
    
    """Connection: wrapper class to get connections to data pools
    
    Description:
    ------------------
    
    Inputs/variables:
    ------------------
        
    
    methods:
    ------------------
    get_connection: this methode is used to fetch any connection obj using
                    the only parameter conntype        
    """
    
    alphavantage = None
    equitystatic = None

    
    def get_connection(self,conntype="AlphaVantage"):
        
        try:
            
            if (conntype.lower() == "alphavantage"):
    
                if self.alphavantage is None:
                    self.alphavantage = AlphaVantage()
                
                return(self.alphavantage)
                
            elif (conntype.lower() == "equitystatic"):
                
                if self.equitystatic is None:
                    self.equitystatic = EquityStatic().getData()

                return(self.equitystatic)
            
            else:
                raise ValueError("We don't know of any other server!")

        except Exception as err:
            errstr = "Database class error: {}"
            logger.error(errstr.format(err.args[0]), exc_info=True)
            raise
            


