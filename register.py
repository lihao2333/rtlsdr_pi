import urllib
import urllib2

url = "http://10.112.21.187:8000/sdrpub/register?name=sdr_02&loc_x=100&loc_y=200"

req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = res_data.read()
print res
