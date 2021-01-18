class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int sum;
        vector<int> answer;
        int n, target2;
        
        for (int i = 0; i < nums.size()-1; i++)
        {
            n = nums[i];
            target2 = target - n;
            for (int j = i+1; j<nums.size(); j++)
            {
                if (nums[j] == target2){
                    answer.push_back(i);
                    answer.push_back(j);
                    return answer;
                }
                else if (nums[j] + nums[j-1] == target){
                    answer.push_back(j-1);
                    answer.push_back(j);
                    return answer;    
                }
            }
        }
        return answer;
    }
};
