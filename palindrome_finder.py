n = int(input("Number: "))

palindrome = False
ans = 0
i = 0

def reverse(s):
    return s[::-1]

while not palindrome:
    i += 1
    m = reverse(str(n))
    m = int(m)

    if str(n + m) == reverse(str(n + m)):
        palindrome = True
        sum = str(n) + " + " + str(m) + " = "
        ans = n + m
    else:
        sum = str(n) + " + " + str(m) + " = "
        n = n + m
        print(str(i) + ". " + sum + str(n))

print("Palindrome: " + sum + str(ans))
print("That took " + str(i) + " step(s).")