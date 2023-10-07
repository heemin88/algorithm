#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<string> park, vector<string> routes) {
    //공원을 나타냄, 수행할 명령어들 
    vector<int> answer;
    int loc_x,loc_y;
    int h = park.size();
    int w = park[0].length();
    for(int i = 0 ; i < h ;i++){
        if (park[i].find('S')!= string::npos){
            loc_x = i;
            loc_y = park[i].find('S');
            break;
        }
    }
    for (int i = 0; i< routes.size();i++){
        int cnt = routes[i][2]-'0';
        switch(routes[i][0]){
            case 'E':
                
                if (loc_y+cnt < w){
                    bool success = true;
                    for (int j = loc_y ; j < loc_y+cnt+1; j++){
                        if(park[loc_x][j] == 'X'){
                            success= false;
                            break;
                        }
                    }
                    if(success){
                        loc_y+= cnt;
                    }
                }
                break;
            case 'S':
                if (loc_x+cnt < h){
                    bool success = true;
                    for (int j = loc_x ; j < loc_x+cnt+1; j++){
                        if(park[j][loc_y] == 'X'){
                            success= false;
                            break;
                        }
                    }
                    if(success){
                        loc_x+= cnt;
                    }
                }
                break;
            case 'W':
                if (loc_y-cnt >= 0){
                    bool success = true;
                    for (int j = loc_y ; j > loc_y-cnt-1; j--){
                        if(park[loc_x][j] == 'X'){
                            success= false;
                            break;
                        }
                    }
                    if(success){
                        loc_y-= cnt;
                    }
                }
                break;
            case 'N':
                if (loc_x-cnt >=0){
                    bool success = true;
                    for (int j = loc_x ; j > loc_x-cnt-1; j--){
                        if(park[j][loc_y] == 'X'){
                            success= false;
                            break;
                        }
                    }
                    if(success){
                        loc_x-= cnt;
                    }
                }
                break;
        }
    }
    answer.push_back(loc_x);
    answer.push_back(loc_y);
    return answer;
}