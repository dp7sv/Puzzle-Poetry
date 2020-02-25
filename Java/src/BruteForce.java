import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class BruteForce {

	public static void main(String[] args) throws FileNotFoundException {

		// define path to files containing tiles and poem
		String poemSRC = "./resources/poem1.txt";
		String tileSRC = "./resources/tiles1.txt";

		// parsing file into set of words
		ArrayList<Long> words = parseWordsFromFile(poemSRC);

		// print out each word for testing
		// words.forEach(i -> System.out.printf("%x\n", i));

		// scan in tiles from file
		ArrayList<Long> tiles = parseTilesFromFile(tileSRC);

		// print out each word for testing
		// tiles.forEach(i -> System.out.printf("%x\n", i));

		// method for randomizing order of tiles used for testing
		// shuffle(tiles);

		tile(tiles, words, "");

		// should exit if solution is found
		System.err.println("a tiling of the poem could not be found");

	}

	/**
	 * Recursive method used to find a valid placement of a tile and then recurse
	 * with the remainder of tiles and words not covered by the placed tile
	 * 
	 * @param t ArrayList of Longs representing the tiles to be placed
	 * @param w ArrayList of Longs representing the words yet to be covered by tiles
	 * @param p String used to store successful placements of tiles
	 */
	public static void tile(ArrayList<Long> t, ArrayList<Long> w, String p) {
		long tile = t.remove(t.size() - 1);
		int iMax = maxLeftShift(tile);
		int jMax = maxDownShift(tile);
		for (int j = 0; j <= jMax; j++) {
			for (int i = 0; i <= iMax; i++) {
				long temp = (tile >> i) >> (10 * j);
				ArrayList<Long> usedWords = new ArrayList<Long>();
				for (int k = w.size() - 1; k >= 0; k--)
					here: {
						long word = w.get(k);
						if ((temp & word) != 0) {
							if (!covers(temp, word)) {
								break here;
							} else {
								w.remove(k);
								usedWords.add(word);
								temp ^= word;
								if (temp == 0l) {
									break here;
								}
							}
						}

					}
				if (temp != 0l) {
					w.addAll(usedWords);
					usedWords.clear();
					continue;
				}
				if (temp == 0l) {
					if (t.isEmpty() && w.isEmpty()) {
						System.out.println(p + "Shift tile " + (12 - t.size()) + " (0x" + Long.toHexString(tile)
								+ ") by (" + i + ", " + j + ")\n");
						System.exit(0);
					} else if (t.isEmpty()) {
						System.err.println("not enough tiles");
						w.addAll(usedWords);
						usedWords.clear();
						t.add(tile);
						return;
					} else if (w.isEmpty()) {
						System.err.println("too many tiles");
						w.addAll(usedWords);
						usedWords.clear();
						t.add(tile);
						return;
					} else {
						// System.out.println("Placed tile " + (12 - t.size()) + " at (" + i + ", " + j
						// + ")");
						tile(t, w, p + "Shift tile " + (12 - t.size()) + " (0x" + Long.toHexString(tile) + ") by (" + i
								+ ", " + j + ")\n");
						w.addAll(usedWords);
						usedWords.clear();
						continue;
					}
				}

			}
		}
		t.add(tile);
	}

	/**
	 * returns true iff tile t completely covers word w
	 * 
	 * @param t Long used to represent a tile
	 * @param w Long used to represent a word
	 * @return
	 */
	public static boolean covers(long t, long w) {
		return ((t ^ w) & w) == 0l ? true : false;
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

	/**
	 * Parses input file to return representation of each tile as a Long
	 * 
	 * @param src String representing path to file containing tiles to be placed
	 * @return ArrayList of Longs representing all tiles to be placed
	 * @throws FileNotFoundException
	 */
	public static ArrayList<Long> parseTilesFromFile(String src) throws FileNotFoundException {
		ArrayList<Long> tiles = new ArrayList<Long>();
		File t = new File(src);
		Scanner in = new Scanner(t);
		while (in.hasNext()) {
			tiles.add(in.nextLong(16));
		}
		in.close();
		return tiles;
	}

	/**
	 * returns how far a tile can be shifted to the left without overflow
	 * 
	 * @param l tile to be shifted
	 * @return maximum number of left-shifts before tile would overflow
	 */
	public static int maxLeftShift(long l) {
		int ret = 9;
		long mask1 = 0x0401004010040100l;
		long mask2 = 0x0200802008020080l;
		long mask3 = 0x0100401004010040l;
		long mask4 = 0x0080200802008020l;
		return (l & mask1) != 0
				? (l & mask2) != 0 ? (l & mask3) != 0 ? (l & mask4) != 0 ? ret - 4 : ret - 3 : ret - 2 : ret - 1
				: ret;
	}

	/**
	 * returns how far a tile can be shifted down without overflow
	 * 
	 * @param l tile to be shifted
	 * @return maximum number of down-shifts before tile would overflow
	 */
	public static int maxDownShift(long l) {
		int ret = 5;
		long mask1 = 0x0003ff0000000000l;
		long mask2 = 0x000000ffc0000000l;
		long mask3 = 0x000000003ff00000l;
		long mask4 = 0x00000000000ffc00l;
		return (l & mask1) != 0
				? (l & mask2) != 0 ? (l & mask3) != 0 ? (l & mask4) != 0 ? ret - 4 : ret - 3 : ret - 2 : ret - 1
				: ret;
	}

	/**
	 * method used in testing to count number of 1s in a long
	 * 
	 * @param x long to be analyzed
	 * @return number of 1s in binary representation of x
	 */
	public static int countBits(long x) {
		int ans = 0;
		while (x > 0l) {
			ans += (int) (x & 1l);
			x >>= 1;
		}
		return ans;
	}

	/**
	 * method used in testing to shuffle an ArrayList of Longs
	 * 
	 * @param l ArrayList of longs to be shuffled
	 */
	public static void shuffle(ArrayList<Long> l) {
		l.sort((i, j) -> (int) (Math.random() * 50 - 25));
	}

}
