import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class SixthOptimize {

	static int count = 0;
	static int block_depth = 12;

	public static void main(String[] args) throws Throwable {

		String out = "./resources/test_sol_5.txt";
		PrintWriter writer = new PrintWriter(out, "UTF-8");
		for (; block_depth >= 0; block_depth--) {
			long t1 = System.currentTimeMillis();
			String poemSRC = "./resources/poem1.txt";
			ArrayList<Long> words = parseWordsFromFile(poemSRC);
			ArrayList<ArrayList<Long>> p = Pentominoes();
			for (int i = words.size() - 1; i >= 0; i--) {
				if (countBits(words.get(i)) < 2) {
					words.remove(i);
				}
			}
			words.clear();
			solve(p, words, writer);

			writer.println("finished in " + (System.currentTimeMillis() - t1) + " ms with block_depth " + block_depth);
			writer.println("found " + count + " solutions");
			// should exit if solution is found
			writer.println("a(nother) tiling of the poem could not be found");
		}
		writer.close();

	}

	public static void solve(ArrayList<ArrayList<Long>> tiles, ArrayList<Long> words, PrintWriter writer) {
		ArrayList<ArrayList<Long>> allTiles = shifts(tiles, words);

		allTiles.forEach(t -> System.out.println(t.size()));

		select(allTiles, 0, 0l, "", writer);
	}

	public static void select(ArrayList<ArrayList<Long>> wordSets, int level, long board, String sol,
			PrintWriter writer) {
		if (level == 12) {
			//System.out.println("Solution found!\n" + sol + "\n");
			//writer.println("Solution found!\n" + sol + "\n");
			count++;
			// System.exit(0);// can be commented out if all solutions are desired
		} else {
			// Location for any optimizations regarding viability of branch given board
			// state

			ArrayList<Long> tiles = wordSets.get(level);
			for (long tile : tiles) {
				if ((tile & board) == 0l && fiveOpen(tile | board)) {
					ArrayList<ArrayList<Long>> blocked = new ArrayList<ArrayList<Long>>();
					for (int i = level + 1; i < block_depth; i++) {
						ArrayList<Long> options = wordSets.get(i);
						ArrayList<Long> temp = new ArrayList<Long>();
						for (int j = options.size(); j-- > 0;) {
							long temp2 = options.get(j);
							if ((temp2 & tile) != 0l) {
								options.remove(j);
								temp.add(temp2);
							}
						}
						blocked.add(temp);
					}
					select(wordSets, level + 1, tile | board, sol + " " + Long.toString(tile, 16), writer);
					for (int i = level + 1; i < block_depth; i++) {
						ArrayList<Long> options = wordSets.get(i);
						options.addAll(blocked.get(i - level - 1));
					}
				}
			}
		}
	}

	public static ArrayList<ArrayList<Long>> shifts(ArrayList<ArrayList<Long>> t, ArrayList<Long> w) {
		ArrayList<ArrayList<Long>> ret = new ArrayList<ArrayList<Long>>();
		for (var T : t) {
			ArrayList<Long> l = new ArrayList<Long>();
			for (long tile : T) {
				int iMax = maxLeftShift(tile);
				int jMax = maxDownShift(tile);
				for (int j = 0; j <= jMax; j++) {
					for (int i = 0; i <= iMax; i++) {
						long temp = (tile >> i) >> (10 * j);
						boolean add = true;
						for (int k = w.size() - 1; k >= 0; k--) {
							long word = w.get(k);
							if ((temp & word) != 0) {
								if (!covers(temp, word)) {
									add = false;
								}
							}
						}
						if (add && fiveOpen(temp)) {
							l.add(temp);
						}
					}
				}
			}
			ret.add(l);
		}
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

	public static ArrayList<ArrayList<Long>> Pentominoes() throws FileNotFoundException {
		ArrayList<ArrayList<Long>> ret = new ArrayList<ArrayList<Long>>();
		String src = "./resources/Pentominoes.txt";
		File f = new File(src);
		Scanner in = new Scanner(f);
		ArrayList<Long> temp = new ArrayList<Long>();
		while (in.hasNextLine()) {
			String s = in.nextLine();
			if (s.equals("")) {
				ret.add(temp);
				temp = new ArrayList<Long>();
			} else {
				temp.add(Long.parseLong(s, 16));
			}
		}
		return ret;
	}

	public static boolean covers(long t, long w) {
		return ((t ^ w) & w) == 0l ? true : false;
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

	public static boolean fiveOpen(long x) {
		x |= 0xf000000000000000l;
		while (x != 0xffffffffffffffffl) {
			long temp0 = 0l;
			long temp1 = 1l;
			while (!((temp1 & x) == 0)) {
				temp1 <<= 1l;
			}
			while (temp0 != temp1) {
				temp0 = temp1;
				long temp5 = (temp0 & (~0x0ffc000000000000l)) << 10;
				long temp2 = (temp0 & (~0x00000000000003ffl)) >> 10;
				long temp3 = (temp0 & (~0x0802008020080200l)) << 1;
				long temp4 = (temp0 & (~0x0004010040100401l)) >> 1;
				temp1 = ((temp5 | temp2 | temp3 | temp4) | (temp0)) & (~x);
			}
			if (!(countBits(temp1) % 5 == 0)) {
				return false;
			}
			x |= temp1;

		}
		return true;

	}

}
