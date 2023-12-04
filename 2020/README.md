# [Advent of Code 2020](https://adventofcode.com/2020/)

<table>
    <tr>
        <th colspan="7">December</th>
    </tr>
    <tr>
        <th></th>
        <th><a href="https://adventofcode.com/2020/day/1">01</a></th>
        <th><a href="https://adventofcode.com/2020/day/2">02</a></th>
        <th><a href="https://adventofcode.com/2020/day/3">03</a></th>
        <th><a href="https://adventofcode.com/2020/day/4">04</a></th>
        <th><a href="https://adventofcode.com/2020/day/5">05</a></th>
        <th><a href="https://adventofcode.com/2020/day/6">06</a></th>
    </tr>
    <tr>
        <th><a href="https://adventofcode.com/2020/day/7">07</a>*</th>
        <th>08</th>
        <th>09</th>
        <th>10</th>
        <th>11</th>
        <th>12</th>
        <th>13</th>
    </tr>
    <tr>
        <th>14</th>
        <th>15</th>
        <th>16</th>
        <th>17</th>
        <th>18</th>
        <th>19</th>
        <th>20</th>
    </tr>
    <tr>
        <th>21</th>
        <th>22</th>
        <th>23</th>
        <th>24</th>
        <th>25</th>
        <th></th>
        <th></th>
    </tr>
</table>

*Only part 1 solved.

## Days & Notes

Day | Name | Info | Notes
:--- | :-- | :---  | :----
[Day 01](https://github.com/enigm4tik/advent-of-code/blob/main/2020/day01.py)  | Report Repair | Report == 2020 | None
[Day 02](https://github.com/enigm4tik/advent-of-code/blob/main/2020/day02.py) | Password Philosophy | Valid Passwords | None 
[Day 03](https://github.com/enigm4tik/advent-of-code/blob/main/2020/day03.py) | Toboggan Trajectory | Slide down a Slope | Numpy
[Day 04](https://github.com/enigm4tik/advent-of-code/blob/main/2020/day04.py) | Passport Processing | Valid Passports | Abandoning lists, use Passport class
[Day 05](https://github.com/enigm4tik/advent-of-code/blob/main/2020/day05.py) | Binary Boarding | Board a Plane: BFLR | Calculate binary to decimal and vice versa
[Day 06](https://github.com/enigm4tik/advent-of-code/blob/main/2020/day06.py) | Custom Customs | Common Questions | Very convoluted but tired
[Day 07](https://github.com/enigm4tik/advent-of-code/blob/main/2020/day07.py) | Handy Haversacks | Bags of bags | Finally learned how to Dijkstra


# Day 07 Advent of Code

I have struggled with this part for a long time.
I had to learn a lot about graph traversal, BFS, DFS, Dijkstra and it did pay off in the end.
This is a reminder for me and anyone who reads this that if you put the work in, you can do it. 

# Sometimes a drawing can help
![Bags containing Bags](https://github.com/enigm4tik/advent-of-code/blob/main/2020/bags_containing_bags.png?raw=true)

What this drawing showed me was that I was completely forgetting the **bag** the bags were **in**. A simple + 1 error.

```py
amount = 1 + all_bags.get(bag) * amount_of_bags_per_bag[current_bag_to_check]
```

So, future me and whoever comes across this.
Never give up :D
