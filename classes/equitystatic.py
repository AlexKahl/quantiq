# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
@title: Py script generic title
@author: vcl2311
@date: Sat Jan 26 18:05:57 2019
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


from raphka.settings import config
logger = config.logging.getLogger('debug')


class EquityStatic():
    
    data = None
    
    def getData(self):
        
        try:
            
            if self.data is None:
                logger.info("reading statics from file!")
                data = config.pd.read_excel(config.eq_static_file['path'],
                                            sheet_name='data')
                data.set_index('symbol',inplace=True)
                self.data = data
                  
            return(self.data)

        except Exception as err:
            errstr = "getdata failed: {}"
            logger.error(errstr.format(err.args[0]), exc_info=True)
            raise
            

