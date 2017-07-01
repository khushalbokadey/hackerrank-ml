#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    double timeCharged;
    float output;
char line[64];
while(fgets(line, 64, stdin)) {
    float input = atof(line);
    output=input*2.0;
    if(output>8.0)
        output=8.0;
    printf("%.2f\n", output);
}    
return 0;
}
