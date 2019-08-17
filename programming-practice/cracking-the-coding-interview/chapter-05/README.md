# Bit manipulation

Left shift by 2
    - Is equivalent to power of a number by 2
    
Right shift by 2
    - Is equivalent to square root of number of 2
    


##  what the following code does: ((n & (n-1)) == 0) ?

It means they have no common ones in their binary representation.
As we know 1&1 = 1 and 0 & 1 or 1 & 0 equals 0, we can be sure that n and n-1 does not
have any ones in common places.

It can be also used to find out if a number is even. If n&n-1 equals 0, then n is even number.
All even numbers have 1 at their right most place, followed by zeros. So the n-1 number which is one digit less than
the n number will have all ones at the all the zero places of n number.
