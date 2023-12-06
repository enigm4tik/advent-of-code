/** Advent of Code - 2023
** Day 6
** Implementation of a binary search in C++ as practice.
** Improved my runtime over the python implementation by A LOT.
** I learned a lesson or two about big numbers...
** I could probably improve it a bit but it's late and I've proved my point :) 
**/

#include <iostream>
using namespace std;

unsigned long long int calculateDistance(int time, int speed){
    unsigned long long int value = time - speed;
    unsigned long long int travel_distance = speed * value;
    return travel_distance;
}

int findLeftMostCandidate(int &time, long long int &distance){
    int left = 0;
    int right = time/2;
    int current = (left + right)/2;
    unsigned long long int calculatedDistance = calculateDistance(time, current);
    unsigned long long int neighbor = calculateDistance(time, current - 1);
    while (!(calculatedDistance > distance && neighbor <= distance)){
        if (calculatedDistance < distance){
            left = current;
        } else if (calculatedDistance >= distance) {
            right = current;
        }
        current = (left+right)/2;
        calculatedDistance = calculateDistance(time, current);
        neighbor = calculateDistance(time, current - 1);
    }
    return current;
}


int findRightMostCandidate(int &time, long long int &distance){
    int left = time/2;
    int right = time;
    int current = (left + right)/2;
    unsigned long long int calculatedDistance = calculateDistance(time, current);
    unsigned long long int neighbor = calculateDistance(time, current + 1);
    while (!(calculatedDistance > distance && neighbor <= distance)){
        if (calculatedDistance <= distance){
            right = current;
        } else if (calculatedDistance > distance) {
            left = current;
        }
        current = (left+right)/2;
        calculatedDistance = calculateDistance(time, current);
        neighbor = calculateDistance(time, current+1);
    }    
    return current;
}

int part1() {
    const int length = 4;
    int time[length] = {35, 93, 73, 66};
    long long int distance[length] = {212, 2060, 1201, 1044};

    int resultContainer[length];
    for (int i = 0; i < length; i++) {
        int result = 1;
        result -= findLeftMostCandidate(time[i], distance[i]);
        result += findRightMostCandidate(time[i], distance[i]);
        resultContainer[i] = result;
    }

    int product = 1;
    for (int amount : resultContainer) {
        product *= amount;
    }
    return product;
}

long long int part2(){
    const int length = 1;
    int time =  35937366;
    long long int distance = 212206012011044;
    long long int result = 1;
    result -= findLeftMostCandidate(time, distance);
    result += findRightMostCandidate(time, distance);

    return result;
}

int main() {
    cout << "Part 1: " << part1() << endl;
    cout << "Part 2: " << part2() << endl;
}

