import requests

r = requests.get('https://esi.evetech.net/latest/universe/structures/?datasource=tranquility&filter=market')
i = r.json()
for value in i:
    print("Jita ID = " + str(value))

systemlist = []
id = None
system_get = input('Enter system name: ')
r = requests.get('https://esi.evetech.net/latest/search/?categories=solar_system&search='+system_get+'&strict=true')
i = r.json()
for key, value in i.items():
    id = str(value[0]).strip()
if id != None:
    r = requests.get('https://esi.evetech.net/latest/industry/systems/?datasource=tranquility')
    for i in r.json():
        systemlist.append(i)
    for system in systemlist:
        for key, value in system.items():
            if str(key) == "solar_system_id" and str(value) == id:
                print("\n"+system_get)
                print("System ID: "+str(value)+"\n")
                for key, value in system.items():
                    if key == "cost_indices":
                        for v in value:
                            for key, value in v.items():
                                if key == "cost_index":
                                    print(str(key)+" -> "+str(value))
                                else:
                                    print(str(key)+" -> "+str(value)+"\n")