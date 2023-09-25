class User:
    def __init__(self,name):
        self.name = name
        self.loggedin = False

def authentication_dec(function):
    def wrapper(*args,**kwargs):
        if args[0].loggedin == True:
            function(args[0])
    return wrapper
@authentication_dec
def createPost(user):
    print(f'{user.name} created a post')
kersten = User("kersten")


createPost(kersten)