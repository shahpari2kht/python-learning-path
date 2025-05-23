# دریافت ورودی
s = input().strip()

# بررسی دو حالت: یکی اول AB و بعد BA، یکی اول BA و بعد AB (بدون همپوشانی)
def check_pair(s, first, second):
    idx1 = s.find(first)
    if idx1 == -1:
        return False
    idx2 = s.find(second, idx1 + 2)
    return idx2 != -1

if check_pair(s, 'AB', 'BA') or check_pair(s, 'BA', 'AB'):
    print("YES")
else:
    print("NO")
