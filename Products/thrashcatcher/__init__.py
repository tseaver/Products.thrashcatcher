from App.ZApplication import connection_open_hooks
from ZServer.DebugLogger import log as trace_log

from threading import local
_data = local()

def onConnectionOpened(conn):
    _data.loads_before, _data.stores_before = conn.getTransferCounts()

    def _onConnectionClosed():
        _data.loads_after, _data.stores_after = conn.getTransferCounts()
        loaded = _data.loads_after - _data.loads_before
        stored = _data.stores_after - _data.stores_before
        env = conn.getDebugInfo()[0]
        method = env['REQUEST_METHOD']
        path = env['PATH_INFO']
        qs = env.get('QUERY_STRING')
        if qs:
            info = '%s %s?%s' % (method, path, qs)
        else:
            info = '%s %s' % (method, path)
        trace_log('L', 0, '%10d (%s)' % (loaded, info))
        trace_log('S', 0, '%10d' % stored)
        
    conn.onCloseCallback(_onConnectionClosed)

def initialize(context):

    connection_open_hooks.append(onConnectionOpened)

