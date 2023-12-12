name = "Shkilsemen" 
nstr = "_".join(name) 
print(nstr) 
 
nameup = nstr.upper() 
print(nameup) 
 
symbol_codes = [ord(symbol) for symbol in nameup] 
print(symbol_codes ) 
 
namelow = nstr.lower() 
print(namelow) 
 
symbol_codes1 = [ord(symbol) for symbol in namelow] 
print(symbol_codes1) 
 
a = min(symbol_codes) 
b = max(symbol_codes) 
print(a, b) 
 
c = min(symbol_codes1) 
d = max(symbol_codes1) 
 
print(c, d)