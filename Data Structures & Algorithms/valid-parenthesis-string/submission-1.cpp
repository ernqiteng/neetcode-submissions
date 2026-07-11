class Solution {
public:
    bool checkValidString(string s) {
        int leftMin = 0;
        int leftMax = 0;

        for (int c=0; c < size(s); c++){
            if (s[c] == '('){
                leftMin += 1;
                leftMax += 1;
            } else if (s[c] == ')'){
                leftMin -= 1;
                leftMax -= 1;
            } else {
                leftMin -= 1;
                leftMax += 1;
            }
            if (leftMax < 0){
                return false;
            }
            if (leftMin < 0){
                leftMin = 0;
            }
        }
        return leftMin == 0;
    }
};