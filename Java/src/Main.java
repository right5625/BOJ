import java.io.*;

public class Main {
    static BufferedReader br;
    static BufferedWriter bw;

    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int X = Integer.parseInt(br.readLine());
        bw.write(String.valueOf(solution(X)));
        bw.flush();
        br.close();
        bw.close();
    }

    static int solution(int X) {
        int result = 0;
        while (X != 0) {
            int cur = 1;
            while (cur * 2 <= X) {
                cur *= 2;
            }
            X -= cur;
            result++;
        }
        return result;
    }
}