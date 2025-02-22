import json

with open('4week/sample-data.json', 'r') as file:
    data = json.load(file)

interfaces = []
for item in data['imdata']:
    interface = item['l1PhysIf']['attributes']
    interfaces.append({
        "DN": interface["dn"],
        "Description": "",  
        "Speed": interface["speed"],
        "MTU": interface["mtu"]
    })


print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

interface = iter(interfaces)
print(next(interface))
print(next(interface))
print(next(interface))