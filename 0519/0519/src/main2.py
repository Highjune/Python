class Demo:
    __name = '한지민'    #class variable
    
    @classmethod
    def class_print(cls):
        print('name = ' + cls.name)
        
    @staticmethod
    def static_print():
        print('name = ' + Demo.name)
        
    def member_print(self):
        print('name = ' + self.name)
        
if __name__ == '__main__' :
    d = Demo()
    #print(d.__name)  접근못함.
    print(d._Demo__name)
#     Demo.class_print()
#     d.member_print()
#     Demo.static_print()