
public class Enumerate {

	public static void main(String[] args) {
		long a = 0x0f80000000000000l;
		long b = rotate(a);
		long c = rotate(b);
		long d = rotate(c);
		long e = rotate(d);
		System.out.println(a);
		System.out.println(b);
		System.out.println(c);
		System.out.println(d);
		System.out.println(e);

	}
	
	public static long rotate(long l) {
		long ret = 0l;
		for(int i = 59;i>0;i++) {
			long temp1 = (l&(1<<i))>>i;
			long temp2 = temp1 << (i/10+((10-(i%10))*10));
			ret|=temp2;
		}
		System.out.println("a");
		while((ret&0x0802008020080200l)==0l) {
			ret<<=1;
		}
		System.out.println("b");
		while((ret&0x0ffc000000000000l)==0l) {
			ret<<=10;
		}

		System.out.println("c");
		return ret;
	}

}
