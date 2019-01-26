# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
@title: Py script generic title
@author: vcl2311
@date: Sat Jan 26 18:35:28 2019
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


from raphka.classes import EquityStatic

# singleton class
eqs = EquityStatic()

data = eqs.getData()
# not reading file again
data2 = eqs.getData()


statics = data.loc['JPM']


statics.