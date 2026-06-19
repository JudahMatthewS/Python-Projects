judah = {"Name":"Judah","Age":13,"Skills":["Python","C"],"Atk":300,"def":1000,"marks":{ "Tamil":70"English":80,"Distraction":100}}

print(judah["Age"])
print(judah.items())
print(judah.keys())
print(judah.values())

for i in judah:
    print(i, judah[i])
