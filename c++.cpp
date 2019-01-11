#include <vector>
#include <queue>
using namespace std;

C++ CppCoreGuidelines:
github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#S-philosophy

TODO:
Binary search implementation
quicksort implementation
priority_queue and above time complexities

// Comparator lambda:
int some_function(){
    vector<int> unsortedVector;
    auto comp = [&externalRef](const pair<int, int>& a, const pair<int, int>& b){
        return (a.first > b.first || (a.first == b.first && a.second < b.second));
    };
    sort(begin(unsortedVector), end(unsortedVector), comp);
}

//2D vector declaration
vector<vector<int>> vectorNameHere( NUM_ROWS, std::vector<int>(NUM_COLS, FILL_VALUE));

//Swap without extra variable
int m,n;
m = m + n;
n = m - n;
m = m - n;

//Range based for loop
for(const auto& i:someDatastructure){
    //Do something
}

//Iterator version
for(auto it = begin(map); it != end(map); it++){

}

//Max or min of multiple values
max({x,y,z});

Preorder: node, left, right
Inorder: left, node, right
Postorder: left, right, node
Level order: BFS with queue;

//Priority queue, ctrl-f "Comparator lambda" for reference
priority_queue<int> maxPQ;
priority_queue<int, vector<int>, std::greater<int>> minPQ;
priority_queue<int, vector<int>, decltype(compLambda)> customPQ;

//Erase all non-unique characters
std::sort(res.begin(), res.end());
res.erase(unique(res.begin(), res.end()), res.end());


//Lower and upper bound
void lower_upperbound(){
    {10,11,11, 12}, VAL = 11
    lower_bound(begin(vec), end(vec), VAL); // First element NOT less than VAL(greater or equal that VAL), index 1
    upper_bound(begin(vec), end(vec), VAL); // First element greater than VAL, index 3
}

Leetcode hash function:
struct customHash {
    int operator()(const vector<char> &vec) const {
        std::size_t seed = vec.size();
        for(auto& i : vec) {
            seed ^= i + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        }
        return seed;
    }
};

Generic Hash function, cannnot use on leetcode
#include <boost/functional/hash.hpp>
template <typename Container> // we can make this generic for any container [1]
struct container_hash {
    std::size_t operator()(Container const& c) const {
        return boost::hash_range(c.begin(), c.end());
    }
};

