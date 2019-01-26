# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
@title: Py script generic title
@author: vcl2311
@date: Sat Jan 26 20:24:36 2019
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

from raphka.classes import Connection


conn = Connection()

eqs = conn.get_connection('equitystatic')

av = conn.get_connection('alphavantage')

