# Read the input string (like: 1+1+3+1+3)
nums = input().split('+')

# Convert to integers, sort, and convert back to strings
nums = [str(x) for x in sorted(int(i) for i in nums)]

# Join with '+'
print('+'.join(nums))
