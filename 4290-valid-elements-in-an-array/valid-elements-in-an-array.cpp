class Solution {
public:
    vector<int> findValidElements(vector<int>& nums) {
        int n = nums.size();
        int left_greatest = INT_MIN;
        int right_greatest = INT_MIN;
        vector<bool> valid(n, false);
        vector<int> result;

        // left pass
        for(int i=0; i<n; i++){
            if(nums[i]>left_greatest){
                valid[i] = true;
                left_greatest = nums[i];
            }
        }

        // right pass
        for(int i=n-1; i>=0; i--){
            if(nums[i]>right_greatest){
                valid[i] = true;
                right_greatest = nums[i];
            }
        }

        for(int i=0; i<n; i++){
            if(valid[i]) result.push_back(nums[i]);
        }

        return result;
    }
};