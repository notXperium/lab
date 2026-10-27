from secret import SSID, KEY
import network, socket
import json, re
import time

class API:
    def __init__(self, on_aim):
        self.on_aim = on_aim

    def connect(self):
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
            raise RuntimeError("connection error")
        print(wifi.ipconfig("addr4"))

    def run(self):
        self.connect()

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("", 80))
        server.listen(5)


        while True:
            client, _ = server.accept()
            req = b""

            while b"\r\n\r\n" not in req:
                chunk = client.recv(1024)
                if not chunk:
                    break
                req+=chunk

            req_line = [r.strip() for r in req.decode("utf-8").split("\r\n")[0].split(" ") if not r.startswith("HTTP")]
            pattern = r"^(/winkel)\?pan=(\d+)&tilt=(\d+)$"
            data = {}
            error = {"code": 400, "status": "Bad Request"}

            if len(req_line) < 2 or "favicon.ico" in req_line[1]:
                client.close()
                continue

            if req_line[0] == "GET":
              m = re.search(pattern, req_line[1])

              if m:
                  path = m.group(1)
                  pan = int(m.group(2))
                  tilt = int(m.group(3))

                  try:
                    self.on_aim(pan, tilt)
                    data = {"path": path, "pan": pan, "tilt": tilt}
                  except ValueError as e: error.update(code=422, status="Unprocessable Entity", message=str(e))
                      

            if len(data):
                d_json = json.dumps(data)  

                res = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: application/json; charset=utf-8\r\n"
                        f"Content-Length: {len(d_json.encode('utf-8'))}\r\n"
                        "\r\n"
                        f"{d_json}"
                    )
            else:
                e_json = json.dumps(error)
                res = (
                    f"HTTP/1.1 {error['code']} {error['status']}\r\n"
                    "Content-Type: application/json; charset=utf-8\r\n"
                    f"Content-Length: {len(e_json.encode('utf-8'))}\r\n"
                    "\r\n"
                    f"{e_json}"
                )

            try:
                client.sendall(res.encode("utf-8"))
            except OSError:
                pass
            finally:
                client.close()
