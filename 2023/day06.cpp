/** Advent of Code - 2023
** Day 6
** Implementation of a binary search in C++ as practice.
** Improved my time over the python implementation by A LOT.
** I learned a lesson or two about big numbers...
** I could probably improve it a bit but it's late and I've proved my point :) 
**/

#include <iostream>
using namespace std;
using bigInt = unsigned long long int;

bigInt calculateDistance(bigInt time, bigInt speed){
    bigInt travel_distance = speed * (time - speed);
    return travel_distance;
}

int findLeftMostCandidate(int &time, bigInt &distance){
    int left = 0;
    int right = time/2;
    int current = (left + right)/2;
    bigInt calculatedDistance = calculateDistance(time, current);
    bigInt neighbor = calculateDistance(time, current - 1);
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


int findRightMostCandidate(int &time, bigInt &distance){
    int left = time/2;
    int right = time;
    int current = (left + right)/2;
    bigInt calculatedDistance = calculateDistance(time, current);
    bigInt neighbor = calculateDistance(time, current + 1);
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
    bigInt distance[length] = {212, 2060, 1201, 1044};

    int part1[length];
    for (int i = 0; i < length; i++) {
        int result = 1;
        result -= findLeftMostCandidate(time[i], distance[i]);
        result += findRightMostCandidate(time[i], distance[i]);
        part1[i] = result;
    }

    int product = 1;
    for (int amount : part1) {
        product *= amount;
    }
    return product;
}

bigInt part2(){
    const int length = 1;
    int time =  35937366;
    bigInt distance = 212206012011044;
    bigInt result = 1;
    result -= findLeftMostCandidate(time, distance);
    result += findRightMostCandidate(time, distance);

    return result;
}

int main() {
    cout << "Part 1: " << part1() << endl;
    cout << "Part 2: " << part2() << endl;
}
