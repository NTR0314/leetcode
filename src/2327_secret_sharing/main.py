class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        new_each_day = [0] * (n + 1)
        new_each_day[1] = 1
        
        active_sharers = 0
        total = 0
        
        for day in range(2, n + 1):
            # Someone who learned 'delay' days ago starts sharing today
            if day - delay >= 1:
                active_sharers += new_each_day[day - delay]
                
            # Someone who learned 'forget' days ago stops sharing today
            if day - forget >= 1:
                active_sharers -= new_each_day[day - forget]
            
            # Today's new people = current active sharers
            new_each_day[day] = active_sharers % MOD
        
        # print(new_each_day)
        for day in range(max(1, n - forget + 1), n + 1):
            # print(day)
            total += new_each_day[day]
        
        return total % MOD