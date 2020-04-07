import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class WordSets {

	public static void main(String[] args) throws FileNotFoundException {

		
		// define path to files containing tiles and poem
		String poemSRC = "./resources/poem1.txt";

		// parsing file into set of words
		ArrayList<Long> words = parseWordsFromFile(poemSRC);
		ArrayList<ArrayList<Long>> tiles = tileSet();

		solve(tiles, words);

		// should exit if solution is found
		System.err.println("a tiling of the poem could not be found");

	}
	
	public static void solve(ArrayList<ArrayList<Long>> tiles, ArrayList<Long> words) {
		ArrayList<ArrayList<Long>> wordSets = generateWordSets(tiles, words);
		
		select(wordSets,0, 0l,"");
	}
	
	public static void select (ArrayList<ArrayList<Long>> wordSets, int level, long board, String sol) {
		if(level==12) {
			System.out.println("Solution found!\n"+sol+"\n");
			System.exit(0);//can be commented out if all solutions are desired
		}else {
			//Location for any optimizations regarding viability of branch given board state
			
			ArrayList<Long> tiles = wordSets.get(level);
			for(long tile:tiles) {
				if ((tile&board)==0l) {
					select(wordSets, level+1, tile|board, sol+" "+tile);
				}
			}
		}
	}
	
	//TODO
	public static ArrayList<ArrayList<Long>> generateWordSets(ArrayList<ArrayList<Long>> tiles, ArrayList<Long> words){
		ArrayList<ArrayList<Long>> ret = new ArrayList<ArrayList<Long>>(tiles.size());
		for(int i = 0;i<tiles.size();i++) {
			ret.add(new ArrayList<Long>());
		}
		ArrayList<wordSet> allSets = new ArrayList<wordSet>();
		addWordSets(allSets, words, 0l);
		
		return ret;
	}
	
	//TODO
	public static void addWordSets(ArrayList<wordSet> sets, ArrayList<Long> words, long curSet) {
		wordSet temp = new wordSet();
		temp.add(curSet);
		
	}
	
	
	/**
	 * Parses input file to return representation of each word as a Long
	 * 
	 * @param src String representing path to file containing poem
	 * @return ArrayList of Longs representing all words in poem
	 * @throws FileNotFoundException
	 */
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
	
	public static ArrayList<ArrayList<Long>> tileSet() throws FileNotFoundException {
		File ti = new File("./resources/allTilesOrdered.txt");
		Scanner in = new Scanner(ti);

		ArrayList<Long> O = new ArrayList<Long>();
		ArrayList<Long> P = new ArrayList<Long>();
		ArrayList<Long> Q = new ArrayList<Long>();
		ArrayList<Long> R = new ArrayList<Long>();
		ArrayList<Long> S = new ArrayList<Long>();
		ArrayList<Long> T = new ArrayList<Long>();
		ArrayList<Long> U = new ArrayList<Long>();
		ArrayList<Long> V = new ArrayList<Long>();
		ArrayList<Long> W = new ArrayList<Long>();
		ArrayList<Long> X = new ArrayList<Long>();
		ArrayList<Long> Y = new ArrayList<Long>();
		ArrayList<Long> Z = new ArrayList<Long>();

		for (int i = 0; i < 2; i++) {
			O.add(in.nextLong(16));
		}
		for (int i = 0; i < 8; i++) {
			P.add(in.nextLong(16));
		}
		for (int i = 0; i < 8; i++) {
			Q.add(in.nextLong(16));
		}
		for (int i = 0; i < 8; i++) {
			R.add(in.nextLong(16));
		}
		for (int i = 0; i < 8; i++) {
			S.add(in.nextLong(16));
		}
		for (int i = 0; i < 4; i++) {
			T.add(in.nextLong(16));
		}
		for (int i = 0; i < 4; i++) {
			U.add(in.nextLong(16));
		}
		for (int i = 0; i < 4; i++) {
			V.add(in.nextLong(16));
		}
		for (int i = 0; i < 4; i++) {
			W.add(in.nextLong(16));
		}
		for (int i = 0; i < 1; i++) {
			X.add(in.nextLong(16));
		}
		for (int i = 0; i < 8; i++) {
			Y.add(in.nextLong(16));
		}
		for (int i = 0; i < 4; i++) {
			Z.add(in.nextLong(16));
		}
		in.close();
		ArrayList<ArrayList<Long>> ret = new ArrayList<ArrayList<Long>>();
		ret.add(X);
		ret.add(O);
		ret.add(T);
		ret.add(U);
		ret.add(V);
		ret.add(W);
		ret.add(Z);
		ret.add(P);
		ret.add(Q);
		ret.add(R);
		ret.add(S);
		ret.add(Y);

		return ret;
	}
}
class wordSet{
	ArrayList<Long> words;
	long area;
	long shiftedArea;
	long adjacency; 
	int size;
	wordSet(){
		//words = new ArrayList<Long>();
		area = 0l;
		adjacency = 0l;
		size = 0;
		shiftedArea = 0l;
	}
	void add(long word) {
		if((word&area)==0l) {
			//words.add(word);
			area|=word;
			long temp1 = (area&(~0x0ffc000000000000l))<<10;
			long temp2 = (area&(~0x00000000000003ffl))>>10;
			long temp3 = (area&(~0x0802008020080200l))<<1;
			long temp4 = (area&(~0x0004010040100401l))>>1;
			adjacency = (temp1|temp2|temp3|temp4)&(~area);
			size += countBits(word);
		}
	}
	
	void shift() {
		shiftedArea = area;
		while((shiftedArea&0x0ffc000000000000l)==0) {
			shiftedArea<<=10;
		}
		while((shiftedArea&0x0802008020080200l)==0) {
			shiftedArea<<=1;
		}
	}
	
	int findMatch(ArrayList<ArrayList<Long>> tiles) {
		shift();
		int ret = -1;
		for(int i = 0;i<tiles.size();i++) {
			ArrayList<Long> tile = tiles.get(i);
			for(long t:tile) {
				if (shiftedArea==t) {
					return i;
				}
			}
		}
		return ret;
	}
	
	//I might need to make a better hashcode
	public int hashCode() {
		return Long.hashCode(area);
	}
	
	private static int countBits(long x) {
		int ans = 0;
		while (x > 0l) {
			ans += (int) (x & 1l);
			x >>= 1;
		}
		return ans;
	}
}
