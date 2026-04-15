import http.server
import ssl
import sys
from pathlib import Path

def start_https_server(port=8443, cert_path="aluno.crt", key_path="aluno.key", bind="0.0.0.0"):
    cert_file = Path(cert_path)
    key_file = Path(key_path)

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=str(cert_file), keyfile=str(key_file))

    handler = http.server.SimpleHTTPRequestHandler
    server = http.server.HTTPServer((bind, port), handler)
    server.socket = context.wrap_socket(server.socket, server_side=True)
    
    print(f"Servidor HTTPS")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServidor parado")
        server.server_close()
        sys.exit(0)

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8443
    cert = sys.argv[2] if len(sys.argv) > 2 else "aluno.crt"
    key = sys.argv[3] if len(sys.argv) > 3 else "aluno.key"
    bind = sys.argv[4] if len(sys.argv) > 4 else "0.0.0.0"
    
    start_https_server(port, cert, key, bind)
