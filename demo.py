from cocos.director import director
from cocos.tiles import load
from cocos.layer import ScrollingManager
from cocos.scene import Scene

director.init()
a = load("demo.tmx")["mytiles"]
scroller = ScrollingManager()
scroller.add(a)
director.run(Scene(scroller))
