#!"C:\Winpython\python-3.8.5.amd64\python.exe"

from mod_python import apache
def handler(req):
    req.content_type = 'text/plain'
    req.send_http_header()
    req.write("Hello World!")
    return apache.OK
