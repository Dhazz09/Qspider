class Mobile:       #class declaration
    storage="512gb"
    camera="8k"
mob=Mobile()       #object defining
print(Mobile.storage)   #calling property by class name
print(mob.storage)       #calling property by object   
Mobile.storage="256gb:"
print(mob.storage)
Mobile.camera="48MP"
print(Mobile.camera)
mob1=Mobile()
mob1.storage="128gb"
print(Mobile.storage)
print(mob.storage)
print(mob1.storage)
Mobile.storage="1T"
print(mob.storage)
print(mob1.storage)