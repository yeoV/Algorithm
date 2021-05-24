from collections import defaultdict


def solution(tickets):
    # ans = ['ICN']
    ans = []
    d = defaultdict(list)
    for info in tickets:
        d[info[0]].append(info[1])
    # 정렬해주기
    for key in d.keys():
        d[key].sort(reverse=True)

    def dfs(airport):
        if not d[airport]:
            ans.append(airport)
            return
        else:
            while d[airport]:
                nxt = d[airport].pop()
                dfs(nxt)
            ans.append(airport)
    dfs('ICN')
    # print(ans[::-1])
    return ans


solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([['ICN', 'AAA'], ['ICN', 'BBB'], ['BBB', 'ICN']])
# solution([["ICN", "SFO"], ["ICN", "ATL"], [
#          "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
