def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")

def greet(name , location):
    print(f"hellow {name}")
    print(f"how do you do {name} ?")
    print("is'not the  weather nice !")
    print(f"i live in {location}")


greet(location="umer" , name="lahore")


def life_in_weeks(x):
    currentage = int(x)
    totallage = 90
    print("if the totall life is 90 year")
    remage =  totallage - currentage
    print(f"remaining age is {remage}")
    inweeks = remage * 52.1
    print("so your remaining age in weeks is {inweeks}")
    
life_in_weeks(56) 