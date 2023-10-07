#include <string>
#include <vector>
#include <map>
#include <iostream>
using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) { //그리워하는 사람의 이름, 그리움 점수, 사진에 찍힌 인물의 이름 
    vector<int> answer;
    map<string,int> score;
    for(int i=0;i < name.size() ; i++){
        score[name[i]] = yearning[i];
    }
    for(int i = 0 ; i< photo.size();i++){
        int s = 0;
        for (int j =0 ; j< photo[i].size();j++){
            s += score[photo[i][j]];
        }
        answer.push_back(s);
    }
    return answer;
}