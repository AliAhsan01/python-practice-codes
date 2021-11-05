import re


x="the rain is happeining in spring"
y=re.search("^the.*spring$",x)

if x:
  print('yes,we have it')
else:
  print('no')