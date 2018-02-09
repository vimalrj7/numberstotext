#-------------------------------------------------------------------------------
# Name:        Number To Text Converter
# Version:     1.0
# Author:      vimalrj
# Created:     18/1/2018
#-------------------------------------------------------------------------------

from guizero import App, Text, TextBox, PushButton, Box

ones = [
"zero",
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten",
"eleven",
"twelve",
"thirteen",
"fourteen",
"fifteen",
"sixteen",
"seventeen",
"eighteen",
"nineteen"
]

tens = [
"",
"ten",
"twenty",
"thirty",
"forty",
"fifty",
"sixty",
"seventy",
"eighty",
"ninety"
]

thousands = [
"",
"thousand",
"million",
"billion",
"trillion",
"quadrillion",
"quintillion",
"sextillion",
"septillion",
"octillion",
"nonillion",
"decillion",
"undecillion",
"duodecillion",
"tredecillion",
"quattuordecillion",
"sexdecillion",
"septendecillion",
"octodecillion",
"novemdecillion",
"vigintillion"
]

# Converts 2 digit numbers
# Divides the number by 10, gets remainder from 'ones' list
# Then gets quotient from 'tens' list
def two_nums(n):
    val = []
    if n < 20:
        val.append(ones[n])
        return val
    q, r = divmod(n, 10)
    if r:
        val.extend((tens[q], ones[r]))
    else:
        val.append(tens[q])
    return val

# Converts 3 digit numbers
# Divides the number by 100, runs the 'two_nums' function on remainder
# Then gets quotient from 'ones' list and adds hundred  
def three_nums(n):
    val = []
    q, r = divmod(n, 100)
    if r:
        val += two_nums(r)
    if q:
        val[:0] = [ones[q], 'hundred']
    return val

# Converts 4 digits and more numbers
# A loop divides the number by a thousand, runs the three_nums function on the remainder
# Gets thousands value from thousands list, then increases the index by one
# Loop runs again, adding to the value until the number becomes zero
def four_nums(n):
    val = []
    i = 0
    while n:
        n, r = divmod(n, 1000)
        if i < len(thousands):
            if r:
                val[:0] = three_nums(r)+[thousands[i],]
        else:
            return 'The number is too big!'
        i += 1
    return val
      
# Decides positive and negative signs
# Returns the number as an integer in a list
def print_int(n):
    try:
        n = int(n)
    except:
        return "That's not a number!"
    if n < 0:
        n = -n
        sign = True
    else:
        sign = False

    if n < 1000:
        if n == 0:
            return 'zero'
        val = three_nums(n)
    else:
        val = four_nums(n)
        
    if sign:
        val[:0] = ['negative',]
     
    return val

# Gets rid of any commas to avoid error
# If decimal point present, adds decimal values
# Prints out final number as a string
def print_num(n):
    n = n.replace(',', '')
    if '.' in n:
        n = str(n).split('.')
        val = print_int(n[0]) + ['point',]
        for i in n[1]:
            val.append(ones[int(i)])
    else:
        val = print_int(n)
    ans = ' '.join(val)
    return ans[0].upper() + ans[1:]
    
    

# GUI logic

# Updates the answer value when button is pressed
def push_button():
    answer.clear()
    input = input_box.get()
    ans = print_num(input)
    answer.value = ans
        
app = App(title="Number To Text Converter", width="500", height="400")
intro = Text(app, text="Type in a number!", size=18)
input_box = TextBox(app, width=50)
button = PushButton(app, command=push_button, text='Convert')
answer = Text(app, text="...", size=14)
answer.tk.config(wraplength=500)
app.display()

    
        
