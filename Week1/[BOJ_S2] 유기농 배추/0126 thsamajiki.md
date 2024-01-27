```
* 풀이

1. 방문한 땅인지 확인하여 모든 땅을 1번씩 방문
2. 방문한 땅에 배추 있는지 여부 판단
    - 배추일 경우: BFS를 사용하여 북동남서 인접한 땅 방문 처리
    - 땅일 경우: 방문 처리

    

* 후기

x, y 좌표 위치를 헷갈릴 수 있으니 주의!
```
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int m, n, k;
    static int[] dx = { -1, 0, 1, 0 };
    static int[] dy = { 0, 1, 0, -1 };
    static int[][] map;
    static boolean[][] visited;

    private void DFS(int x, int y) {
        for (int i = 0; i < 4; i++) {
            int nextX = x + dx[i];
            int nextY = y + dy[i];

            if (nextX < 0 || nextX > n - 1 || nextY < 0 || nextY > m - 1) continue;
            if (map[nextX][nextY] == 1 && !visited[nextX][nextY]) {
                visited[nextX][nextY] = true;
                DFS(nextX, nextY);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < t; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());

            map = new int[n][m];
            visited = new boolean[n][m];

            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                int y = Integer.parseInt(st.nextToken());
                int x = Integer.parseInt(st.nextToken());
                map[x][y] = 1;
            }

            int answer = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (map[i][j] == 1 && !visited[i][j]) {
                        visited[i][j] = true;
                        answer++;
                        main.DFS(i, j);
                    }
                }
            }

            System.out.println(answer);
        }
    }
}
```
