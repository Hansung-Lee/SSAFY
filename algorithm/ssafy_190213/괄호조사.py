bracket = input()
stack = []
bracket_dict = {')': '(', '}': '{', ']': '['}
error_tf = False

for b in bracket:
    if b in bracket_dict.values():
        stack.append(b)
    else:
        if stack:
            if stack[-1]==bracket_dict[b]:
                stack.pop()
            else:
                print('괄호 사이에는 포함관계만 존재합니다.')
                error_tf = True
                break
        else:
            print('왼쪽 괄호가 먼저 와야합니다.')
            error_tf = True
            break

if not error_tf:
    if stack:
        print('왼쪽 괄호와 오른쪽 괄호의 개수가 같아야합니다.')
    else:
        print('올바른 괄호 사용입니다.')