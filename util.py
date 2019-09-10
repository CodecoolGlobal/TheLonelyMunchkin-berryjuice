from random import randint

def get_gender_randomly():
    genders = ['male', 'female']
    random = randint(0, 1)

    return genders[random]
