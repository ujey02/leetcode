// 0ms / 97.79%

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        else
        {
            int p1 = 1;
            int p2 = 2;
            for (int i = 0; i < n-2; i++)
            {
                swap(p1,p2);
                p2 = p1 + p2;
            }
            return p2;
        }
    }
};
