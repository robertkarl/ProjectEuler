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

		int max = (int)Math.sqrt((double)n);
		for (int i = 2; i <= max; i++) {
			if (n % i == 0)
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
		for (int i = 1000000000; i < 2000000000; i++) {
			System.out.println(String.format("isPrime(%d) = %b", i, isPrime(i)));
		}

	}

	public static void main(String[] args) {
		int familySize = 7;
		int answer = firstPrimeFamily(familySize, 100003000);
		System.out.println(String.format("Family of size %d starts at %d", familySize, answer));
	}


	public static int firstPrimeFamily(int size, int maxN) {
		// for each prime of increasing size
		//		for each pair of equivalent digits
		//			for k = (that digit; k <= 9; k++)
		//				count # primes

		ArrayList<Integer> p = getPrimes(2, maxN);
		for (int i = 0; i < p.size(); i++) {
			int curr = p.get(i);

			String s = String.format("%d", curr);
			for (int x = 0; x < s.length() - 1; x++) {
				for (int y = x + 1; y < s.length() - 1; y++) {
					if (s.charAt(x) == s.charAt(y)) {
						int k = s.charAt(x) - '0' + 1;
						int primeFamilyCount = 1;
						for (; k <= 9; k++) {
							// int amountToAdd = 
							String nextPotentialFamilyMember = replace(s, x, y, k);
							int nextInt = Integer.parseInt(nextPotentialFamilyMember);
							if (isPrime(nextInt)) {
								primeFamilyCount++;
							}
						}
						System.out.println(String.format("For prime %d found family of size %d at indices %d,%d", curr, primeFamilyCount, x, y));
						if (primeFamilyCount == size) {
							return curr;
						}
					}
				}
			}
		}
		return -1;
	}
	/*
		s = 12345
			 x y	
		each time, add 10**(s.length - x - 1)
	*/

	public static String replace(String s, int x, int y, int k) {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < s.length(); i++) {
			if (i == x || i == y) {
				sb.append(k);
			}
			else {
				sb.append(s.charAt(i));
			}

		}
		return sb.toString();
	}

}
