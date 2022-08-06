class Solution:
    def countArrangement(self, n: int) -> int:
        mask = 1 << n
        dp = [[0 for _ in range(mask)] for _ in range(n+2)]
        dp[0][0] = 1
        for i in range(1, n+1):
            print(f'i={i}')
            for state in range(mask):
                print(f'  state={bin(state)}')
                for k in range(1, n+1):
                    is_k_picked_in_state = state >> (k-1) & 1
                    print(f'    k = {k}')
                    if not is_k_picked_in_state:
                        print('    k is not picked within this state.')
                        continue
                    if k % i != 0 and i % k != 0:
                        print('    k at i not fulfill 1. and 2.')
                        continue
                    stateWithoutK = state & (~(1 << (k - 1)))
                    permCntWithoutK = dp[i-1][stateWithoutK]
                    print(f'    stateWithoutK = {bin(stateWithoutK)}, permCntWithoutK = {permCntWithoutK}')
                    dp[i][state] += permCntWithoutK;
                    print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in dp]))
        return dp[n][mask-1]    #mask - 1 = all k are selected
    
s = Solution()
#s.countArrangement(3)
s.countArrangement(5)