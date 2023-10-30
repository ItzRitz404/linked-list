class ssl():
    def __init__(self):
        self.singleList = []

    def insert(self, value):
        self.singleList.append(value)
        return self.singleList
    
    def searchFor(self, item):
        for i in self.singleList:
            if i == item:
                return self.singleList[i]
            else:
                return "item not found"    
    
    def delete(self, index):
        self.singleList.remove(index)

    def traverse(self):
        for i in self.singleList:
            print(i)
        



list1 = ssl()
list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(4)
list1.insert(5)
print(list1.traverse())