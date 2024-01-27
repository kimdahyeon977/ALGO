```
* 2차원 문제에서 3차원으로 사고를 확장하는 문제

* 풀이

1. 저장될 때부터 모든 토마토가 익어있는지 확인
2. 익은 토마토를 큐에 넣기 -> BFS 해서 토마토 익히기 + 날짜 세기
3. 익은 토마토를 새로운 큐에 넣어서 BFS 반복하기
    -> 즉, 익을 수 있는 모든 토마토을 익히기
4. 익지 않은 토마토가 있는지 판단
    - 모든 토마토가 익으면 -> 며칠이 걸렸는지 추력
    - 익지 않은 토마토가 1개라도 있으면 -> -1 출력
    

* 후기

x, y 좌표 위치를 헷갈릴 수 있으니 주의!
```
```java
import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[][] map;
    static int[][] days;
    static int[] dx = { 0, 0, -1, 1 };
    static int[] dy = { -1, 1, 0, 0 };
    static Queue<int[]> q = new LinkedList<>();
    static int answer;

    public void bfs() {

        while(!q.isEmpty()) {
            int[] now = q.poll();
            int nowX = now[0];
            int nowY = now[1];

            for(int i = 0; i < 4; i++) {
                int nextX = nowX + dx[i];
                int nextY = nowY + dy[i];

                if(nextX >= 0 && nextX < n && nextY >= 0 && nextY < m) {
                    if(map[nextX][nextY] == 0 && days[nextX][nextY] == -1) {
                        q.add(new int[] { nextX, nextY });
                        days[nextX][nextY] = days[nowX][nowY] + 1;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        
        boolean alreadyFlag = true;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(map[i][j] == 0) {
                    alreadyFlag = false;
                }
            }
        }

        if(alreadyFlag) {
            System.out.println(0);
            return;
        }

        days = new int[n][m];

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(map[i][j] == 1) {
                    q.add(new int[] { i, j });
                    days[i][j] = 0; // days는 거리를 저장하는 것
                } else {
                    days[i][j] = -1; 
                }
            }
        }

        main.bfs();

        boolean nonFlag = false;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if (map[i][j] == 0 && days[i][j] == -1) {
                    nonFlag = true;
                    break;
                }
            }
        }
        
        if(nonFlag) {
            System.out.println(-1);
            return;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                answer = Math.max(answer, days[i][j]);
            }
        }

        System.out.println(answer);
    }
}
```
