def merge(list1, list2):
    #Takes two sorted lists and merges them into one.
    newlist = []

    #Until one of the list is empty, remove the head of the list with the smaller value and add it to the new list.
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] < list2[0]:
            newlist.append(list1[0])
            list1 = list1[1:]
        else:
            newlist.append(list2[0])
            list2 = list2[1:]

    #Once a list is empty, add the remaining contents of the other list to the end of the new list.
    if not list1:
        newlist.extend(list2)
    elif not list2:
        newlist.extend(list1)

    return newlist


def mergeSort(listtosort):
    if len(listtosort) == 1:
        return listtosort

    #Splits the list in half recursively, then sorts two lists into one using the merge function.
    lengthOfList = len(listtosort)
    leftHalfList = mergeSort(listtosort[:int(lengthOfList / 2)])
    rightHalfList = mergeSort(listtosort[int(lengthOfList / 2):])
    sortedList = merge(leftHalfList, rightHalfList)
    return sortedList
