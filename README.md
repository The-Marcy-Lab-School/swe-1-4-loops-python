# Loops

Practice repeating work with `for` and `while`, and with `range()`.

**Practicing:** for loops, while loops, `range()`, `break`, `continue`, looping over a string

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Setup](#setup)
- [Before You Start](#before-you-start)
- [From Scratch](#from-scratch)
  - [Question 1: `loop_0_up_to_10`](#question-1-loop_0_up_to_10)
  - [Question 2: `loop_5_to_10`](#question-2-loop_5_to_10)
  - [Question 3: `loop_even_numbers_up_to_10`](#question-3-loop_even_numbers_up_to_10)
  - [Question 4: `countdown_5_to_0`](#question-4-countdown_5_to_0)
  - [Question 5: `loop_up_to_num`](#question-5-loop_up_to_num)
  - [Question 6: `fizzbuzz`](#question-6-fizzbuzz)
  - [Question 7: `count_vowels`](#question-7-count_vowels)
  - [Question 8: `halving_steps`](#question-8-halving_steps)
  - [Question 9: `ask_for_pin`](#question-9-ask_for_pin)
- [Modify](#modify)
  - [Question 10: `while_to_for`](#question-10-while_to_for)
- [Debug](#debug)
  - [Question 11: `broken_loop`](#question-11-broken_loop)
  - [Question 12: `broken_digit_count`](#question-12-broken_digit_count)
  - [Question 13: `broken_letter_count`](#question-13-broken_letter_count)
  - [Question 14: `broken_score_total`](#question-14-broken_score_total)
- [Submitting](#submitting)
- [Good luck!](#good-luck)

## AI Use on This Assignment

Use whichever mode matches where you are with this material. Both are fine,
and most people move between them as a concept clicks.

**Tutor mode.** The AI explains, questions, quizzes, and critiques, and you
write every line you submit. For this assignment that means asking it what the
three numbers in `range()` do, or having it quiz you until you can predict
what your own loop will print. Ask it a hundred questions — that is the whole
point. What you do not do is ask it for the function. Paste this at the start
of a chat and it will hold for the rest of the conversation:

> You are acting as a tutor. Your job is to explain what this coding question
> is asking, clarify confusing wording, and highlight the relevant concepts I
> need to know — but do not provide the full solution or code that directly
> answers the question. Instead, rephrase the problem in simpler terms,
> identify what is being tested, and suggest what steps or thought processes
> might help. Ask me guiding questions to make sure I am thinking critically.
> Do not write the final function, algorithm, or code implementation.

**Implementer mode.** You write a specification first, the AI writes code from
it, and then you verify that code line by line. For this assignment your spec
must say, for every loop, where it starts, where it stops, and whether the
last value is included. If what comes back does more than you asked for,
reject it — over-delivery is a defect, and catching it is part of the job.

You own every line either way, and you will be asked to explain it.

## Setup

Clone your repository in `development/mod-1` and then `cd` into it. Set up
your virtual environment and make a draft branch before you start.

```sh
git clone [your_repo]
cd [your_repo]
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git checkout -b draft
```

Run `pytest` to test the entire assignment, or `pytest -k fizzbuzz` for one
question. Every push runs the tests on GitHub and reports your score in the
**Actions** tab.

75% of tests passing counts as complete. Submit at that point even if it is
not perfect. Treat submitting as a checkpoint rather than a finish line, and
come back to improve it.

When you are done working on this assignment, turn off your virtual
environment by running:

```sh
deactivate
```

## Before You Start

This assignment has three sections:

1. From Scratch
2. Modify
3. Debug

You will see a _lot_ of similar loops in these problems. You may want to copy
and paste, and _ordinarily_ that is fine. Not here. We want you to build some
muscle memory with `for` loops, so please write each "from scratch" question
out by hand. Loops turn up in a huge number of algorithm challenges, and we
want you to get so good at writing them it is literally boring.

Also, READ THE TESTS CAREFULLY, the limits are exact. If a description
confuses you, do what the _test_ says. Remember that **inclusive** means
"include the number" and **exclusive** means "do NOT include the number". So
inclusive 1 to exclusive 5 is 1, 2, 3, 4. Exclusive 5 to inclusive 10 is 6, 7,
8, 9, 10.

Most of these questions **print** rather than return. The tests read what you
printed, so a returned value will not count.

## From Scratch

Write your solutions in `src/from_scratch.py`.

### Question 1: `loop_0_up_to_10`

Write a `for` loop that starts on 0 and prints each number up to, but not
including, 10. Count up by 1.

### Question 2: `loop_5_to_10`

Write a `for` loop that starts on 5 and prints each number up to, and
including, 10. Count up by 1.

Remember `range()` stops before its second number. So what do you pass to
finish on 10?

### Question 3: `loop_even_numbers_up_to_10`

Write a `for` loop that starts on 0 and prints each _even_ number up to, but
not including, 10. What should you count by?

- 0 counts as an even number here
- an `if` check with `continue` would _technically_ work, but it is overkill.
  Is there a simpler way? The tests confirm you did not use either

### Question 4: `countdown_5_to_0`

Write a `for` loop that starts on 5 and prints each number down to, and
including, 0. Count down by 1.

Counting down means all three numbers in `range()` change. Which one makes it
go backwards?

### Question 5: `loop_up_to_num`

Write a `for` loop that starts on 0 and prints each number up to, but not
including, a given `num` argument. Count up by 1.

```python
loop_up_to_num(3)   # prints 0, 1, 2
loop_up_to_num(0)   # prints nothing
```

Check the test for how this should behave when given 0 or a negative number.

### Question 6: `fizzbuzz`

Write a `for` loop that prints every number from 1 to 100, with three
exceptions:

- multiples of 3 print `"fizz"`
- multiples of 5 print `"buzz"`
- multiples of **both** print `"fizzbuzz"`

```text
1
2
fizz
4
buzz
fizz
...
```

Hint: be careful about the order that you check these in! This question comes
up in real interviews more than it has any right to, so it's worth getting
comfortable with. Don't overthink it!

### Question 7: `count_vowels`

Write a function `count_vowels` that takes a string `word` and a boolean
`include_y` that defaults to `False`. It should return how many vowels the
word contains, in either case.

```python
count_vowels("hello")
# 2
count_vowels("rhythm")
# 0
count_vowels("rhythm", True)
# 1
count_vowels("AEIOU")
# 5
```

A `for` loop works on any **iterable**, which is anything Python can hand you
one item at a time. A string is one, so this is the first question here that
loops over something other than a `range()`.

Recall: `include_y` needs a default value, because the tests call this with
only a word.

### Question 8: `halving_steps`

Write a function `halving_steps` that takes a number and returns how many
times you can halve it before it drops below 1.

```python
halving_steps(8)
# 4
halving_steps(1)
# 1
halving_steps(0.5)
# 0
```

Work through `8` by hand: 8 becomes 4, then 2, then 1, then 0.5. That is four
halvings, and the fourth is the one that took it under 1.

You cannot write this with `range()`, because you do not know how many
halvings it will take until you start. Which kind of loop keeps going while
something is still true? The tests check you used one.

A `while` loop is also the only one here that can become an **infinite loop**,
which is a loop whose condition never turns false. If your terminal sits there
doing nothing, press `Ctrl + C` to stop it, then check that something inside
the loop actually changes the value the condition tests.

### Question 9: `ask_for_pin`

Write a function `ask_for_pin` that asks the user for a 4-digit PIN with `input()` and keeps asking until the answer is exactly four digits. Clean each answer with `strip()` before you check it. After each answer that is not four digits, print a message that names the answer, then ask again. Once the answer is valid, return it. Here is what it should look like when you call `ask_for_pin()`

```text
Enter a 4-digit PIN: 12
Sorry, 12 is not a 4-digit PIN
Enter a 4-digit PIN: abcd
Sorry, abcd is not a 4-digit PIN
Enter a 4-digit PIN: 0420
```

Note: Here `ask_for_pin()` returns `"0420"`. Return the PIN as a string, because `int("0420")` is `420`, and a PIN that loses its leading zero is a different PIN.

Note: The tests type the answers for you, one answer for each call to `input()`. If a test fails with `StopIteration`, your function asked for more answers than the test typed, which usually means that the loop did not stop on a valid PIN.

## Modify

Change the function already in `src/modify.py`.

### Question 10: `while_to_for`

Rewrite `while_to_for` as a `for` loop with `range()`. It currently prints 0
to 4 using a `while` loop and a counter it has to increment by hand. The
output stays exactly the same, and the tests check the `while` is gone.

## Debug

### Question 11: `broken_loop`

`broken_loop(start, end)` should build a string of every number from `start`
to `end`, **including** `end`. It currently skips every other number and stops
one short.

```python
broken_loop(1, 10)   # want "12345678910"
broken_loop(0, 0)    # want "0"
broken_loop(0, -1)   # want ""
```

Both problems are in the `range()` call. Note the last two cases: a range that
covers one number, and a range that covers none.

### Question 12: `broken_digit_count`

`broken_digit_count(text)` should return how many characters in `text` are
digits. It currently crashes with an `AttributeError` instead.

```python
broken_digit_count("R2-D2")        # want 2
broken_digit_count("2026-10-13")   # want 8
broken_digit_count("no digits")    # want 0
```

The loop variable is named `character`, but a name does not decide what a
variable holds. Print `character` inside the loop. What does it actually hold,
and where do those values come from?

### Question 13: `broken_letter_count`

`broken_letter_count(text, letter)` should return how many times `letter` appears in `text`. It currently returns 0 or 1 whatever the text is, and it crashes with an `UnboundLocalError` when `text` is empty.

```python
broken_letter_count("banana", "a")   # want 3, gets 1
broken_letter_count("banana", "n")   # want 2, gets 0
broken_letter_count("", "a")         # want 0, crashes
```

Print `count` at the end of every pass through the loop for `broken_letter_count("banana", "a")`. When does it go back to 0? Then think about the empty string: how many times does the loop body run, and which lines inside it never run?

### Question 14: `broken_score_total`

`broken_score_total()` should ask for quiz scores until the user types `done`, then return the total of the scores. When the user types something that is not a whole number, such as `ten`, the function should print `Sorry, ten is not a score` and ask again. It currently crashes with a `ValueError` instead, because `int()` cannot convert the word `ten` into a number.

```text
Enter a quiz score, or done to finish: 90
Enter a quiz score, or done to finish: ten
Sorry, ten is not a score
Enter a quiz score, or done to finish: 85
Enter a quiz score, or done to finish: done
```

Here `broken_score_total()` should return `175`.

Fix it with a guard clause. A **guard clause** here is an `if` that runs `continue`. `continue` abandons the current trip through the loop and starts the next one, skipping the rest of the body, so `int(score)` never receives an answer it cannot convert, and the loop goes straight back to asking. The tests check you used it.

As in Question 9, the tests type the answers for you, one answer for each call to `input()`.

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Pushing runs the tests on GitHub. Check the **Actions** tab for your score,
then open a pull request to your instructor for feedback.

## Good luck!

Off-by-one errors are a rite of passage. When a loop misbehaves, print the
counter and watch what it actually does. You got this!
