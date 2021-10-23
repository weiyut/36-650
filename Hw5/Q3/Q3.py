def oneedit(str1, str2):
    if abs(len(str1) - len(str2)) > 1: 
        return False
    count = 0
    idx_1 = 0
    idx_2 = 0
    while idx_1 <len(str1) and idx_2 < len(str2):
        if str1[idx_1] != str2[idx_2]:
            count += 1
            idx_1, idx_2 = (idx_1+1, idx_2) if len(str1) > len(str2) else (idx_1, idx_2+1) if len(str2) > len(str1) else (idx_1+1, idx_2+1)
        else:
            idx_1 +=1;idx_2 +=1
    count = count+1 if idx_1 <len(str1) or idx_2 < len(str2) else count
    return count <= 1 

print(oneedit('pale','ple'))
print(oneedit('pales','pale'))
print(oneedit('pale','bale'))
print(oneedit('pale','bake'))