def frequency(sentence):
    alpha_map = {}
    for str in sentence:
        if str != ' ':
            if str in alpha_map:
                alpha_map[str] = alpha_map[str] + 1
            else:
                alpha_map[str] = 1
    
    for key,val in alpha_map.items():
        if val > 1:
            return False
    return True
            

