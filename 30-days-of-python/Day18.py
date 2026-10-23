import re

txt = 'I love to teach python and javaScript'


match = re.match('I love to Teach', txt, re.I)
print(match)

span = match.span()
print(span)
start, end =span
sub = txt[start:end]
print(sub)

txt2 = '''Python is the most beautiful Language that a human being has ever created.
I recommend python for a first programming language'''

m = re.search("first", txt2, re.I)
print(m)

st, en = m.span()
sb = txt2[st:en]
print(sb)

m2= re.findall("language", txt2, re.I)
print(m2)

print(re.findall("[Pp]ython", txt2))
print(re.findall("Python|python",  txt2))

print(re.sub("[Pp]ython", "Java", txt2))

txt3 = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches3 = re.sub('%', '', txt3)
print(matches3)

print(re.split("\n", matches3))

