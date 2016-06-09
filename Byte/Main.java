import static java.lang.System.out;

public class Main {
    public static void main(String[] args) {
        Sfmt sfmt = new Sfmt(256);
        long start = System.currentTimeMillis();
        int max = 1000000;
        while(true) {
            if (max == 0) {
                break;
            }
            int counter = 0;
            byte num = (byte) sfmt.NextInt(256);
            String[] nums = Integer.toBinaryString(num).split("");
            for (int i = 0; i < nums.length; i++) {
                if (nums[i].equals("1")) {
                    counter += 1;
                }
            }
            max--;
        }
        long end = System.currentTimeMillis();
        System.out.printf("経過時間: %.4f\n",(double)(end - start) / 1000);

        String[] memoCount = {  "25", "26", "26", "27", "26", "27", "27", "28", "26", "27", "27", "28", "27", "28", "28", "29", "26", "27", "27", "28", "27", "28", "28", "29", "27", "28", "28", "29", "28", "29", "29", "30", "26", "27", "27", "28", "27", "28", "28", "29", "27", "28", "28", "29", "28", "29", "29", "30", "27", "28", "28", "29", "28", "29", "29", "30", "28", "29", "29", "30", "29", "30", "30", "31", "26", "27", "27", "28", "27", "28", "28", "29", "27", "28", "28", "29", "28", "29", "29", "30", "27", "28", "28", "29", "28", "29", "29", "30", "28", "29", "29", "30", "29", "30", "30", "31", "27", "28", "28", "29", "28", "29", "29", "30", "28", "29", "29", "30", "29", "30", "30", "31", "28", "29", "29", "30", "29", "30", "30", "31", "29", "30", "30", "31", "30", "31", "31", "32",  "0",  "1",  "1",  "2",  "1",  "2",  "2",  "3",  "1",  "2",  "2",  "3",  "2",  "3",  "3",  "4",  "1",  "2",  "2",  "3",  "2",  "3",  "3",  "4",  "2",  "3",  "3",  "4",  "3",  "4",  "4",  "5",  "1",  "2",  "2",  "3",  "2",  "3",  "3",  "4",  "2",  "3",  "3",  "4",  "3",  "4",  "4",  "5",  "2",  "3",  "3",  "4",  "3",  "4",  "4",  "5",  "3",  "4",  "4",  "5",  "4",  "5",  "5",  "6",  "1",  "2",  "2",  "3",  "2",  "3",  "3",  "4",  "2",  "3",  "3",  "4",  "3",  "4",  "4",  "5",  "2",  "3",  "3",  "4",  "3",  "4",  "4",  "5",  "3",  "4",  "4",  "5",  "4",  "5",  "5",  "6",  "2",  "3",  "3",  "4",  "3",  "4",  "4",  "5",  "3",  "4",  "4",  "5",  "4",  "5",  "5",  "6",  "3",  "4",  "4",  "5",  "4",  "5",  "5",  "6",  "4",  "5",  "5",  "6",  "5",  "6",  "6",  "7", };

        start = System.currentTimeMillis();
        max = 1000000;
        while(true) {
            if(max == 0) {
                break;
            }
            byte num = (byte) sfmt.NextInt(256);
            String ans = memoCount[num + 128];
            max--;
        }
        end = System.currentTimeMillis();
        System.out.printf("経過時間: %.4f\n",(double)(end - start) / 1000);

        /*
        String[] memoCount = new String[256];
        for (int i = -128; i < 128; i++) {
            byte num = (byte) i;
            int counter = 0;
            String[] nums = Integer.toBinaryString(num).split("");
            for (int j = 0; j < nums.length; j++) {
                if (nums[j].equals("1")) {
                    counter += 1;
                }
            }
            memoCount[i + 128] = String.valueOf(counter);
        }
        out.print("{ ");
        for (String str: memoCount) {
            out.printf("%3s,", str);
        }
        out.println(" }");
        */
    }
}

abstract class CountByte {
    int decimalNum;
    String binaryNum;
    int counter;
    CountByte(int decimalNum) {
        this.decimalNum = decimalNum;
    }

    private void convertByte(int deciamlNum) {
        this.binaryNum = Integer.toBinaryString(decimalNum);
    }

    private String getBinaryNum() {
        convertByte(decimalNum);
        return binaryNum;
    }

    abstract int countByte(String binaryNum);

    public String toString() {
        return String.valueOf(countByte(getBinaryNum()));
    }
}

class SplitCountByte extends CountByte {
    SplitCountByte (int decimalNum) {
        super(decimalNum);
    }
    @Override
    int countByte(String binaryNum) {
        counter = 0;
        String[] binaryNums = binaryNum.split("");
        for (int i = 0; i < binaryNums.length; i += 1) {
            if (binaryNums[i].equals("1")) {
                counter += 1;
            }
        }

        return counter;
    }
}
