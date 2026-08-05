class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        from collections import defaultdict

        adj = defaultdict(list)
        for u, v in invocations:
            adj[u].append(v)
        
        suspicious = set()
        stack = [k]
        suspicious.add(k)
        
        while stack:
            curr = stack.pop()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    stack.append(neighbor)
        
        is_valid = True
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                is_valid = False
                break
        
        if not is_valid:
            return list(range(n))
        
        return [i for i in range(n) if i not in suspicious] 