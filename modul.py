## Krzysztof Niezabitowski## L3

class FiboIter:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a
    

def fibgen(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a

class FiboIter2:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        a, b = 0, 1
        for i in range(self.n):
            a, b = b, a + b
            if i>=100000:
                yield a




if __name__ == '__main__':

    ciag = FiboIter(10) ## zwracaj kolejne wyrazy cagu mniejsze od n>0
    ciag2 = FiboIter2(100020) ## zwraca kolejne wyrazy ciagu mniejsze od n>100000
    file = open("plik.txt","w")
    dlugosc = []
    for num in ciag2: ## zapisuje liczby do pliku tekstowego 
        file.write(str(num)+"\n")
    file.close()
    with open('plik.txt') as file:
        for linia in file: ## liczy dlugosci liczb z pliku tekstowego
            dlugosc.append(len(linia)-1)
    print("\n")
    n = 100000
    print(f"dlugosc liczyby {n} ciagu fibonacciego wynosi:{dlugosc[0]}")

    



    
    

    
    
