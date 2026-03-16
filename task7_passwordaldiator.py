import string
def is_valid_password(pw):
    if len(pw)==8 and string.whitespace:
        return False
    elif len(pw)>8:
        p=list(pw)
        lc_count=0
        uc_count=0
        dc_count=0
        pc_count=0
        wp_count=0
        for i in range(len(p)):
            if p[i] in string.ascii_lowercase:
                lc_count+=1
            elif p[i] in string.ascii_uppercase:
                uc_count+=1
            elif p[i] in string.digits:
                dc_count+=1
            elif p[i] in string.punctuation:
                pc_count+=1
            elif p[i] in string.whitespace:
                wp_count+=1
        if(lc_count>=1 and uc_count>=1 and dc_count>=1 and pc_count>=1 and wp_count<1):
            return True
        else:
            return False
    else:
        return False


print(is_valid_password("short1! "))