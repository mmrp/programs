import time
def loop(n):
    s = time.time()
    for i in range(n):
        pass
    e = time.time()
    print (e-s)


print (loop(int(raw_input("n :"))))


