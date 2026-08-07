# kmh = [40, 60, 80, 100, 120]
#
# mph = []
#
# for i in kmh:
#    mph.append(i/1.61)
#
# print(mph)

kmh = [40, 60, 80, 100, 120]

''' Cria uma função map() '''
mph2 = list(map(lambda x: x/1.61, kmh))
print(mph2)