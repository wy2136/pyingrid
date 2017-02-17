"""
@author: Wenchang Yang (yang.wenchang@uci.edu)
"""
import numpy as np
import pandas as pd

def num2time(num,units):
    '''Convert expression of time from "months since yyyy-mm-dd" into pandas DatetimeIndex.'''
    if units.lower().startswith('months since'):
        # get the yyyy-mm (or yyyy-m) string from units
        yyyy_mm = '-'.join( units.split()[2].split('-')[:2] )
        period0 = pd.Period(yyyy_mm)
    else:
        print('\n**** units must be: months since yyyy-mm-dd.')
        return
    return pd.PeriodIndex(period0 + np.floor(num).astype('int'))\
        .to_timestamp()
