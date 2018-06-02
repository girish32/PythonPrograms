import urllib3

url='http://oasis.pjm.com/doc/projload.txt'
filename='pjmload.xls'
connection_pool = urllib3.PoolManager()
resp = connection_pool.request('GET',url )
f = open(filename, 'wb')
f.write(resp.data)
f.close()
resp.release_conn()