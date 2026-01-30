class stack:
    def __init__(self):
        self.items = []
        def isEmpty(self):
            return len( self.items) == 0
        

        def push (self, items):
            self.items.append(items) 

        def pop(self):
                if self.isEmpty():
                    return "stack is empty"
                
                else:
                    return self.items.pop()

        def peek(self):
            if not self.isEmpty():
                return self.items[-1]    
            else:
                return "stack is empty"     
            

        def size(self):
            return len(self.items)   

        def display(self):
            return self.items   
        
        def menu():
            print("1.push")
            print("2.pop")
            print("3.peek")     
            print("4.size")
            print("5.display")
            print("6.exit")

                
        choice  = int(input("enter your choicr:"))

        if choice == 1:
                    item = int(input("enter the item to push:"))
                    self.push(item)
                
        elif choice == 2:
                    print("popped item:",self.pop())

        elif choice == 3:
                    print("top item is:",self.peek())

        elif choice == 4:
                    print("size of stack is:",self.size())  

        elif choice == 5:
                    print("stack items are:",self.dispaly())

        else:
                    print("it is a invalid choice")  
s=stack()

         
        
        