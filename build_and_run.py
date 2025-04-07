import http.server
import os
import socketserver
from app import build_site

PORT = 8080
web_dir = os.path.join(os.path.dirname(__file__), "build")
Handler = http.server.SimpleHTTPRequestHandler

if __name__ == "__main__":
    build_site()
    os.chdir(web_dir)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"serving http://localhost:{PORT}")
        httpd.serve_forever()
