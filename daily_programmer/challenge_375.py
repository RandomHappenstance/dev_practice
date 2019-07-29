
def add_one(num):
    return ''.join([str(int(index)+1) for index in str(num)])
    
print(add_one(998))
