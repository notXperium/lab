from secret import SSID, KEY
import network, time, sys
import socket
import json


wifi = network.WLAN()
wifi.active(True)

wifi.disconnect()
wifi.connect(SSID, KEY)
for i in range(30):
    if wifi.isconnected():
        break
    print(i, wifi.status())
    time.sleep(0.5)
if not wifi.isconnected():
    sys.exit()
print(wifi.ipconfig("addr4"))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("", 80))

server.listen(5)

while True:
    client, _ = server.accept()

    request = b""
    while b"\r\n\r\n" not in request:
        chunk = client.recv(1024)
        if not chunk:
            break
        request += chunk

    request_line = request.decode("utf-8").split("\r\n")[0].split(" ")

    data = {}

    if "favicon.ico" in request_line[1]:
        client.close()
        continue

    if request_line[0] == "GET":

        if all(p in request_line[1] for p in ("/winkel", "pan", "tilt")):
            path, query = request_line[1].split("?", 1)

            data = {"path": path, "pan": None, "tilt": None}

            if query:
             for pair in query.split("&"):
                 key, value = pair.split("=")
                 if value.isdigit():
                    if key in data: data[key] = int(value)
        

    if len(data):
        data_json = json.dumps(data)

        res = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json; charset=utf-8\r\n"
            f"Content-Length: {len(data_json.encode('utf-8'))}\r\n"
            "\r\n"
            f"{data_json}"
        )
    else:
         res = (
            "HTTP/1.1 422 Unprocessable Entity\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "\r\n"
            "<h1>Unprocessable Entity</h1>"
        )
         
    try:
        client.sendall(res.encode("utf-8"))
    except OSError:
        pass
    finally:
        client.close()






