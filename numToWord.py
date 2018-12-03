maps = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}

ip = 341

# print(len(str(ip)))

a = ip % 10
# print(a)

for i in range(len(str(ip))):
    a = ip % 10
    if a in maps.keys():
        print(maps[a])
    ip = int(ip/10)

# print(divmod(ip, 10))
#
# print(type(divmod(ip, 10)))

# for i in len(ip):
#     print(i)
