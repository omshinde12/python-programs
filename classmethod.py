class myclass:
    @staticmethod
    def smeth():
     print("this is a static method")
    @classmethod
    def cmeth(cls):
     print("this is a class ,method",cls)
myclass.smeth()
myclass.cmeth()
