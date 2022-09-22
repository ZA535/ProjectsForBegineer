import json
from msilib.schema import File

data = ''
with open('friends.txt', 'r') as df:
    data = df.read()

lines = data.split('\n')
student_record = []
for line in lines:
    d = line.split('?')
    student_record.append({
        'Name': d[0],
        'Registeration #': d[1],
        'Year': d[2],
        'University': d[3]

    })
    jsonData = json.dumps(student_record)
with open("my_friend_As_Json_form.json", 'w') as nf:
    nf.write(jsonData)
dic = None
with open("my_friend_As_Json_form.json", 'r') as lf:
    some = lf.read()
    dic = json.loads(some)

print(dic[1])


# commerr add
