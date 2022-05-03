# n2w-turkish
This is the Number-to-Word function for Turkish

### How to Use
It's very easy. Let's type a number in the string format as the input. If you want to use some punctuations such as comma, point to divide the number to units easily, it doesn't matter. Here's an example:

```python
n2w("84680273")
n2w("84.680.273")
```

### Limits
The maximum limit of the function is **katrilyon** (it means *quadrillion*), but it's possible to extend it if you need more. You can add names of the bigger units such as **kentilyon**, **sekstilyon**, **septilyon** into the `unitnames` variable on the line 41. See at [here](https://tr.wikipedia.org/wiki/B%C3%BCy%C3%BCk_say%C4%B1lar%C4%B1n_adlar%C4%B1).

```python
unitnames = ["", "bin ", "milyon ", "milyar ", "trilyon ", "katrilyon "]
```

### To-do
- Some improvements for the current function
- The w2n function

### Contact
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/mehmetumutmutlu.svg?style=social&label=Follow%20@mehmetumutmutlu)](https://twitter.com/mehmetumutmutlu)
