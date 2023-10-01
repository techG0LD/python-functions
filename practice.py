def hello():
    print("Hello user")

def greet_user(user):
    print(f"Hi, {user}")

def pack(item1,item2,item3):
    return [item1,item2,item3]
    
def eat_lunch(Lunch_items):
    if len(Lunch_items) == 0:
            print("My lunchbox is empty")

    for item in Lunch_items:
        if(item == Lunch_items[0]):
            print(f"First I eat {item}")
        elif item != Lunch_items[0]:
             print(f"Then I eat {item}")



    # if len(Lunch_items) == 0:
    #     print("My lunchbox is empty")
    # else:
    #     for index in range(len(Lunch_items)):
    #         if index == 0:
    #             print(f"First I eat {Lunch_items[index]}")
    #         else:
    #             print(f"Then I eat {Lunch_items[index]}")
    

greet_user("mat")

print(pack("show","glow","flow"))

eat_lunch(pack("show","glow","flow"))