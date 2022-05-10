from http.server import HTTPServer , SimpleHTTPRequestHandler
import urllib.request

HOST = "127.0.0.2"
PORT = 8080

class MyProxyServer(SimpleHTTPRequestHandler):

    def __init__(self , *args , **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type" , "text/html")
        self.end_headers()
        url = self.path
        self.copyfile(urllib.request.urlopen(url) , self.wfile)


server = HTTPServer( (HOST , PORT) , MyProxyServer)
server.serve_forever()
print("My Server has started ...")
server.serve_close()
print("My is closed now ...")