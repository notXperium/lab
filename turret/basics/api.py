from turret.secret import SSID, KEY
import network, time, sys
import json, re
import socket


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

    request_line = [r.strip() for r in request.decode("utf-8").split("\r\n")[0].split(" ") if not r.strip().startswith("HTTP")]
    pattern = r"^(/winkel)\?pan=(\d+)&tilt=(\d+)$"
    data = {}

    if len(request_line) < 2 or "favicon.ico" in request_line[1]:
        client.close()
        continue

    if request_line[0] == "GET":

        m = re.search(pattern, request_line[1])

        if m:
            path = m.group(1)
            pan = int(m.group(2))
            tilt = int(m.group(3))
        
            if 0 <= pan <= 180 and 0 <= tilt <= 180:
                data = {"path": path, "pan": pan, "tilt": tilt}
                

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
         error = json.dumps({"Code": "422", "Error": "Unprocessable Entity"})
         res = (
            "HTTP/1.1 422 Unprocessable Entity\r\n"
            "Content-Type: application/json; charset=utf-8\r\n"
            f"Content-Length: {len(error.encode('utf-8'))}\r\n"
            "\r\n"
            f"{error}"
        )
         
    try:
        client.sendall(res.encode("utf-8"))
    except OSError:
        pass
    finally:
        client.close()






