
# hash code - More Pizza

Objective: Order the greatest possible no. of pizza slices

## Rules

1. Only can order one of each type
2. Total slices cannot be greater than M (Max. slices)

## Examples
a.
<br />

i) Input

    Stock:
        M = 17
        N = 4

    Menu:
    {
        Type 0: 2 slices
        Type 1: 5 slices
        Type 2: 6 slices
        Type 3: 8 slices
    }

ii) Submission
    
    Order:
        N = 3 types
    
    
    {
        Type 0: 2 slices
        Type 2: 6 slices
        Type 3: 8 slices

    }

    Total slices = 16


b.

    M = 100
    N = 10

    {
        Type 0: 4 slices
        Type 1: 14 slices
        Type 2: 15 slices
        Type 3: 18 slices
        Type 4: 29 slices
        Type 5: 32 slices
        Type 6: 36 slices
        Type 7: 82 slices
        Type 8: 95 slices
        Type 9: 95 slices
    }

c.

    M = 4500
    N = 50

    {
        Type 0: 7 slices
        Type 1: 12 slices
        Type 2: 12 slices
        Type 3: 13 slices
        Type 4: 14 slices
        Type 5: 28 slices
        Type 6: 29 slices
        Type 7: 29 slices
        Type 8: 30 slices
        Type 9: 32 slices
        Type 10: 32 slices
        ...
        ...
        Type 49: 195 slices
    }

d.

    M = 1000000000
    N = 2000

    {
        Type 0: 476 slices
        ...
        ...
        Type 1999: 999867 slices
    }

e.

    M = 505000000
    N = 10000

    {
        Type 0: 223
        ...
        ...
        Type 9999: 150000
    }