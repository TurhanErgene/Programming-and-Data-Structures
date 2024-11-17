
text_list = ["anna", "Kakor", "akAkA", "madam"]

def check_palindrome(str):
    str = str.lower()

    if len(str) == 1 or "":
        return True
    elif str == str[::-1]:
        return True
    else:
        return False


for i in range(len(text_list)): 
    print("text", str(i+1), " (", text_list[i], "): ", str(check_palindrome(text_list[i])))
# print("text 1: ", check_palindrome(text))
# print("text 2: ", check_palindrome(text2))
# print("text 3: ", check_palindrome(text3))

# for i in text_list:
    # print(check_palindrome(i))
