#WRP to check whether inputed no. is Armstrong no. or not.
s=0
no=int(input('Enter any no.:'))
temp=no
while no>0:
    rem=no%10
    s+=rem*rem*rem
    no//=10
if s==temp:
    print(f'The inputed no.{temp} is Armstrong no.')
else:
    print(f'The inputed no.{temp} is not Armstrong no.')
