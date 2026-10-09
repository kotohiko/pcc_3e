def hello_world():
    print("Hello World!")


times = 5

for i in range(times):
    print(i)
    if i == 0:
        continue
    hello_world()
