import http.server
import ssl
import sys

server_address = ('0.0.0.0', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
print("Before wrapping the socket in SSl")
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile="server.pem",
                               keyfile="key.pem",
                               ssl_version=ssl.PROTOCOL_SSLv23)
print("After wrapping the socket in SSL")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nClosing the server......")
    httpd.socket.close()
    sys.exit(0)

