import pickle


def verifyUser(username, password):

    with open('user_data.pkl', 'rb') as fp:
        users = pickle.load(fp)

    return users.get(username, None).get('password', "") == password


def addUser(username, password, email):

    with open('user_data.pkl', 'rb') as fp:
        users = pickle.load(fp)

    if username in users:
        return False

    users.update({username: {'password': password, 'email': email}})

    with open('user_data.pkl', 'wb') as fp:
        pickle.dump(users, fp)

    return True


def getUsers():

    with open('user_data.pkl', 'rb') as fp:
        users = pickle.load(fp)

    return users
