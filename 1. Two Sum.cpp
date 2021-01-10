// brute force O(n^2)
class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        const int n = nums.size();
        int a, b;

        for (int i = 0; i < n; i++) {
            a = nums[i];
            for (int j = i + 1; j < n; j++) {
                b = nums[j];
                if ((a + b) == target) {
                    return {i, j};
                }
            }
        }
        return {0, 0};
    }
};

// with hashmap O(n) 
class Solution {
public:
vector<int> twoSum(vector<int> &nums, int target) {
    map<int, int> table;
    for (int i = 0; i < nums.size(); i++) {
        int diff = target - nums[i];
        if (table.count(nums[i])) {
            return {table[nums[i]], i};
        }
        table[diff] = i;
    }
    return {0, 0};
}

};
