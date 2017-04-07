"""
@author: Wenchang Yang (yang.wenchang@uci.edu)
"""

import xarray as xr
from .util import num2time
from .datalib_manager import get_dataurl

def _get_time_dim_name(ds):
    return [s for s in ['T', 'time'] if s in list(ds.dims)][0]
def _get_data_var_name(ds, index=0):
    return [s for s in list(ds.data_vars)][index]

class Ingrid(object):
    '''ingrid'''
    def __init__(self, *args, server=None):
        '''Construct data url from args and server.

            args: string, or a list of strings, e.g.
                'http://iridl.ldeo.columbia.edu/SOURCES/.NASA/.GPCP/.V2p2/.satellite-gauge/.prcp'
                or 'gpcp',
                or ['SOURCES', '.NASA', '.GPCP', '.V2p2', '.satellite-gauge', '.prcp'],
                or 'SOURCES .NASA .GPCP .V2p2 .satellite-gauge .prcp'.

            server: string, e.g. 'http://iridl.ldeo.columbia.edu'.

        For more information on the arguments, please see pyingrid.datalib_manager.get_dataurl. '''
        dataurl = get_dataurl(*args, server=server)
        self._dataflow = [dataurl,]

    def __repr__(self):
        return str(self.__class__) + '\n' \
            + '\n\t'.join(self._dataflow)

    def do(self, cmd):
        '''Apply an Ingrid operation.

            cmd: string of Ingrid command.
                e.g. 'T (Jan 1980) (Dec 2009) RANGE' '''
        self._dataflow.append(cmd)
        return self

    def undo(self):
        '''Cancel the last Ingrid operation.'''
        if len(self._dataflow)>1:
            self._dataflow.remove(self._dataflow[-1])
        else:
            print('[Warning]: Ingrid does not contain any operations.')
        return self

    def to_url(self):
        '''Convert to a url representation.'''
        return '/'.join(self._dataflow).replace(' ', '%20')

    def to_dataset(self, **kw):
        '''Convert to an xarray Dataset.'''
        datafile = self.to_url()
        if datafile.endswith('.nc') or datafile.endswith('/dods'):
            pass
        elif datafile.endswith('/'):
            datafile += 'dods'
        else:
            datafile += '/dods'
        try:
            ds = xr.open_dataset(datafile, **kw)
        except ValueError:
            ds = xr.open_dataset(datafile, decode_times=False, **kw)
            tname = _get_time_dim_name(ds)
            if hasattr(ds[tname], 'units'):
                tunits = ds[tname].units
                ds[tname].values = num2time(ds[tname].values, units=tunits)
                ds[tname].attrs['old units'] = ds[tname].attrs.pop('units')
        except OSError:
            print('[OSError]: file not found: {}'.format(self.to_url()))
            return
        return ds

    def to_xarray(self, **kw):
        '''Convert to an xarray DataArray.'''
        ds = self.to_dataset(**kw)
        dname = _get_data_var_name(ds)
        return ds[dname]

    def look(self, **kw):
        '''Look at the Ingrid dataset structure.'''
        ds = self.to_dataset(**kw)
        try:
            ds.info()
        except:
            print(ds)

    def trend(self, dim='T'):
        '''Calculate linear trend along a given dimension dim.'''
        cmd = '''dup [{dim}]detrend-bfl sub dup {dim}(last)VALUES exch {dim}(first)VALUES sub'''.format(dim=dim)
        self._dataflow.append(cmd)
        return self
