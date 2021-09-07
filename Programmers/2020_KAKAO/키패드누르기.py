# 키패드 누르기

left = [1, 4, 7]
right = [3, 6, 9]
keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9],['*', 0, '#']]

# 현재 손의 좌표 찾기
def find_location(num):
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == num:
                return i, j


def solution(numbers, hand):
    answer = ''
    lefthand = (3,0)
    righthand = (3,2)
    for n in numbers:
        if n in left:
            answer += 'L'
            lefthand = find_location(n)
        elif n in right:
            answer += 'R'
            righthand = find_location(n)
        else:
            x, y = find_location(n)
            x_length = abs(righthand[0]-x) + abs(righthand[1]-y)
            y_length = abs(lefthand[0]-x) + abs(lefthand[1]-y)
            # 길이 비교 후 왼손 or 오른손 움직임
            if x_length > y_length:
                answer += 'L'
                lefthand = (x,y)
            elif y_length > x_length:
                answer += 'R'
                righthand = (x,y)
            else:
                if hand == 'left':
                    answer += 'L'
                    lefthand = (x,y)
                elif hand=='right':
                    answer += 'R'
                    righthand = (x,y)

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
