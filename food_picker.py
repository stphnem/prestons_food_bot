from random import randint

asian_food = ['sushi', 'ramen', 'chow mein', 'korean bbq', 'udon']

def pick_asian_food():
    random_number = randint(0, len(asian_food) - 1)
    return asian_food[random_number]

mexican_food = ['tacos', 'quesadilla', 'buritto', 'enchiladas']

def pick_mexican_food():
    random_number = randint(0, len(mexican_food) - 1)
    return mexican_food[random_number]

italian_food = ['pasta', 'pizza', 'ravioli']

def pick_italian_food():
    random_number = randint(0,len(italian_food)-1)
    return italian_food[random_number]

american_food = ['hamburger','chicken nugget', 'french fries', 'hot dog']

def pick_american_food():
    random_number = randint(0,len(american_food)-1)
    return american_food[random_number]

indian_food = ['roti', 'masala chai', 'curry', 'biryani','tandoori chicken', 'chaat']

def pick_indian_food():
    random_number = randint(0,len(indian_food)-1)
    return indian_food[random_number]

def pick_cuisine(cuisine):
    if cuisine == 'asian':
        return pick_asian_food()
    elif cuisine == 'mexican':
        return pick_mexican_food()
    elif cuisine == 'italian':
        return pick_italian_food()
    elif cuisine == 'american':
        return pick_american_food()
    elif cuisine == 'indian':
        return pick_indian_food()
    else:
        return 'invalid cuisine'
    
print(pick_cuisine('mexican'))