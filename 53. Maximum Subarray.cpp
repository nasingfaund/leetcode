// brute force O(n^3) - Time Limit Exceeded
class Solution {
public:
    int maxSubArray(vector<int> &nums) {
        const int n = nums.size();
        int best = INT_MIN;
        for (int a = 0; a < n; a++) {
            for (int b = a; b < n; b++) {
                int sum = 0;
                for (int k = a; k <= b; k++) {
                    sum += nums[k];
                }
                best = max(best, sum);
            }
        }

        return best;
    }

};

// brute force O(n^2) - Time Limit Exceeded
class Solution {
public:
    int maxSubArray(vector<int> &nums) {
        const int n = nums.size();
        int best = INT_MIN;
        for (int a = 0; a < n; a++) {
            int sum = 0;
            for (int b = a; b < n; b++) {
                sum += nums[b];
                best = max(best, sum);
            }
        }

        return best;
    }

};

// Kadane’s algorithm - O(n)
class Solution {
public:
    int maxSubArray(vector<int> &nums) {
        const int n = nums.size();
        int best = INT_MIN, sum = 0;
        for (int k = 0; k < n; k++) {
            sum = max(nums[k], sum + nums[k]);
            best = max(best, sum);
        }

        return best;
    }

};
