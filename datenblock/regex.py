import re
inp = "/winkel?pan=90&tilt=45"

print(re.search(r"pan=\d+", inp))


for text in ["/winkel?pan=90", "/winkelpan=90", "/winkepan=90"]:
    print(text, "->", re.search(r"^/winkel\?pan=\d+$", text))

m = re.search(r"^pan=(\d+)$", "pan=90")
print(m.group(0))
print(m.group(1))
print(type(m.group(1)))

pattern = r"^/winkel\?pan=(\d+)&tilt=(\d+)$"

tests = [
    "/winkel?pan=90&tilt=45",  
    "/winkel?pan=5&tilt=170",    
    "/winkel?pan=abc&tilt=45",   
    "/winkel?pan=90",            
    "/winkel?pan=90&tilt=45xx",  
]

for i in tests:
    m = re.search(pattern, i)
    if m:
        print(m.group(1), m.group(2))
    else:
        print(None)