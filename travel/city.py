class City:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        
    def cityDetail(self):
        return str(self)
    
    def __repr__(self):
        str = f"City Name: {self.name}, City Description: {self.description}"
        return str

