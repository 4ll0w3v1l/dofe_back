# import requests
# import json
#
# payload_reg = {'email': '222@224.666', 'password': '123'}
# cookie = {
#     'Authorization': '3243873f139acdbdfedff86249facabcd9823f474aa1b92b0adb7e64da844d221ed0a2518ad7d7c55ac3c637f5beb2e53b554a06e7b7efc45892f2e744ad8cf2'}
# # payload_get_acc = {'uid': 1}
# #
# # print(payload_reg['email'])
# #
# #
# # requests.post('http://127.0.0.1:5000/account/register', json.dumps(payload_reg))
# r = requests.get('http://127.0.0.1:5000/account/1', cookies=cookie)
#
#
# print(r.text)
# # print(r.status_code)
#
#
def dirReduc(arr):
    cycle = [0, 0]
    i = 0
    while True:
        if i >= len(arr) - 1:
            i = 0
        if cycle[1] >= len(arr):
            break

        if (arr[i] == 'NORTH' and arr[i + 1] == 'SOUTH') or (arr[i + 1] == 'NORTH' and arr[i] == 'SOUTH'):
            arr.pop(i), arr.pop(i)
            cycle[0] += 1
            cycle[1] = 0
            i -= 1

        if (arr[i] == 'WEST' and arr[i + 1] == 'EAST') or (arr[i + 1] == 'WEST' and arr[i] == 'EAST'):
            arr.pop(i), arr.pop(i)
            cycle[0] += 1
            cycle[1] = 0
            i -= 1

        cycle[1] += 1
        i += 1

    return arr


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))


# ['NORTH', 'EAST']
# ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH']
# ['EAST', 'NORTH', 'EAST', 'SOUTH']
# ['SOUTH', 'SOUTH', 'EAST', 'WEST', 'SOUTH', 'NORTH', 'EAST', 'SOUTH', 'WEST', 'NORTH', 'NORTH', 'WEST', 'WEST', 'WEST']
