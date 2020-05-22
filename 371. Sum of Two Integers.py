class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(math.log((2**a)*(2**b) ,2))
        
    #public int getSum(int a, int b) {
	#if (a == 0) return b;
	#if (b == 0) return a;
    #
	#while (b != 0) {
	#	int carry = a & b;
	#	a = a ^ b;
	#	b = carry << 1;
	#}
	#
	#return a;
    #}