class User:
    def __init__(self):
        self.user_type ='guest'
        self.uname = None
        self.pwd = None
        self.email = None

    def register(self,uname, pwd, email):
        self.uname = uname
        self.pwd = pwd
        self.email = email

    def __repr__(self):
        str = f"Name: {self.uname}, Email: {self.email}, User Type: {self.user_type}"
        return str
    
class FrequentTraveller(User):
        def __init__(self):
            self.user_type ='Frequent Traveller'
            self.travellerID = None

        def register(self, uname, pwd, email, travellerID):
            super().register(uname, pwd, email)
            self.travellerID = travellerID

        def __repr__(self):
            str = super().__repr__()
            str = str + f" Traveller ID: {self.travellerID}"
            return str