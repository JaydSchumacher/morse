class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
        
    def __str__(self, pattern):
        self.pattern = pattern
        print(self.pattern)
        self.new_str = ''
        for item in self.pattern:
            if item == ".":
                self.new_str += "dot-"
            if item == "_":
                self.new_str += "dash-"
        return self.new_str
    

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)


test =  S()
print(test.__str__(pattern = ['.', '.', '.']))