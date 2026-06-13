class Solution {
    public double myPow(double x, int n) {
        if (n == 0){
            return 1;
        }

        int power = 0;
        if (n > 0){
            power = n;
        } else {
            power = -n;
        }

        double num = x;
        int count = 1;

        while (count != power){
            num = num*x;
            count++;
        }
        if (n > 0){
            return num;
        }
        return 1/num;
    }
};