# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
@title: Py script generic title
@author: vcl2311
@date: Sat Jan 26 20:51:20 2019
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



from raphka.classes import Equity,Connection


eq = Equity("MSFT",connection=Connection())
eq.getData()



eq.data.head()
eq.name
eq.industry
