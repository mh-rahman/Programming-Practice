// constructing maps
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <climits>

using namespace std;

//vector<int> movieDuration(int flightDuration, vector<int> movieDuration)
//{
//    int total = flightDuration - 30;
//    int idx1 = INT_MIN, idx2 = INT_MIN;
//    map<int, int> m;
//    for (int i=0; i<movieDuration.size(); i++) {
//    	if (movieDuration[i] < 0) {
//    		continue;
//		}
//        if (m.find(total - movieDuration[i]) != m.end()) {
//            int id1 = i;
//            int id2 = m[total - movieDuration[i]];
//            int max_so_far = max(movieDuration[id1], movieDuration[id2]);
//            if (idx1 == INT_MIN || 
//                max(movieDuration[id1], movieDuration[id2]) > 
//                max(movieDuration[idx1], movieDuration[idx2])) {
//                idx1 = min(id1, id2);
//                idx2 = max(id1, id2);
//            }
//        } else {
//            m.insert(pair<int, int>(movieDuration[i], i));
//        }
//    }
//    vector<int> result;
//    result.push_back(idx1);
//    result.push_back(idx2);
//    return result;
//}
//
//
//int main() {
//	vector<int> input;
//	input.push_back(100);
//	input.push_back(180);
//	input.push_back(40);
//	input.push_back(120);
//	input.push_back(10);
//	int duration = 250;
//	vector<int> result = movieDuration(duration, input);
//	cout<<result[0]<<" "<<result[1]<<endl;
//}

int main(){
	
	int duration=90-30,l_index,longest=0;
	int n=5;//number of movies
	int movies[] = {1, 5, 7, -1, 6};
	duration=10;
	
	map<int,int> movie;
	
	for(int i=0;i<5;i++){
		int diff=duration-movies[i];
		map<int,int>::iterator it = movie.find(diff);
		if (it!=movie.end()){
			if(longest<max(movies[i],diff)){
				if(movies[i]>diff){
					longest=movies[i];
					l_index=i;
				}
				else{
					longest=diff;
					l_index=movie[diff];
				}
				
			}
		}
		movie.insert(pair<int,int> (movies[i],i));
	}
	int p[] = {0,0};
	p[0]=l_index;
	p[1]=movie[duration-longest];
	sort (p,p+2);
	cout<<"Sum = "<<duration<<", Indexes = ["<<p[0]<<","<<p[1]<<"], Values = ["<<movies[p[0]]<<","<<movies[p[1]]<<"]"<<endl;
	
	
	return 0;
	
	
	
}
