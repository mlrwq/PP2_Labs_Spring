import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print(80*"=")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

for i in data["imdata"][:3]:
    attributes = i["l1PhysIf"]["attributes"]
    print("{:<50}{:<22}{:<10}{:<10}".format(attributes["dn"], attributes["descr"], attributes["speed"], attributes["mtu"]))