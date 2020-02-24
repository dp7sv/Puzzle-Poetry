import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class BruteForce {

	public static void main(String[] args) throws FileNotFoundException {

		String poemSRC = "./resources/poem1.txt";
		String tileSRC = "./resources/tiles1.txt";

		// parsing file into set of words
		ArrayList<Long> words = parseWordsFromFile(poemSRC);

		// print out each word for testing
		//words.forEach(i -> System.out.printf("%x\n", i));

		// scan in tiles from file
		ArrayList<Long> tiles = parseTilesFromFile(tileSRC);

		// print out each word for testing
		//tiles.forEach(i -> System.out.printf("%x\n", i));

		tile(tiles, words, "");

	}

	public static void tile(ArrayList<Long> t, ArrayList<Long> w, String p) {
		long tile = t.remove(t.size() - 1);
		int iMax = maxLeftShift(tile);
		int jMax = maxDownShift(tile);
		for (int j = 0; j <= jMax; j++) {
			for (int i = 0; i <= iMax; i++) {
				long temp = (tile >> i) >> (10 * j);
				ArrayList<Long> usedWords = new ArrayList<Long>();
				for (int k = w.size() - 1; k >= 0; k--) {
					long word = w.get(k);
					if ((temp & word) != 0) {
						if (!covers(temp, word)) {
							break;
						} else {
							w.remove(k);
							usedWords.add(word);
							temp ^= word;
						}
					}

				}
				if (temp == 0l) {
					if (t.isEmpty() && w.isEmpty()) {
						System.out.println(p);
						System.exit(0);
					} else if (t.isEmpty()) {
						System.err.println("not enough tiles");
						//System.exit(1);
					} else if (t.isEmpty()) {
						System.err.println("too many tiles");
						//System.exit(1);
					} else {
						System.out.println("Placed tile " + (12 - t.size()) + " at (" + i + ", " + j + ")");
						tile(t, w, p + "Shift tile " + (12 - t.size()) + " by (" + i + ", " + j + ")\n");
					}

				}
				// System.out.println("here " + p);
				w.addAll(usedWords);

			}
		}

	}

	public static boolean covers(long t, long w) {
		return ((t ^ w) & w) == 0l ? true : false;
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

}
