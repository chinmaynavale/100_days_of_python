# Table of contents:

- [01 Leap Year](#Leap-Year)
- [02 Pizza Order](#Pizza-Order)

</br>
</br>

# Leap Year

## Instructions

_Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February._

The reason why we have leap years is really fascinating, this video does it more justice:
[What is a Leap Year](https://www.youtube.com/watch?v=xX96xng7sAE)

This is how you work out whether if a particular year is a leap year.

> On every year that is evenly divisible by 4  
> **except** every year that is evenly divisible by 100  
> **unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)  
2000 ÷ 100 = 20 (Not Leap)  
2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.  
But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)  
2100 ÷ 100 = 21 (Not Leap)  
2100 ÷ 400 = 5.25 (Not Leap)
</br>
</br>

**Example Input 1**

```
2400
```

**Example Output 1**

```
Leap year.
```

**Example Input 2**

```
1989
```

**Example Output 2**

```
Not leap year.
```

---

</br>
</br>
</br>

# Pizza Order

## Instructions

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

```
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
```

```
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
```

```
Extra cheese for any size pizza: +$1
```

**Example Input**

```
size = "L"
```

```
add_pepperoni = "Y"
```

```
extra_cheese = "N"
```

**Example Output**

```
Pizza Size L: $25
Pepperoni: $3

Your final bill is: $28
```

---

[Go Back to Table of contents](#Table-of-contents)
