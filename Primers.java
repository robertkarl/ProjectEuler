import java.util.ArrayList;
import java.util.HashSet;
import java.lang.RuntimeException;
public class Primers {

	static HashSet<Integer> sPrimes;

	public static boolean isPrime(int n) {
		if (sPrimes == null) {
			sPrimes = new HashSet<Integer>();
		}
		if (sPrimes.contains(n)) {
			return true;
		}

		if (n < 2) return false;
		if (n == 2) return true;
		if (n % 2 == 0) return false;
		if (n % 3 == 0) return false;

		int max = (int)Math.sqrt((double)n);
		for (int k = 2; 3 * k - 1 <= max; k++) {
			if (n % (3 * k - 1) == 0)
				return false;
			if (n % (3 * k + 1) == 0)
				return false;
		}
		sPrimes.add(n);
		return true;
	}

	public static ArrayList<Integer> getPrimes(int minN, int maxN) {
		ArrayList<Integer> ans = new ArrayList<Integer>();
		for (int i = minN; i <= maxN; i++) {
			if (isPrime(i))
				ans.add(i);
		}
		return ans;
	}

	public static void test() {
		// for (int i = 1000000000; i < 2000000000; i++) {
		// 	System.out.println(String.format("isPrime(%d) = %b", i, isPrime(i)));
		// }

		int[] someVals = new int[]{12344233, 1229, 1339, 1449, 1559, 1669, 1779, 1889, 1999};
		for (int i = 0; i < someVals.length; i++) {
			System.out.println(String.format("isPrime(%d) = %b", someVals[i], isPrime(someVals[i])));
		}


	}

	public static void main(String[] args) {
		int familySize = 8;
		int minPrime = Integer.parseInt(args[0]);
		int maxPrime = Integer.parseInt(args[1]);
		System.out.println(String.format("Searching for primes between %d and %d", minPrime, maxPrime));
		int answer = firstPrimeFamily(familySize, minPrime, maxPrime);
		System.out.println(String.format("Family of size %d starts at %d", familySize, answer));
	}

	public static int firstPrimeFamily(int size, int minN, int maxN) {
		// for each prime of increasing size
		//		for each pair of equivalent digits
		//			for k = (that digit; k <= 9; k++)
		//				count # primes

		ArrayList<Integer> p = getPrimes(minN, maxN);
		System.out.println(String.format("Found %d primes needed.", p.size()));
		for (int i = 0; i < p.size(); i++) {
			int curr = p.get(i);

			String s = String.format("%d", curr);
			for (int x = 0; x < s.length() - 1; x++) {
				for (int y = x + 1; y < s.length() - 1; y++) {
					for (int z = y + 1; z < s.length() - 1; z++) {
						if (s.charAt(x) == s.charAt(y) && s.charAt(x) == s.charAt(z)) {
							int k = s.charAt(x) - '0' + 1;
							int primeFamilyCount = 1;
							int currPrimeFamilyInteger = curr;

							int amountToAdd = 0;
							amountToAdd += (int)Math.pow(10, s.length() - x - 1);
							amountToAdd += (int)Math.pow(10, s.length() - y - 1);
							amountToAdd += (int)Math.pow(10, s.length() - z - 1);

							for (; k <= 9; k++) {
								currPrimeFamilyInteger += amountToAdd;
								if (isPrime(currPrimeFamilyInteger)) {
									primeFamilyCount++;
								}
							}
							if (primeFamilyCount >= 7)
								System.out.println(String.format("For prime %d found family of size %d at indices %d,%d", curr, primeFamilyCount, x, y));
							if (primeFamilyCount == size) {
								return curr;
							}
						}
					}
				}
			}
		}
		return -1;
	}


}
