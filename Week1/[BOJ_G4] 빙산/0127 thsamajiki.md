```
* 풀이

1. 입력이 모두 0일 경우를 고려한다.
2. 모두 0이 아니면, 무조건 한 덩어리가 입력으로 주어지므로 모든 배열을 돌며 각 얼음을 녹일 갯수를 세어 저장한다.
3. 다시 한번 더 돌며 빙산을 녹여 없앤다.
4. BFS를 수행하여 빙산의 개수를 세고 하나의 빙산이라면 2를 다시 수행한다.


* 후기

x, y 좌표 위치를 헷갈릴 수 있으니 주의!
```
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Iceberg {
    int r, c;

    public Iceberg(int r, int c) {
        super();
        this.r = r;
        this.c = c;
    }
}

public class Main {
    static int N, M;
    static int answer;
    static int[][] map;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        int[][] melt = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (true) {
            for (int i = 0; i < N; i++) {
                Arrays.fill(visited[i], false);
                Arrays.fill(melt[i], 0);
            }

            int count = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (map[i][j] > 0 && !visited[i][j]) {
                        main.BFS(i, j);
                        count++;
                    }
                }
            }

            if (count > 1)
                break;
            else if (count == 0) {
                answer = 0;
                break;
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (map[i][j] > 0) {
                        for (int step = 0; step < 4; step++) {
                            int nextR = i + dx[step];
                            int nextC = j + dy[step];
                            if (nextR >= 0 && nextR < N && nextC >= 0 && nextC < M && map[nextR][nextC] < 1) {
                                melt[i][j]++;
                            }
                        }
                    }

                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    map[i][j] -= melt[i][j];
                }
            }
            answer++;
        }

        System.out.println(answer);
    }

    public void BFS(int r, int c) {
        Queue<Iceberg> q = new LinkedList<>();
        q.offer(new Iceberg(r, c));
        visited[r][c] = true;

        while (!q.isEmpty()) {
            Iceberg temp = q.poll();

            for (int i = 0; i < 4; i++) {
                int nextR = temp.r + dx[i];
                int nextC = temp.c + dy[i];

                if (nextR >= 0 && nextR < N && nextC >= 0 && nextC < M && !visited[nextR][nextC] && map[nextR][nextC] > 0) {
                    q.offer(new Iceberg(nextR, nextC));
                    visited[nextR][nextC] = true;
                }
            }
        }
    }
}
```
