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
        
    
    def sort(self):
        size = len(self.singleList)
        swapped = False

        for index in range(size - 1, 0, -1):
            for i in range(index):
                if self.singleList[i] > self.singleList[i + 1]:
                    swapped = True
                    self.singleList[i], self.singleList[i + 1] = self.singleList[i + 1], self.singleList[i]

        return self.singleList




list1 = ssl()
list1.insert(5)
list1.insert(3)
list1.insert(1)
list1.insert(2)
list1.insert(4)
print(list1.traverse())
print(list1.sort())