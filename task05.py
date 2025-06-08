a = "{b} + {c} = {d}"

b =int(input(":"))
c =int(input(":")) #float ham ishlatish mumkin
d = c + b

x = a.format( b = b , c = c , d=d)
print(x)