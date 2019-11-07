#a named tuple is self-explanatory, 
# #it provide a way to access tuple with a dictionary-like key

from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color (55,155,255)

print(color[0])    #55
print (color.red)  #55