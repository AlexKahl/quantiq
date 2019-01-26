# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
@title: Py script generic title
@author: vcl2311
@date: Sat Jan 26 16:38:17 2019
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

from raphka.classes import AlphaVantage

avcon = AlphaVantage()
avcon.datasize = "full"
avcon.source = "Intraday"
ts = avcon.getData("MSFT")


ts['AdjustedClose'].plot()
