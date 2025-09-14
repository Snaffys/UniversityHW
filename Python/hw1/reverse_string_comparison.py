def reverse_string_comparison(str1, str2):
    if(str1 == str2):
        print("strings are equal")
        return

    min_len = min(len(str1), len(str2))

    for i in range(min_len):
        if(str1[i] != str2[i]):
            if(str1[i] < str2[i]):
                print(str1, ">", str2)
            else:
                print(str1, "<", str2)     
            return           
    if(len(str1) < len(str2)):
        print(str1, "<", str2)
    else:
        print(str1, ">", str2)