import json
import os
# questions
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

# quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

q1 = Question('What is the most popular programming language ?',['python','javascript','PHP','C#'],'python')
q2 = Question('What is the easiest programming language ?',['java','C++','python','C#'],'python')
q3 = Question('What is the most helpful programming language ?',['python','C#','java','PHP'],'python')

questions = [q1,q2,q3]



class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()

    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('giris yapildi')
                sinav = input('Sinava girmek icin 1 tuslayin: ')
                if sinav == '1':
                    self.getQuiz()
                else:
                    break
            else:
                print('boyle bir kullanici bulunamadi.')

    def getQuiz(self):
        quiz = Quiz(questions)
        


    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}

    def savetoFile(self):

        list = []   
        for user in self.users:
            list.append(json.dumps(user.__dict__))


        with open('kullanicilar.json','w') as file:
            json.dump(list,file)





repository = UserRepository()

while True:
    print('Ogrenci Kayiti'.center(50,'*'))
    islem = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nislem:')

    if islem == '5':
        break
    else:
        if islem == '1':
            username = input('username: ')
            password = input('password: ')
            user = User(username=username,password= password)            
            repository.register(user)
        
        elif islem == '2':
            username = input('username: ')
            password = input('password: ')

            repository.login(username,password)
            
            

        elif islem == '3':
            repository.logout()
        elif islem == '4':
            pass
        else:
            print('hatali tuslama!')




















