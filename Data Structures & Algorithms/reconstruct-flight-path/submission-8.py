class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        tickets = tickets[::-1]
        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])
        
        res = []

        def dfs(node):
            while adj[node]:
                temp = adj[node].pop()
                dfs(temp)
            res.append(node)
        
        dfs('JFK')
        return res[::-1]


        





        