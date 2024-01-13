import threading

def helloWorld():
    for i in range(100):
        print("Hello World")
    
def helloBangladesh():
    for i in range(100):
        print("Hello Bangladesh")
    
t1= threading.Thread(target=helloWorld)
t2 = threading.Thread(target=helloBangladesh)
t1.start()
t2.start()