
## Abdirizak Ali ##

from graphics import *
win = GraphWin("T_V Graph", 600, 800)
win.setCoords(-20,0,40,40)

linex = Line(Point(-5,10), Point(40,10))
linex.draw(win)

liney = Line(Point(-5,10), Point(-5,40))
liney.draw(win)

## Y Axis Labels

velocity = Text(Point(-10,25), "Velocity")
velocity.draw(win)

zeroy = Text(Point(-7,10), "0m/s")
zeroy.draw(win)


teny = Text(Point(-7,13), "10m/s")
teny.draw(win)


twentyy = Text(Point(-7,23), "20m/s")
twentyy.draw(win)


thirtyy = Text(Point(-7,33), "30m/s")
thirtyy.draw(win)

## X Axis Labels

timex = Text(Point(14,7), "Time")
timex.draw(win)

zerox = Text(Point(-5,9), "0s")
zerox.draw(win)

fivex = Text(Point(2,9), "5s")
fivex.draw(win)

tenx = Text(Point(10,9), "10s")
tenx.draw(win)

fifteenx = Text(Point(18,9), "15s")
fifteenx.draw(win)

twentyx = Text(Point(26,9), "20s")
twentyx.draw(win)



infilet = open("t.txt", "r")
infilev = open("v.txt", "r")


tlist = []

for i in infilet:
    x = i.strip()
    tlist.append(int(x))
print(tlist)

vlist = []

for i in infilev:
    z = i.strip()
zsplit = z.split(",")

for i in zsplit:
   vlist.append(int(i))


for i in range(len(tlist)):
    newpoint = Point(tlist[i],vlist[i])
    newpoint.draw(win)
