#include <bits/stdc++.h>
#define ll long long
#define FASTIO   \
  cin.tie(NULL); \
  ios::sync_with_stdio(false)
#define END return 0
using namespace std;

struct Point {
  ll x, y;
  Point() {}
  Point(ll _x, ll _y) : x(_x), y(_y) {}
};
Point operator+(const Point& a, const Point& b) {
  return Point(a.x + b.x, a.y + b.y);
}
Point operator-(const Point& a, const Point& b) {
  return Point(a.x - b.x, a.y - b.y);
}
Point operator*(const Point& a, ll k) { return Point(a.x * k, a.y * k); }

ll dot(const Point& a, const Point& b) { return a.x * b.x + a.y * b.y; }
ll cross(const Point& a, const Point& b) { return a.x * b.y - a.y * b.x; }
ll orient(const Point& a, const Point& b, const Point& c) {
  return cross(b - a, c - a);
}
int ccw(const Point& a, const Point& b, const Point& c) {
  ll v = orient(a, b, c);
  if (v > 0) return 1;
  if (v < 0) return -1;
  return 0;
}
bool is_left_turn(const Point& a, const Point& b, const Point& c) {
  return orient(a, b, c) > 0;
}
int main() {
  FASTIO;
  int P;
  cin >> P;
  while (P--) {
    int N;
    cin >> N;
    vector<Point> p(N);
    for (int i = 0; i < N; i++) cin >> p[i].x >> p[i].y;
    sort(p.begin(), p.end(), [](const Point& a, const Point& b) {
      if (a.x != b.x) return a.x < b.x;
      return a.y < b.y;
    });
    vector<Point> hull;
    for (int i = 0; i < N; i++) {
      while (hull.size() >= 2 &&
             orient(hull[hull.size() - 2], hull.back(), p[i]) <= 0) {
        hull.pop_back();
      }
      hull.push_back(p[i]);
    }
    int l_size = hull.size();
    for (int i = N - 2; i >= 0; i--) {
      while ((int)hull.size() > l_size &&
             orient(hull[hull.size() - 2], hull.back(), p[i]) <= 0) {
        hull.pop_back();
      }
      hull.push_back(p[i]);
    }
    hull.pop_back();
    reverse(hull.begin(), hull.end());

    int idx = 0;
    for (int i = 1; i < hull.size(); i++) {
      if (hull[i].y > hull[idx].y ||
          (hull[i].y == hull[idx].y && hull[i].x < hull[idx].x)) {
        idx = i;
      }
    }

    vector<Point> ans;
    for (int i = 0; i < hull.size(); i++) {
      ans.push_back(hull[(idx + i) % hull.size()]);
    }

    cout << ans.size() << "\n";
    for (Point& pt : ans) {
      cout << pt.x << " " << pt.y << "\n";
    }
  }
  END;
}