class Solution {
public:
    int maxProfit(vector<int>& prices) {
        const int n = prices.size();
        if (n == 0) {
            return 0;
        }
        int first, second, maximum;
        first=second=maximum = 0;
        
        for(int i=0; i< n; i++) {
            if (prices[i] <= prices[first]) {
                first = second= i;
            }
            if (prices[i] > prices[second]) {
                second = i;
                maximum = max(maximum, prices[second] - prices[first]);
            }
        }
        return maximum;
        
    }
};
