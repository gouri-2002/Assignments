

def commmon_data(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result

print(commmon_data([2,3,4],[3,5,6]))