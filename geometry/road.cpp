#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")
#include <bits/stdc++.h>
#define FASTIO   \
  cin.tie(NULL); \
  ios::sync_with_stdio(false)
#define END return 0
using ll = long long;
using namespace std;

struct Point {
  long long x, y;
};

enum Orientation { CW = -1, COLLINEAR = 0, CCW = 1 };

ll ccw(const Point& a, const Point& b, const Point& c) {
  return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

Orientation orientation(const Point& a, const Point& b, const Point& c) {
  long long v = ccw(a, b, c);
  if (v > 0) return CCW;
  if (v < 0) return CW;
  return COLLINEAR;
}

vector<Point> convex_hull(vector<Point>& pts) {
  sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
    if (a.x == b.x) return a.y < b.y;
    return a.x < b.x;
  });

  vector<Point> hull;
  for (auto& p : pts) {
    while (hull.size() >= 2 &&
           orientation(hull[hull.size() - 2], hull.back(), p) != CCW)
      hull.pop_back();
    hull.push_back(p);
  }

  int t = hull.size() + 1;
  for (int i = pts.size() - 2; i >= 0; i--) {
    Point p = pts[i];
    while (hull.size() >= t &&
           orientation(hull[hull.size() - 2], hull.back(), p) != CCW)
      hull.pop_back();
    hull.push_back(p);
  }

  hull.pop_back();
  return hull;
}
ll dist2(Point& a, Point& b) {
  ll dx = a.x - b.x;
  ll dy = a.y - b.y;
  return dx * dx + dy * dy;
}

ll calipers(vector<Point>& hull) {
  int n = hull.size();
  if (n < 2) return 0;
  if (n == 2) return dist2(hull[0], hull[1]);
  ll max_d2 = 0;
  int j = 1;
  for (int i = 0; i < n; i++) {
    int ni = (i + 1) % n;
    while (true) {
      int nj = (j + 1) % n;
      if (ccw(hull[i], hull[ni], hull[nj]) > ccw(hull[i], hull[ni], hull[j])) {
        j = nj;
      } else {
        break;
      }
    }
    max_d2 = max({max_d2, dist2(hull[i], hull[j]), dist2(hull[ni], hull[j])});
  }
  return max_d2;
}

pair<Point, Point> calipers_pair(vector<Point>& hull) {
  int n = hull.size();
  if (n == 2) return {hull[0], hull[1]};
  ll max_d2 = 0;
  pair<Point, Point> farthest;
  int j = 1;
  for (int i = 0; i < n; i++) {
    int ni = (i + 1) % n;
    while (true) {
      int nj = (j + 1) % n;
      if (ccw(hull[i], hull[ni], hull[nj]) > ccw(hull[i], hull[ni], hull[j])) {
        j = nj;
      } else {
        break;
      }
    }
    ll d2_i = dist2(hull[i], hull[j]);
    if (d2_i > max_d2) {
      max_d2 = d2_i;
      farthest = {hull[i], hull[j]};
    }
    ll d2_ni = dist2(hull[ni], hull[j]);
    if (d2_ni > max_d2) {
      max_d2 = d2_ni;
      farthest = {hull[ni], hull[j]};
    }
  }
  return farthest;
}

int main() {
  FASTIO;
  int n;
  cin >> n;
  vector<Point> pts(n);
  for (int i = 0; i < n; i++) cin >> pts[i].x >> pts[i].y;
  vector<Point> hull = convex_hull(pts);
  pair<Point, Point> far = calipers_pair(hull);
  cout << far.first.x << " " << far.first.y << " " << far.second.x << " "
       << far.second.y;
  END;
}