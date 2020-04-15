import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;


public class SixByTen {

	static int count = 0;
	
	public static void main(String [] args) throws FileNotFoundException {
		long t1 = System.currentTimeMillis();
		String poemSRC = "./resources/poem2.txt";
		String solutions = "./resources/10x6solutions.txt";
		ArrayList<Long> words = parseWordsFromFile(poemSRC);
		for(int i = words.size()-1;i>=0;i--) {
			if(countBits(words.get(i))<2){
				words.remove(i);
			}
		}
		findSolutions(solutions, words);
		System.out.println("finished in " + (System.currentTimeMillis()-t1) + " ms");
		System.out.println("found " + count + " solutions");
		
	}
	
	public static void findSolutions(String s, ArrayList<Long> w) throws FileNotFoundException {
		File f = new File(s);
		Scanner in = new Scanner(f);
		while(in.hasNextLine()) {
			String line = "";
			if(!in.hasNext()) {
				break;
			}
			in.next();
			line+=in.next();
			line+=in.next();
			line+=in.next();
			line+=in.next();
			line+=in.next();
			line+=in.next();
			//System.out.println(line);
			long [] tiles = {0l,0l,0l,0l,0l,0l,0l,0l,0l,0l,0l,0l};
			char[] letters = {'F','I','L','Z','V','Y','N','X','T','W','P','U'};
			for(int i = 59;i>=0;i--) {
				tiles[indexOf(letters,line.charAt(59-i))]|=(1l<<i);
			}
			
			     
			//System.out.println();
			boolean p = true;
			for(int i = 0;i<12;i++) {
				for(long word : w) {
					if(((tiles[i]&word)!=0)&&(!covers(tiles[i],word))) {
						p = false;
						break;
					}
				}
			}
			if(p) {
				System.out.println("solution Found!");
				count+=1;
				print(tiles);
			}
		}
		in.close();
	}
	
	public static void print(ArrayList<Long> l) {
		l.forEach(i -> System.out.printf("%x\n", i));
	}
	
	public static void print(long [] a) {
		for(int i = 0;i<a.length;i++) {
			System.out.printf("%16x\n", a[i]);
		}
	}
	
	public static boolean covers(long t, long w) {
		return ((t ^ w) & w) == 0l ? true : false;
	}
	
	public static int indexOf(char[] a,char b) {
		int ret = -1;
		for(int i = 0;i<a.length;i++) {
			if(a[i]==b)
				return i;
		}
		return ret;
	}
	
	public static int countBits(long x) {
		int ans = 0;
		while (x > 0l) {
			ans += (int) (x & 1l);
			x >>= 1;
		}
		return ans;
	}
	
	public static ArrayList<Long> parseWordsFromFile(String src) throws FileNotFoundException {
		ArrayList<Long> words = new ArrayList<Long>();
		File w = new File(src);
		Scanner in = new Scanner(w);
		char curChar = 'A';
		long temp = 0l;
		for (int i = 59; i >= 0; i--) {
			char c = in.next().charAt(0);
			if (c != curChar) {
				curChar++;
				if (c != curChar) {
					System.err.println("poem not formatted correctly at char " + (60 - i));
					System.exit(1);
				}
				words.add(temp);
				temp = 0l;
			}
			temp |= (1l << i);

		}
		words.add(temp);
		in.close();
		return words;
	}
	
	

}
