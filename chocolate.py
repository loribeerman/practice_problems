'''from hackerrank:  Little Bob loves chocolate, and he goes to a store with $N$N in his pocket. The price of each chocolate is $C$C. The store offers a discount: for every MM wrappers he gives to the store, he gets one chocolate for free. How many chocolates does Bob get to eat?'''


N, C, M = 6, 2, 2
num_choc = N / C
num_wrap = N / C

while num_wrap >= M:
   num_wrap -= M
   num_choc += 1
   num_wrap += 1

print num_choc
