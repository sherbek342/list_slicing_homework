def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    list1=[1,2,3,4,5]
    l2 = list1[::-1]
    l3 =  list1 + l2
    return l3
print(main(list1=[1,2,3,4,5]))