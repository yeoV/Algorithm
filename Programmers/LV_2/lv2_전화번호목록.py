def solution(phone_book):
    # 길이가 긴것은 정렬할 필요 x
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    else:
        return True


solution(["119", "97674223", "1195524421"])
solution(["123", "456", "789"])
