def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        n = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            if phone_book[i][:n] != phone_book[j][:n]:
                break
            if phone_book[j].startswith(phone_book[i]):
                return False

    return True

print(solution(["119", "97674223", "1195524421"]))