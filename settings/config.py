# -*- coding: utf-8 -*-
"""
@title: raphka set up script
@author: Alexander Kahl
@date: Mon Sep  3 08:07:47 2018
@version: 0.01
@description: settings file for raphka package
@Details: this file will contain all libraries used in our repository.
          Furthermore the general logging library will be configured for our
          needs so that each source file in the repository can work with the 
          same logging set up!
@external file paths:
@key inputs:
@key variables:
@external sources:
@key output:
@comment: we still need to add a file logger to config 
"""

alphavantage_settings = {'api-key' : "BP1UK2Z1G6M6B3W9"}


logging.config.dictConfig({
    'version': 1,
    
    'disable_existing_loggers': False,  # this fixes the problem
    
    'formatters': {
        'standard': {
            'format': """%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s (No. %(lineno)d): %(message)s'"""

        },
        'simple': {
            'format': """%(asctime)s - %(name)s - %(levelname)s - %(message)s'"""
        },

    },
    'handlers': {
            
        'default': {
            'level':'ERROR',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
                
        'console_debug': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
                
         'console_info': {
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        }
            
        'backtest_file': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'Z:/backtestlog.log',
            'maxBytes': 5000, 
            'backupCount': 3,
            'formatter': 'standard'
        }
                         
    },
    'loggers': {
            
        '': {
            'handlers': ['default'],
            'level': 'ERROR',
            'propagate': True
        },
        'backtest': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
                
        'portfolio': {
            'handlers': ['console_info'],
            'level': 'INFO',
            'propagate': True
        },
                
        'debug': {
            'handlers': ['console_debug'],
            'level': 'DEBUG',
            'propagate': True
        }        
    }
})
    