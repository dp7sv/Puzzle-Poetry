import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;


//doesn't work
public class FirstOptimize {

	public static void main(String[] args) throws FileNotFoundException {

		String poemSRC = "./resources/poem1.txt";

		ArrayList<ArrayList<Long>> allTiles = tileSet();
		ArrayList<Long> words = parseWordsFromFile(poemSRC);
		tile(allTiles, words, "");

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

	public static void tile(ArrayList<ArrayList<Long>> t, ArrayList<Long> w, String p) {
		
//		try {
//			Thread.sleep(100);
//		} catch (InterruptedException e) {
//			e.printStackTrace();
//		}
		
		ArrayList<Long> tiles = t.remove(t.size() - 1);
		if (t.size() == 0) {
			System.out.println("here");
		}
		for (long tile : tiles) {
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
							t.add(tiles);
							return;
						} else if (w.isEmpty()) {
							System.err.println("too many tiles");
							w.addAll(usedWords);
							usedWords.clear();
							t.add(tiles);
							return;
						} else {
							//System.out.println("Placed tile " + (12 - t.size()) + " (0x" + Long.toHexString(tile)
									//+ ") at (" + i + ", " + j + ")");
							tile(t, w, p + "Shift tile " + (12 - t.size()) + " (0x" + Long.toHexString(tile) + ") by ("
									+ i + ", " + j + ")\n");
							w.addAll(usedWords);
							usedWords.clear();
							continue;
						}
					}

				}
			}
		}
		t.add(tiles);
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
	 * returns true iff tile t completely covers word w
	 * 
	 * @param t Long used to represent a tile
	 * @param w Long used to represent a word
	 * @return
	 */
	public static boolean covers(long t, long w) {
		return ((t ^ w) & w) == 0l ? true : false;
	}

}
