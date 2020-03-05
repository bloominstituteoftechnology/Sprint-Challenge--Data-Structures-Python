duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# xlist = []
# ylist = []
cache = LRUCache(10000)

# for x in range(len(names_1)):
#     cache.set(x, names_1[x])
# for x in range(len(names_1)):   
#     xitems = cache.get(x)
#     xlist.append(xitems)
# for y in range(len(names_2)):
#     cache.set(y, names_2[y])
# for y in range(len(names_2)):
#     yitems = cache.get(y)
#     ylist.append(yitems)

# for i in xlist:
#     if i in ylist:
#         duplicates.append(i)

for x in range(len(names_1)):
    cache.set(names_1[x], names_1[x])


#input a dictionary of one name list, with name1key : name1value
#if i in 2ndlist == name1
for i in names_2:
    if cache.get(i) == i:
    #append
        duplicates.append(i)