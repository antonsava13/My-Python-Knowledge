import re

def re_match_1():
    m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
    m.group(0)       # The entire match
    m.group(1)       # The first parenthesized subgroup.
    m.group(2)       # The second parenthesized subgroup.
    m.group(3)       # The third parenthesized subgroup.
    m.group(1,2,3)   # Multiple arguments give us a tuple.

def re_match_2():
    import re
    m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
    m.groups()

def re_match_3():
    m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
    print(m.groupdict())

def re_findall_1():
    re.findall(r'\w','http://www.hackerrank.com/')
    # ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

def re_findall_2():
    re.finditer(r'\w','http://www.hackerrank.com/')
    # <callable-iterator object at 0x0266C790>
    l = map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))

    print(l)
    for i in l:
        print(i)
    # ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

def positive_negative_lokahaed():
    import string
    my_string = "baaekeetaat"
    vowels = "aeiouAEIOU"
    consonants = "".join([x for x in string.ascii_letters if x not in vowels])
    reg = rf"[{consonants}]([{vowels}]{{2,}})(?![{vowels}])"
    res = re.findall(reg, my_string)
    if res:
        for i in res:
            print(i)
    else:
        print(-1)

def start_end_of_serach():
    m = re.search(r'\d+','1234')
    print(m.end())
    # 4
    print(m.start())
    # 0

def find_start_end_of_search_string():
    str_1 = input()
    str_2 = input()

    len_str_2 = len(str_2) - 1

    rex = fr"(?=({str_2}))"
    m = re.finditer(rex, str_1)

    result = []

    for i in m:
        result.append(f"({i.start()}, {i.start()+len_str_2})")

    if len(result) == 0:
        print("(-1, -1)")
    else:
        for j in result:
            print(j)


if __name__ == "__main__":

    pass
# Hello

