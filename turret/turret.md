# Turm

## Was ist das?
Ich will wieder mit Mikrocontrollern arbeiten und hab mir einen ESP32-S3 zugelegt.
Als erstes richtiges Projekt auf meinem Lernweg möchte ich ein Zielerfassungssystem bauen.
Geplant ist ein Turm, der sich auf zwei Achsen bewegt und mithilfe eines selbst trainierten neuronalen Netzes ein Ziel erfasst und festhält.

## Dokumentation

### LED mithilfe eines Potentiometers steuern

<img src="../Assets/turret/LED-poti.jpeg" width="500" alt="LED auf dem Steckbrett, gesteuert über ein Potentiometer">

**Code:** [Licht](./basics/light.py)

### Servo mithilfe eines Potentiometers steuern

<img src="../Assets/turret/servo-poti.jpeg" width="500" alt="Servo folgt dem Potentiometer">

**Code:** [Servo](./basics/servo.py)

### Die Webcam erkennt Rot

<img src="../Assets/turret/rot-kamera.png" width="500" alt="Webcam-Bild mit rotem Deckel">
<img src="../Assets/turret/rot-maske.png" width="500" alt="Maske: nur der Deckel bleibt weiß">

Oben das Kamerabild, unten die Maske: Jeder Pixel, der meine Regel für Rot erfüllt, wird weiß, alles andere schwarz.

<img src="../Assets/turret/rot-kamera-fadenkreuz.png" width="500" alt="Zielerfassung">

Aus allen Punkten des roten Objekts Mittelpunkt berechnen. Letzte bekannte Position wird gemerkt

**Code:** [Erkennung](./basics/ball.py)

### 2 Achsen mithilfe von einem Joystick steuern

<img src="../Assets/turret/servos-joystick.jpeg" width="500" alt="Servos folgen dem Joystick">

Hatte leider nur einen Servo, neue sind bestellt. Prinzip ist das selbe.
Als Ersatz baute ich ein LCD Display an, welches die Winkel von Pan & Tilt ausgibt


<img src="../Assets/turret/servos-joystick-lcd.jpeg" width="500" alt="LCD zeigt pan und tilt Winkel">

Servos sind angekommen!

<img src="../Assets/turret/servos-joystick2.jpeg" width="500" alt="Joystick steuert 2 Achsen">


**Code:** [Achsen](./basics/axles.py)

### ESP32 als Webserver

<img src="../Assets/turret/api-web.png" width="500" alt="Basic API">

Endpoint `/winkel` nimmt Parameter `pan` und `tilt`

**Code:** [API](./basics/api.py)

## Steuerung und API als Klassen

<img src="../Assets/turret/api-control.jpeg" width="500" alt="API Control">

Klassen [API](./classes/api.py) und [Turret](./classes/turret.py) werden in [main.py](./main.py) zusammengeführt. Servos werden über Anfrage im Webbrowser gesteuert.

