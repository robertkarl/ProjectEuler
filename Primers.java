public class Primes {

	static HashSet<Integer> sPrimes;

	public static boolean isPrime(int n) {
		if (sPrimes == null) {
			sPrimes = new HashSet<Integer>();
		}
		if (primes.contains(n)) {
			return true;
		}

		if (i < 2) return false;

		int max = (int)Math.sqrt((double)n);
		for (int i = 2; i <= max; i++) {
			if (n % i == 0)
				return false;
		}
		primes.add(n);
		return true;
	}

	public void test() {
		for (int i = 1; i < 14; i++) {
			System.out.println(String.format("isPrime(%d) = %b", i, isPrime(i)));
		}
	}

	public static void main(String[] args) {
		test();
	}
}