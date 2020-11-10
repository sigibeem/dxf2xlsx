class myclass:
    user_name = None
    age = None
    def say(self):
        print("名前 : {0}, 年齢 : {1}".format(self.user_name, self.age))
user1 = myclass()
user1.user_name = "山田"
user1.age = 29

user1.say()