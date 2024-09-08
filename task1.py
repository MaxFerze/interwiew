class Stack():

    def __init__(self, mylist): 
        self.mylist = list(mylist)

    def is_empty(self):
        if self.mylist == []:
            return True
        else:
            return False
        
    def push(self, object): 
        self.mylist.append(object)

    def pop(self):
        self.mylist.remove[-1]

    def peek(self):
        return self.mylist[-1]
    
    def size(self):
        return len(self.mylist)
    
    def check_balance(self):
        parenthesis = []
        pairs_parenthesis = {')':'(',']':'[','}':'{'}

        for i in self.mylist:
            if i in pairs_parenthesis.values():
                parenthesis.append(i)
            elif i in pairs_parenthesis.keys():
                if pairs_parenthesis.get(i) in parenthesis:
                    parenthesis.remove(pairs_parenthesis.get(i))
                else:
                    print('Несбалансированно')
                    return
            
        print('Cбалансированно')



if __name__ == '__main__':
    pass

string1 = Stack("(((([{}]))))")
string1.check_balance()
string2 = Stack("[([])((([[[]]])))]{()}")
string2.check_balance()
string3 = Stack("{{[()]}}")
string3.check_balance()
string4 = Stack("}{}")
string4.check_balance()
string5 = Stack("{{[(])]}}")
string5.check_balance()
string6 = Stack("[[{())(}]]")
string6.check_balance()
string7 = Stack(")))(((")
string7.check_balance()
string8 = Stack("")
string8.check_balance()

