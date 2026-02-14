#include <bits/stdc++.h>
using namespace std;

template <typename T, class Op>
class SparseTable {
 private:
  int n;
  int maxlg;
  vector<vector<T>> st;
  vector<int> log;
  Op op;

 public:
  SparseTable(const vector<T>& arr) {
    n = arr.size();
    maxlg = 32 - __builtin_clz(n);
    st.assign(maxlg, vector<T>(n));
    log.assign(n + 1, 0);
    for (int i = 2; i <= n; i++) {
      log[i] = log[i / 2] + 1;
    }
    for (int i = 0; i < n; i++) {
      st[0][i] = arr[i];
    }
    for (int k = 1; k < maxlg; k++) {
      for (int i = 0; i + (1 << k) <= n; i++) {
        st[k][i] = op(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
      }
    }
  }
  T query(int l, int r) {
    T res{};
    bool init = false;
    for (int k = maxlg - 1; k >= 0; k--) {
      if ((1 << k) <= r - l + 1) {
        if (!init) {
          res = st[k][l];
          init = true;
        } else {
          res = op(res, st[k][l]);
        }
        l += 1 << k;
      }
    }
    return res;
  }
};

struct CustomOp {
  long long operator()(long long a, long long b) const {
    // Fill in anything you want
    return a + b;
  }
};