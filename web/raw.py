import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("example.com", 80))


anfrage = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n".encode("utf-8")

sock.sendall(anfrage)
chunks = []
while True:
    chunk = sock.recv(2048)

    if not chunk:  
        break

    chunks.append(chunk)

print(b''.join(chunks).decode("utf-8").split("\r\n\r\n")[0])


zeile = "HTTP/1.1 301 Moved Permanently"

version, code, text = zeile.split(" ", 2)
print(f"{version}\n{int(code)}\n{text}")
sock.close()