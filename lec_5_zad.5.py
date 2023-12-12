name = "Shkilsemen" 
names = name.upper()
names1 = name.lower()
symbol_codes = [ord(name) for symbol in names]
symbol_codes1 = [ord(name) for symbol in names1]
print(sum(symbol_codes)) 
print(sum(symbol_codes1 ))