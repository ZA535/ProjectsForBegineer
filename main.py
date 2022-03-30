# from test_file import Box
from msilib.schema import File

import json

file_data = ''
with open("user_account_details.txt", 'r') as nf:
    file_data = nf.read()
lines = file_data.split('\n')
user_data = []
for line in lines:
    d = line.split(',')
    user_data.append({
        'name': d[0],
        'age': d[1],
        'year': d[2]
    })
json_data = json.dumps(user_data)
# print(json_data)
with open('user_account_details.json', 'w') as nf:
    nf.write(json_data)
dict_js = None
with open('user_account_details.json', 'r') as nf:
    jf = nf.read()
    dict_js = json.loads(jf)

print(dict_js[3])
print(dict_js[2])



# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
