from datetime import datetime
import getpass, random, time
stored_users = {'Schuyler': 'dimple', 'BP': 'forehead', 'Rorie': 'explore', 'Deep': 'dive', 'Andrew': 'foureyes'}
tries = 1
name = ''
pswd = ''
current_time = datetime.now().strftime("%H:%M:%S")
session = 'dead'
user_message = ''
while True:
    while session == 'dead':
        name = input("Username: ")
        if name in stored_users:
            pswd = getpass.getpass('Password: ')
            if pswd in stored_users[name] and len(pswd) > 0:
                session = 'live'
                break
            else:
                print('You have made '+str(tries)+' attempts. '+str(4-tries-1)+' remaining.')
                tries += 1
        else:
            print('That username does not exist')
        if tries >= 4:
            print('You have made too many attempts, please try again later.')
            break
    while session == 'live':
        user_message = input("Message: ")
        timename = current_time + " - " + name
        if user_message == '/logout':
            session = 'dead'
        elif user_message == '/roll':
            print(timename + ": " + str(random.randint(1,100)))
        elif user_message == '/pull':
            i = 10
            while i != 0:
                print("pulling in " + str(i))
                i -= 1
                time.sleep(1)
            print("Pull Now!")
        else:
            print(timename + ": " + user_message)
