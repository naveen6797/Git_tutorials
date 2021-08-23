a='dad'
i=len(a)-1
result=''
while i>=0:
  result=result+a[i]
  i=i-1
  print(result)
if(a==result):
    print('its a palindrome')
else:
    print('not a palindrome')

