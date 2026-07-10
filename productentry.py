products = 4

entry = []
for i in range(products):
    item = []
    name = input("Enter product name:")
    category = input("Enter category name:")
    qty = int(input("Enter quantity: "))
    entry.append([name,category,qty])

print(entry)

'''entry.sort(key=lambda x:x[1])
print(entry)

to sort using the second element
'''