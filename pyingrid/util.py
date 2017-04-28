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

def ingrid_sel_range(t_start, t_end, dim='T'):
    '''Ingrid commands that select a time range,
    e.g. t_start='Jan 1980', t_end='Dec 2009'. '''
    cmd = '{}({})({})RANGE'.format(dim, t_start, t_end)
    return cmd

def ingrid_sel_season(seasonName, dim='T'):
    '''Ingrid commands that specify a season, e.g. 'Mar-May'. '''
    cmd = '{}({})seasonalAverage'.format(dim, seasonName)
    return cmd

def ingrid_climatology(season=None, time_range=None, dim='T'):
    '''Ingrid commands that calculate climatology of a specified season (e.g. Mar-May)
    over a specified time range (e.g. Jan 1980 to Dec 2009). '''
    if season is None:
        season = 'Jan-Dec'
    month_start = season.split('-')[0]
    month_end = season.split('-')[-1]
    if time_range is None:
        time_range = (month_start+' 1980', month_end+' 2009')
    cmd = '{dim}({season})seasonalAverage {dim}({T_start})({T_end})RANGE [{dim}]average'.format(
        dim=dim, T_start=time_range[0], T_end=time_range[-1], season=season
    )
    return cmd

def ingrid_trend(dim='T'):
    '''Ingrid commands that calculate linear trend.'''
    cmd = '''dup [{dim}]detrend-bfl sub dup {dim}(last)VALUE exch {dim}(first)VALUE sub'''.format(dim=dim)
    return cmd
