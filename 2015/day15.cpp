/*
 * Advent of Code - 2015
 * Day 15
*/

#include <iostream>
#include <vector>
using namespace std;

struct Ingredient
{
	Ingredient(int c, int d, int f, int t, int cal)
	{
		this->capacity = c; 
		this->durability = d;
		this->flavor = f;
		this->texture = t;
		this->calories = cal;
	}
	int capacity = 0;
	int durability = 0;
	int flavor = 0;
	int texture = 0;
	int calories = 0;
};

void calculateCookies(vector<Ingredient>& recipe, bool calories)
{
	Ingredient cookie(0, 0, 0, 0, 0);
	int bestScore = 0;
	for (int i = 0; i < 100; i++)
	{
		for (int j = 0; j < 100 - i; j++)
		{
			for (int k = 0; k < 100 - i - j; k++)
			{

				int l = 100 - i - j - k; 
				cookie.capacity = recipe[0].capacity * i + recipe[1].capacity * j + recipe[2].capacity * k + recipe[3].capacity * l;
				cookie.durability = recipe[0].durability * i + recipe[1].durability * j + recipe[2].durability * k + recipe[3].durability * l;
				cookie.flavor = recipe[0].flavor * i + recipe[1].flavor * j + recipe[2].flavor * k + recipe[3].flavor * l;
				cookie.texture = recipe[0].texture * i + recipe[1].texture * j + recipe[2].texture * k + recipe[3].texture * l;
				cookie.calories = recipe[0].calories * i + recipe[1].calories * j + recipe[2].calories * k + recipe[3].calories * l;
				if (calories)
				{
					if (cookie.calories != 500)
						continue;
				}
				if (cookie.capacity < 0)
					cookie.capacity = 0;
				if (cookie.durability < 0)
					cookie.durability = 0;
				if (cookie.flavor < 0)
					cookie.flavor = 0;
				if (cookie.texture < 0)
					cookie.texture = 0;
				int score = cookie.capacity * cookie.durability * cookie.flavor * cookie.texture;
				
				if (score > bestScore)
					bestScore = score;
			}
		}
	}
	cout << bestScore;
}

int main()
{
	// Hard coded input: For such a simple input parsing is overkill.
	
	Ingredient frosting = Ingredient(4, -2, 0, 0, 5);
	Ingredient candy = Ingredient(0, 5, -1, 0, 8);
	Ingredient butterscotch = Ingredient(-1, 0, 5, 0, 6);
	Ingredient sugar = Ingredient(0, 0, -2, 2, 1);

	vector<Ingredient> recipe = { frosting, candy, butterscotch, sugar };
	
	cout << "Part 1: ";
	calculateCookies(recipe, false);
	cout << endl;
	cout << "Part 2: ";
	calculateCookies(recipe, true);
	cout << endl;

	return 0;
}	