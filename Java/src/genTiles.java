import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class genTiles {

	public static void main(String[] args) throws Throwable {

		String tileSRC = "./resources/tiles1.txt";
		ArrayList<Long> tiles = parseTilesFromFile(tileSRC);
		ArrayList<ArrayList<Long>> T = moreTiles(tiles);
		tiles.forEach(t->System.out.printf("%x\n", t));
		System.out.println();
		T.forEach(a -> a.forEach(b -> System.out.printf("%x\n", b)));
		
		String out = "./resources/Pentominoes.txt";
		PrintWriter writer = new PrintWriter(out, "UTF-8");
		for(var t:T) {
			for (long a : t) {
				writer.printf("%x\n",a);
			}writer.println();
			
		}
		writer.close();
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
	
	public static ArrayList<ArrayList<Long>> moreTiles(ArrayList<Long> tiles) {
		ArrayList<ArrayList<Long>> ret = new ArrayList<ArrayList<Long>>();
		tiles.forEach(t -> ret.add(configs(t)));
		return ret;
	}
	public static ArrayList<Long> configs(long t){
		ArrayList<Long> ret = new ArrayList<Long>();
		ret.add(t);
		boolean [][]a = toArray(t);
		print(a);
		System.out.println();
		a = rotate(a);
		
		t=toTopCorner(toLong(a));
		if(!ret.contains(t)) {
			ret.add(t);
		}
		a = rotate(a);
		t=toTopCorner(toLong(a));
		if(!ret.contains(t)) {
			ret.add(t);
		}
		a = rotate(a);
		t=toTopCorner(toLong(a));
		if(!ret.contains(t)) {
			ret.add(t);
		}
		a = flip(a);
		print(a);
		System.out.println();
		t=toTopCorner(toLong(a));
		if(!ret.contains(t)) {
			ret.add(t);
		}
		a = rotate(a);
		t=toTopCorner(toLong(a));
		if(!ret.contains(t)) {
			ret.add(t);
		}
		a = rotate(a);
		t=toTopCorner(toLong(a));
		if(!ret.contains(t)) {
			ret.add(t);
		}
		a = rotate(a);
		t=toTopCorner(toLong(a));
		if(!ret.contains(t)) {
			ret.add(t);
		}
		return ret;
	}
	public static boolean [][] rotate(boolean [][] a){
		boolean [][] ret = new boolean[5][5];
		for(int i = 0;i<5;i++) {
			for(int j = 0;j<5;j++) {
				ret[i][j]=a[j][4-i];
			}
		}
		return ret;
	}
	
	public static boolean [][] flip(boolean [][] a){
		boolean [][] ret = new boolean[5][5];
		for(int i = 0;i<5;i++) {
			for(int j = 0;j<5;j++) {
				ret[i][j]=a[i][4-j];
			}
		}
		return ret;
	}
	
	public static long toTopCorner(long t) {
		while((t&0x0ffc000000000000l)==0l) {
			t<<=10;
		}
		while((t&0x0802008020080200l)==0l) {
			t<<=1;
		}
		return t;
	}
	
	
	public static boolean [][] toArray(long t){
		boolean [][] ret = new boolean[5][5];
		for(int i = 0;i<5;i++) {
			for(int j = 0;j<5;j++) {
				ret[i][j]=((t>>(59-(10*i+j))&1l)==1l);
			}
		}
		return ret;
	}
	public static long toLong (boolean [][] a) {
		long ret = 0l;
		for(int i = 0;i<5;i++) {
			for(int j = 0;j<5;j++) {
				if(a[i][j]) {
					ret|=(1l<<(59-(10*i+j)));
				}
			}
		}
		return ret;
	}
	public static void print(boolean[][]a) {
		for(int i = 0;i<5;i++) {
			for(int j = 0;j<5;j++) {
				System.out.print(""+(a[i][j]?"+":" "));
			}
			System.out.println();
		}
	}

}
