import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.ArrayList;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author lewin
 */
public class Solution {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        DiverseSubarray solver = new DiverseSubarray();
        int testCount = Integer.parseInt(in.next());
        for (int i = 1; i <= testCount; i++)
            solver.solve(i, in, out);
        out.close();
    }

    static class DiverseSubarray {
        int[][] sum;
        int[][] max_psum;

        void update(int level, int index) {
            sum[level][index] = sum[level + 1][2 * index] + sum[level + 1][2 * index + 1];
            max_psum[level][index] = Math.max(
                    max_psum[level + 1][2 * index],
                    sum[level + 1][2 * index] + max_psum[level + 1][2 * index + 1]
            );
        }

        void iset(int level, int index, int value) {
            sum[level][index] = value;
            max_psum[level][index] = value;
            while (level > 0) {
                --level;
                index /= 2;
                update(level, index);
            }
        }

        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int N = in.nextInt(), s = in.nextInt();
            int[] M = in.readIntArray(N);
            int depth = 18;
            sum = new int[depth + 1][];
            for (int l = 0; l <= depth; ++l) sum[l] = new int[1 << l];
            max_psum = new int[depth + 1][];
            for (int l = 0; l <= depth; ++l) max_psum[l] = new int[1 << l];

            HashMap<Integer, ArrayList<Integer>> occurrences
                    = new HashMap<Integer, ArrayList<Integer>>();
            for (int n = 0; n < N; ++n) {
                if (!occurrences.containsKey(M[n])) {
                    occurrences.put(M[n], new ArrayList<Integer>());
                }
                occurrences.get(M[n]).add(n);
            }

            HashMap<Integer, Integer> offsets = new HashMap<Integer, Integer>();
            for (int scene : occurrences.keySet()) offsets.put(scene, 0);

            for (int n = 0; n < (1 << depth); ++n) iset(depth, n, 0);
            for (int scene : occurrences.keySet()) {
                for (int j = 1; j <= s && j - 1 < occurrences.get(scene).size(); j++) {
                    iset(depth, occurrences.get(scene).get(j - 1), +1);
                }
                if (occurrences.get(scene).size() >= s + 1) {
                    iset(depth, occurrences.get(scene).get(s), -s);
                }
            }

            int answer = 0;
            for (int start = 0; start < N; ++start) {
                if (max_psum[0][0] > answer) answer = max_psum[0][0];

                int scene = M[start];
                int off = offsets.get(scene);
                iset(depth, start, 0);

                if (occurrences.get(scene).size() >= s + 1 + off) {
                    iset(depth, occurrences.get(scene).get(s + off), +1);
                }
                if (occurrences.get(scene).size() >= s + 2 + off) {
                    iset(depth, occurrences.get(scene).get(s + 1 + off), -s);
                }
                offsets.put(scene, off + 1);
            }
            out.printf("Case #%d: %d\n", testNumber, answer);
        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1 << 16];
        private int curChar;
        private int numChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int[] readIntArray(int tokens) {
            int[] ret = new int[tokens];
            for (int i = 0; i < tokens; i++) {
                ret[i] = nextInt();
            }
            return ret;
        }

        public int read() {
            if (this.numChars == -1) {
                throw new InputMismatchException();
            } else {
                if (this.curChar >= this.numChars) {
                    this.curChar = 0;

                    try {
                        this.numChars = this.stream.read(this.buf);
                    } catch (IOException var2) {
                        throw new InputMismatchException();
                    }

                    if (this.numChars <= 0) {
                        return -1;
                    }
                }

                return this.buf[this.curChar++];
            }
        }

        public int nextInt() {
            int c;
            for (c = this.read(); isSpaceChar(c); c = this.read()) {
                ;
            }

            byte sgn = 1;
            if (c == 45) {
                sgn = -1;
                c = this.read();
            }

            int res = 0;

            while (c >= 48 && c <= 57) {
                res *= 10;
                res += c - 48;
                c = this.read();
                if (isSpaceChar(c)) {
                    return res * sgn;
                }
            }

            throw new InputMismatchException();
        }

        public String next() {
            int c;
            while (isSpaceChar(c = this.read())) {
                ;
            }

            StringBuilder result = new StringBuilder();
            result.appendCodePoint(c);

            while (!isSpaceChar(c = this.read())) {
                result.appendCodePoint(c);
            }

            return result.toString();
        }

        public static boolean isSpaceChar(int c) {
            return c == 32 || c == 10 || c == 13 || c == 9 || c == -1;
        }

    }

    static class OutputWriter {
        private final PrintWriter writer;

        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer) {
            this.writer = new PrintWriter(writer);
        }

        public void printf(String format, Object... objects) {
            writer.printf(format, objects);
        }

        public void close() {
            writer.close();
        }

    }
}

