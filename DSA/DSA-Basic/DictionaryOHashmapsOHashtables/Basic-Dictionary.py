# Implementing basic dictionary in python.
dic = {
    "BWU/BCA/22/394": "AGNIK ROY",
    "BWU/BCA/22/395": "JEETSEKHAR DEO",
    "BWU/BCA/22/420": "SHIBHAM GUPTA",
    "BWU/BCA/22/384": "SRISTHI SARKER",
    "BWU/BCA/22/408": "PRYIA NIYA",
    "BWU/BCA/22/400": "SAYANDIP XO",
}
print("Code-1")
print(dic)

print("Code-2")

print(type(dic))

print("Code-3")

print(dic["BWU/BCA/22/384"])

print("Code-4")

dic["BWU/BCA/22/400"] = "SudhirVhi"
print(dic)

print("Code-5")

del dic["BWU/BCA/22/420"]
print(dic)

print("Code-6")

print(dic.keys())
print("Code-7")
print(dic.values())
