# Day 07 Advent of Code

I have struggled with this part for a long time.
I had to learn a lot about graph traversal, BFS, DFS, Dijkstra and it did pay off in the end.
This is a reminder for me and anyone who reads this that if you put the work in, you can do it. 

# Sometimes a drawing can help
![Bags containing Bags](https://github.com/enigm4tik/advent-of-code/blob/main/2020/day07/bags_containing_bags.png?raw=true)

What this drawing showed me was that I was completely forgetting the **bag** the bags were **in**. A simple + 1 error.

```py
amount = 1 + all_bags.get(bag) * amount_of_bags_per_bag[current_bag_to_check]
```

So, future me and whoever comes across this.
Never give up :D
