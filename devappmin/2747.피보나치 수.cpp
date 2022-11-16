#include <iostream>
long long r[90]={0,1};
int main(){
    int l;
    std::cin>>l;
    for(int i=2;i<=l;i++){
        r[i]=r[i-1]+r[i-2];
    }
    std::cout<<r[l];
    return 0;
}
