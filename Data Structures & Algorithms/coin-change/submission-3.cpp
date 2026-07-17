class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> numofcoins(amount+1, amount+1);
        numofcoins[0] = 0;
        for (int i=1; i <= amount; i++){
            for (int j=0; j < coins.size(); j++){
                if (i-coins[j] >= 0){
                    numofcoins[i] = min(numofcoins[i-coins[j]]+1, numofcoins[i]);
                }
            }
        }
        return numofcoins[amount] != amount+1 ? numofcoins[amount] : -1;
    }
};