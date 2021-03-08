#include <iostream>

using namespace std;


int*[] get_factors(int num) {
    int*  factors = new int[10000000];
    return factors;

}

int main(){
    int*  factors = new int[10000000];

    std::cout << "test" << std::endl;
    factors = get_factors(19);

    std::cout << "--" << get_factors << std::endl;
    return 1;
}