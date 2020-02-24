import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class BruteForce {

	static long b1 = 0x0004010040100401l;
	static long b2 = 0x00000000000003ffl;

	public static void main(String[] args) throws FileNotFoundException {
		
		String poemSRC = "./resources/poem1.txt";
		String tileSRC = "./resources/tiles1.txt";
		
		//parsing file into set of words
		ArrayList<Long> words = new ArrayList<Long>();
		File w = new File(poemSRC);
		Scanner in = new Scanner(w);
		char curChar = 'A';
		long temp = 0l;
		for(int i = 59;i>=0;i--) {
			char c = in.next().charAt(0);
			if(c!=curChar) {
				curChar++;
				if(c!=curChar) {
					System.err.println("poem not formatted correctly at char "+(60 - i));
					System.exit(1);
				}
				words.add(temp);
				temp = 0l;
			}
			temp|=(1l<<i);
			
		}
		words.add(temp);
		in.close();

		//print out each word for testing
		//words.forEach(i -> System.out.printf("%x\n", i));
		
		//scan in tiles from file
		ArrayList<Long> tiles = new ArrayList<Long>();
		File t = new File(tileSRC);
		in = new Scanner(t);
		while(in.hasNext()) {
			tiles.add(in.nextLong(16));
		}
		in.close();
		
		//print out each word for testing
		tiles.forEach(i -> System.out.printf("%x\n", i));
		
	
		tile(tiles,words);
		

	}

	public static void tile(ArrayList<Long> t, ArrayList<Long> w) {
		long tile = t.remove(t.size()-1);
		
		
	}
	
	public static boolean find(long t, ArrayList<Long> w) {
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 6; j++) {
				long temp = (t >> i) >> (10 * j);
				
				
			}
		}
		return false;

	}
	
	public static boolean covers(long t, long w) {
		return ((t^w)&w)==0l?true:false;
	}

}
