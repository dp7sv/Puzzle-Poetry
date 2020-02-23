import java.util.ArrayList;

public class BruteForce {

	static long b1 = 0x0004010040100401l;
	static long b2 = 0x00000000000003ffl;

	public static void main(String[] args) {

		long word1 = 0x0f80000000000000l;
		long word2 = 0x007c000000000000l;
		long tile1 = 0x0f80000000000000l;
		long tile2 = 0x0f80000000000000l;
		ArrayList<Long> words = new ArrayList<Long>();
		words.add(word1);
		words.add(word2);
		ArrayList<Long> tiles = new ArrayList<Long>();
		tiles.add(tile1);
		tiles.add(tile2);
		
		tile(tiles,words);
		

	}

	public static void tile(ArrayList<Long> t, ArrayList<Long> w) {
		long tile = t.remove(t.size()-1);
		
	}
	
	public static boolean find(long t, long w) {
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 6; j++) {
				long temp = (t >> i) >> (10 * j);

				//System.out.printf("%x %x\n",temp,w);
//				if(((temp&(b1))!=0)||((temp&(b2))!=0)) {
//					continue;
//				}
				if(temp==w) {
					System.out.printf("Match found by shifting tile (%d, %d)\n",i,j);
					return true;
				}
			}
		}
		return false;

	}
	
	public static boolean covers(long t, long w) {
		return ((t^w)&w)==0l?true:false;
	}

}
