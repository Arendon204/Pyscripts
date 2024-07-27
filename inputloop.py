def call():
    return cal()

def cal():
    num = int(input("number: "))
    print("a number: " + str(num))
    
    
    
    while True:
        
        if num < 20:
            print("less than 20")
        
        elif num >= 20:
            print("more than 20")

        again = input("to go again press y or n: ")    
        if again not in {"y", "n"}:
            print("pick one ")

        elif again == "n":
            return "finished op"
        
        elif again == "y":
            
            return call()

call()
            