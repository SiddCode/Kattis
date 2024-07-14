u = int(input())

p,k,w = False, False, False
for i in range(u):
    o = input()
    if o == 'phone':
        p = True
    if o == 'keys':
        k = True
    if o == 'wallet':
        w = True

if k == False:
    print('keys')
if p == False:
    print('phone')
if w == False:
    print('wallet')
if p == True and k == True and w == True:
    print('ready')