st = set()

st = {1, 4, 5, 12, 56, 7, 45, 6, 9}
print(len(st))
print(5 in st)
x = 5 in st
if not x:
    st.add(5)

st.update([67, 68, 69])
st.remove(1)
st.pop()

lst = [1, 2, 3]
set2 = set(lst)

st3 = st.union(set2)
print(st3.intersection(st))
st.difference(set2)

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()

x = 0
for i in words:
    amount = words.count(i)
    if amount == 1:
        x+=1
        print(i)

print(x)
