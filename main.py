print('Hello, bro!')


def return_longer_line(str1: 'str', str2: str) -> str:
    """
    The function takes two str strings and returns the longest of them.
    """
    if len(str1) > len(str2):
        return str1
    else:
        return str2


print(return_longer_line('Hi!', 'Git one love'))


def return_only_numbers(lst: list) -> bool:
    """
   The function accepts a list and returns True if the list consists only of numbers and False if not.
    """
    for item in lst:
        if type(item) in {int, float}:
            continue
        else:
            return False
    return True


lst = [1., 'New York', 76]
if return_only_numbers(lst):
    sum(lst)
print(return_only_numbers(lst))


def print_eighty_stars() -> None:
    """
The function outputs a tape of 80 stars to the console. The function takes no arguments and returns no value.
    """
    print('*' * 80)
