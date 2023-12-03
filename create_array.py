import ctypes

class Meralist:
    
# make array   
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)
#length   
    def __len__(self):
        return self.n

#print 
    def __str__(self):
        result = ""
        for i in range(self.n):
            result += str(self.A[i]) + ','

        return '[' + result[:-1] + ']'
#index   
    def __getitem__(self, index):
        if 0 <= index <= self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'
#clear
    def clear(self):
        self.n = 0
        self.size = 1


#append   
    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size*2)

            # append
        self.A[self.n] = item
        self.n += 1

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign
        self.A = B

#pop
    def pop(self):
        if self.n <= 0:
            return 'Empty list'
        
        print(self.A[self.n - 1])
        self.n = self.n - 1
#find
    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - not in list'
#insert
    def insert(self, pos, item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in (self.n, pos, -1):
            self.A[i] = self.A[i-1]

        self.A[pos] =item
        self.n += 1
# delete
    def __delitem__(self, pos):
        if 0 <= pos <= self.n:
            for i in range(pos, self.n - 1):
                self.A[i] = self.A[i + 1]
            self.n = self.n -1 
# remove
    def remove(self, item):
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos
# min
    def min(self, L):
        for item in L:
            if item < min_value:
                min_value = item
        return min_value

    def __make_array(self, capacity):
        return (capacity*ctypes.py_object)()
    
L = Meralist()
L.append("hello")
L.append(10)
L.append("rakhi")

print(L)





    