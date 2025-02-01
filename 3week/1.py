class string:
    def get_str(self):
        self.input_str=input()
    def prt_str(self):
        print(self.input_str.upper())
    def rvs_str(self):
        print(self.input_str[::-1])
        
string_manipulation=string()        
string_manipulation.get_str()
string_manipulation.prt_str()        
string_manipulation.rvs_str()