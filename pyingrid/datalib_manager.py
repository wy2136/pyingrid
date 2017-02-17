"""
@author: Wenchang Yang (yang.wenchan@uci.edu)
"""

from . import datalib

def listdata():
    '''list all datasets in the datalib.'''
    return [s for s in dir(datalib) if not s.startswith('_')]

def findata(dname=None):
    '''find data according to the name'''
    datalist = [s for s in dir(datalib) if not s.startswith('_')]
    if dname is None:
        return datalist
    else:
        return [s for s in datalist if dname in s]

def get_dataurl(*args, server=None):
    '''Construct data url from args and server.

        args: string, or a list of strings, e.g.
            'http://iridl.ldeo.columbia.edu/SOURCES/.NASA/.GPCP/.V2p2/.satellite-gauge/.prcp'
            or 'gpcp',
            or ['SOURCES', '.NASA', '.GPCP', '.V2p2', '.satellite-gauge', '.prcp'],
            or 'SOURCES .NASA .GPCP .V2p2 .satellite-gauge .prcp'. '''

    if len(args) < 1:
        dataurl = ''
    elif len(args) > 1 : # more than one positional args
        dataurl = '/'.join( ['/'.join( arg.split() ) for arg in args] )
    elif len(args) == 1 and ' ' in args[0]: # only one positional arg that contains space
        dataurl = '/'.join(args[0].split())
    else: # only one positional args
        try: # the single positional arg is a dataname stored in the datalib
            dataurl = getattr(datalib, args[0])
        except AttributeError: # the single positional arg is the dataurl
            dataurl = args[0]
    if server is not None:
        dataurl = '/'.join([server, dataurl])

    return dataurl
