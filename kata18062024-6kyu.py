#Write a function that takes an array of numbers (integers for the tests) and a target number.
#It should find two different items in the array that, when added together, give the target value.
#The indices of these items should then be returned in a tuple / list (depending on your language) like so: `(index1, index2)`.

#For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

#The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers;
#target will always be the sum of two different items from that array). 

def two_sum(numbers, target):
    result = []
    for i in numbers:
        x = int(target) - i
        if x in numbers and numbers.count(x) != 1:
            inx = [n for n, t in enumerate(numbers) if t == x]
            z = max(inx)
            result.append(numbers.index(i))
            result.append(z)
            break
        elif x in numbers and numbers.count(x) == 1 and x != i:
            result.append(numbers.index(x))
            result.append(numbers.index(i))
            break
        else:
            continue
    result = tuple(result)
    return result
