dic = {"aaa":"123456","bbb":"888888","ccc":"333333"}

ID = input()
password = input()
if ID not in dic:
    print("Wrong User")
if ID in dic and dic[ID] != password:
    print("Fail")
if ID in dic and dic[ID] == password:
    print("Success")