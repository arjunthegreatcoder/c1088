import random as r 
import plotly.figure_factory as ff
sumlist = []
for i in range(0,100):
    dice1 = r.randint(1,6)
    dice2 = r.randint(1,6)
    sum = dice1+dice2
    sumlist.append(sum)

figure = ff.create_distplot([sumlist],["sumList"],show_hist = False)
figure.show()