def sol(str):
    if str[0] == "-":
        print(-int(str.lstrip("+-")))
    else:
        print(int(str.lstrip("+-")))


sol("1234")
sol("-1234")
sol("+1234")


def sol2(str):
    print(int(str))


sol2("1234")
sol2("-1234")
sol2("+1234")
