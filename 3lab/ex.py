#ex1

def gramToOunces(grams):
    return grams*28.3495231

a = 2 #in grams
print(gramToOunces(a))

def FtoC(faren):
    return (faren-32)*(5/9)

b = 3 #in farenheit 
print (FtoC(b))

def primeSorter(list):
    result = []
    for i in list:
        if i > 1:
            flag = False
            for j in range(2, int(i**0.5) + 1):
                if i % j==0:
                    flag = True
                    break
            if not flag:
                result.append(i)
    return result

c = [1,4,6, 19, 17, 11]
print(primeSorter(c))

def permutator(str, empt = ""):
    if not str:
        print(empt)
    else:
        for i in range(len(str)):
            new_str = str[:i] + str[i+1:]
            permutator(new_str, empt + str[i])

# permutator("sultan")

def wordReversor(str1):
    b = str1.split(" ")
    str2 = ""
    for i in reversed(b):
        str2 += i
        str2 += " " 
    print(str2)

wordReversor("hello everyone")

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

list = [3,4,5,6,7,3]
print(has_33(list))

def spy_game(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i+2] == 7:
            return True
    return False

list = [0,0,4,0,0,7]
print(spy_game(list))


def findValue(radius):
    print((4/3)*3.14*radius**2)

findValue(3)

def uniqueElements(list):
    unique_list = []
    
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    
    return unique_list

list = [1,4,4,5,5,6,3,1]
result = uniqueElements(list)

print(result)

