addset = set(('Google', 'Taobao', 'MS'))
addset.add('Metaverse')
print(addset)

#####
updateset = set(('Google', 'Taobao', 'MS'))
updateset.update({1,2,3})
print(updateset)

updateset = set(('Google', 'Taobao', 'MS'))
updateset.update([1,4], [1,5,6])
print(updateset)

#####
removeset = set(('Google', 'Taobao', 'MS'))
removeset.remove('MS')
print(removeset)

removeset = set(('Google', 'Taobao', 'MS'))
removeset.remove('Meta')
print(removeset)

#####
discardset = set(('Google', 'Taobao', 'MS'))
discardset.discard('Meta') #没有这个element
print(discardset)