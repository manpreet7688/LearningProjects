'''BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) 18
blackjack(9,9,9)  'BUST'
blackjack(9,9,11) 19'''

def blackjack(int1,int2,int3):
    if sum((int1,int2,int3)) <= 21:
        return sum((int1,int2,int3))
    elif sum((int1,int2,int3)) > 21 and (int1==11 or int2==11 or int3==11):
        return sum((int1,int2,int3)) - 10
    else:
        return 'Bust'

result = blackjack(5,6,7)
print(result)

result = blackjack(9,9,9)
print(result)

result = blackjack(9,9,11)
print(result)