def solution(s):
    answer = ''
    visited = [False] * len(s)

    def dfs(depth, nxt, ans):
        nonlocal answer
        answer = max(answer, ans)
        if depth == len(s):
            return
        for i in range(nxt, len(s)):
            if not visited[i]:
                visited[i] = True
                dfs(depth+1, i, ans+s[i])
                visited[i] = False
    dfs(0, 0, '')
    return answer


solution("xyb")
solution("yxyc")
