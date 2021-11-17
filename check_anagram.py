def check_anagram(str1,str2):
    if list(str1).sort()==list(str2).sort():
        print("%(str1)s and %(str2)s are Anagram Pairs" %{'str1':str1,'str2':str2})
    else:
        print("%(str1)s and %(str2)s are Not Anagram Pairs" %{'str1':str1,'str2':str2})

check_anagram('eat','ate')