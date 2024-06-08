import requests
from const import addr

def getUsers():
    response = requests.get(addr + '/users')

    return response.json()

def getCart(user: int):
    response = requests.get(addr + '/ready/' + str(user))

    return response.json()

def delete(user: int):
    response = requests.post(addr + '/del/' + str(user))

    return response.json()  

if __name__ == "__main__":
    users = getUsers()

    print(users)

    if users != None:
        for user in users:
            order = getCart(user)

            for elem in order:
                print("Elem:")
                print("It is package number: ", elem[0])
                print("It is goods id: ", elem[1])
                print("It is amount of good: ", elem[2])
                print()

    