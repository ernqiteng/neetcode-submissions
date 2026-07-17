class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] numofcoins = new int[amount+1];
        Arrays.fill(numofcoins, amount + 1);
        numofcoins[0] = 0;
        for (int i=1; i <= amount; i++){
            for (int j=0; j < coins.length; j++){
                if (i-coins[j] >= 0){
                    numofcoins[i] = Math.min(numofcoins[i-coins[j]]+1, numofcoins[i]);
                }
            }
        }
        return numofcoins[amount] != amount+1 ? numofcoins[amount] : -1;
    }
}