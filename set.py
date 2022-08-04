addset = set(('Google', 'Taobao', 'MS'))
addset.add('Metaverse')
print(addset)

print('----------------------------------------------------')

updateset = set(('Google', 'Taobao', 'MS'))
updateset.update({1,2,3})
print(updateset)

updateset = set(('Google', 'Taobao', 'MS'))
updateset.update([1,4], [1,5,6])
print(updateset)

print('----------------------------------------------------')

removeset = set(('Google', 'Taobao', 'MS'))
removeset.remove('MS')
print(removeset)

removeset = set(('Google', 'Taobao', 'MS'))
removeset.remove('Meta')
print(removeset)

print('----------------------------------------------------')

discardset = set(('Google', 'Taobao', 'MS'))
discardset.discard('Meta') #没有这个element
print(discardset)