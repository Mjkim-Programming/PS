#include <bits/stdc++.h>
#define FASTIO                 \
  ios::sync_with_stdio(false); \
  cin.tie(nullptr)
#define END return 0
#define iter(i, n) for (int i = 0; i < n; i++)
using namespace std;
struct Query {
  int l, r, idx, block;
  bool operator<(const Query& other) const {
    if (block != other.block) return block < other.block;
    if (block & 1) return r > other.r;
    return r < other.r;
  }
};
int main() {
  FASTIO;
  int N;
  cin >> N;
  vector<int> A(N);
  iter(i, N) cin >> A[i];
  int M;
  cin >> M;
  int blsize = sqrt(N);
  vector<Query> queries(M);
  iter(i, M) {
    int l, r;
    cin >> l >> r;
    l--;
    r--;
    queries[i] = {l, r, i, l / blsize};
  }
  sort(queries.begin(), queries.end());
  vector<int> freq(1000001, 0);
  vector<int> ans(M);
  int curL = 0, curR = -1, cur = 0;
  auto add = [&](int x) {
    if (freq[x] == 0) cur++;
    freq[x]++;
  };
  auto remove = [&](int x) {
    freq[x]--;
    if (freq[x] == 0) cur--;
  };
  for (const Query& q : queries) {
    while (curL > q.l) add(A[--curL]);
    while (curR < q.r) add(A[++curR]);
    while (curL < q.l) remove(A[curL++]);
    while (curR > q.r) remove(A[curR--]);
    ans[q.idx] = cur;
  }
  iter(i, M) cout << ans[i] << '\n';
  END;
}