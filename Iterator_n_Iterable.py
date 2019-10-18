#Iteratable and Iterator
#create a class that can be used as a generator
class Sentence():
    def __init__(self, txt):
        self.txt_lst = txt.split()
        self.txt_len = len(self.txt_lst)
        self.start = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.txt_len:
            raise StopIteration
        current = self.txt_lst[self.start]
        self.start += 1
        return current

my_sentence = Sentence('This is a test')

# for w in my_sentence:
#     print(w)

#A function that return a generator, so much easier
def sentence(txt):
    return (w for w in txt.split())

# g = sentence('This is a test')
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))