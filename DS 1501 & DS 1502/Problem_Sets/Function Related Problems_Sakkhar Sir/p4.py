def calculate_sum(lst0):
    """calculate the sum of n numbers 
    coming from the console and stored in an array"""
    total = sum(lst0)
    print(f"Sum In Function: {total}")
    return total
n = int(input())
lst = list(map(int, input().split()[:n]))
sumation = calculate_sum(lst)
print(f"Sum In Main: {sumation}")