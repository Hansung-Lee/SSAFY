def my_map1(func, input_list):
    # 0. 빈 리스트를 만들고
    # 1. 인자로 받은 리스트를 돌면서
    # 2. 인자로 받은 함수를 각각의 요소에 적용한 값을 빈 리스트에 넣어서
    # 3. 빈 리스트를 리턴한다.
    new_list = []

    for il in input_list:
        new_list.append(func(il))
    
    return new_list

def my_map2(func, input_list):
    return [func(i) for i in input_list]



def is_even(num):
    return not num%2

def my_filter(func, input_list):
    return [i for i in input_list if func(i)]

if __name__ == "__main__":
    print(list(map(int, ["1","2"])))
    print(my_map1(int, ["1","2"]))
    print(my_map2(int, ["1","2"]))

    print(list(filter(is_even,[1,2,3,4])))
    print(my_filter(is_even,[1,2,3,4]))