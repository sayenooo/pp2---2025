def solve(numheads, numlegs):
    rabbits = (numlegs - numheads*2)//2
    chicken = numheads - rabbits
    print(f"rabbits = {rabbits}")
    print(f"chicken = {chicken}")
    
h,l = map(int,input().split())
solve(h,l)