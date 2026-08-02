import http.server
import socketserver
import os, errno

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(ROOT_DIR)

SERVER_PORT = 1663

Handler = http.server.SimpleHTTPRequestHandler

def check_port():
    global SERVER_PORT
    while True:
        try:
            httpd = socketserver.TCPServer(("", SERVER_PORT), Handler)
            httpd.server_close()
            return SERVER_PORT
        except OSError as e:
            if e.errno == errno.EADDRINUSE:
                print(f"Port {SERVER_PORT} is busy, trying next...")
                SERVER_PORT += 1
            else:
                raise
            
def run():
    port = check_port()
    os.chdir(BASE_DIR)
    with socketserver.TCPServer(("", port), Handler) as httpd:
        #subprocess.run([sys.executable, os.path.join(ROOT_DIR, "generate_assets.py")])
        print(f"Server started on: http://localhost:{port}")
        httpd.serve_forever()


if __name__ == "__main__":
    run()