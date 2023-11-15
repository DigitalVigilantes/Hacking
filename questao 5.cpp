#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
    int E, M, D;
    cin >> E >> M >> D;

    vector<pair<int, int>> like_pairs;
    vector<pair<int, int>> dislike_pairs;

    for (int i = 0; i < M; ++i) {
        int x, y;
        cin >> x >> y;
        like_pairs.push_back({x, y});
    }

    for (int i = 0; i < D; ++i) {
        int u, v;
        cin >> u >> v;
        dislike_pairs.push_back({u, v});
    }

    vector<vector<int>> groups(E / 3, vector<int>(3));
    for (int i = 0; i < E / 3; ++i) {
        cin >> groups[i][0] >> groups[i][1] >> groups[i][2];
    }

    int violation_count = 0;

    for (const auto& pair : like_pairs) {
        int x = pair.first;
        int y = pair.second;
        bool found = false;

        for (const auto& group : groups) {
            if ((group[0] == x || group[1] == x || group[2] == x) &&
                (group[0] == y || group[1] == y || group[2] == y)) {
                found = true;
                break;
            }
        }

        if (!found) {
            ++violation_count;
        }
    }

    for (const auto& pair : dislike_pairs) {
        int u = pair.first;
        int v = pair.second;

        for (const auto& group : groups) {
            unordered_set<int> group_set(group.begin(), group.end());

            if ((group_set.count(u) && group_set.count(v)) ||
                (group_set.count(u) == 0 && group_set.count(v) == 0)) {
                ++violation_count;
                break;
            }
        }
    }

    cout << violation_count << endl;

    return 0;
}
