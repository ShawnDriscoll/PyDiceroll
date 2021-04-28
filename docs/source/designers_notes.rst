**Designer's Notes**
====================

In the Beginning
----------------
One of the first things I do when learning a new language is to
discovery how it generates random numbers. Older computer languages
from the '70s had their own built-in random number generators. Technically,
they were pseudo-random number generators. But technically, I wanted to
program my Star Trek games anyway no matter what they were called.

In the '80s, I would discover that not all computer languages came
with random number generators built in. Many didn't have such a thing
unless some external software library was installed. Both FORTRAN and C
couldn't do random anything out of the box. A math library had to be picked from
the many that were out there. And if none were available, a computer class on campus
was available to teach you how to program your own random number generator from scratch.

By the '90s, random number generators were pretty much standardized as
for as how accurately random they were. And they were included in standard
libraries for various languages. By the time Python was being developed, the
C language used to write Python had very robust random number generators.
And because Python was written in C, it just made sense for it to make
use of C libraries.

For those that are curious, **PyDiceroll** uses the ``random.randint()`` module that comes
with CPython. There are stronger random generators out there now, with NumPy being one
of them. But at the time of designing **PyDiceroll**, I didn't quite understand how-all
NumPy worked, or what version of it to install. And for rolling dice, the built-in
random number generator would be just fine.

Lessons Learned
---------------
In the past, when I needed a random number from 1 to say 6 (see 6-sided dice), I would use ``INT(RND(1)*6) + 1``.
And I would be used to doing it that way for probably 15 years or so, because that is
how most BASIC languages did things. Other languages like C required me to whip out the
80286 System Developer's 3-ring binder to find out how ``srand()`` and ``rand()`` worked,
and under what circumstances.

Fast-forward 20 years, and I'm learning CPython without knowing the difference between a CPython
or an RPython or any other Python out there. I figured Python was the same all over, even though
I had a feeling Linux did things differently because of its filepath naming and OS commands. And
of course, the first thing I had to try was Python's ``random`` module, as well as its
ugly-looking ``randint()``.

Right away I noticed the way Python "loaded" modules was going to be a learning experience. I
hadn't really programmed anything huge since my TANDY Color Computer 3 days running OS-9 Level II
and programming in BASIC09 (https://en.wikipedia.org/wiki/BASIC09). Python would reveal different
ways of importing modules the more I read about them, and the more code I poured over.

I would soon find that: ::

   import random
   
   print(random.randint(1, 6)) # roll a 6-sided die

Was the same thing as: ::

   from random import randint
   
   print(randint(1, 6)) # roll a 6-sided die

Which looked a bit cleaner. But I was debating if I wanted to use ``randint()`` at all in
my normal coding.

So while I was learning how to write my own functions, as well as how to go about importing them, I came up with
an idea for **PyDiceroll**. It would include a ``roll()`` function, and a ``die_rolls()`` function as
a "side effect." Even though ``die_rolls()`` had no error-checking, ``roll()`` would call it after
doing its own error-checking.

I was trying to avoid using: ::

   from PyDiceroll import die_rolls
   
   print(die_rolls(6, 2)) # roll two 6-sided dice

For my dice rolls, I wanted something more readable. Something like: ::

   from PyDiceroll import roll
   
   print(roll('2D6')) # roll two 6-sided dice

It was almost less typing, which I thought was great because I was going to be typing this function a lot
for a Python project I had in mind. And it would be a lot easier to spot what kind of rolls were being made in my
code. And the simple addition or subtraction of DMs to such a roll was making the function more appealing: ::

   print(roll('2D6+3')) # roll two 6-sided dice and add a DM of +3 to it

The Channel 1
-------------
**diceroll** was written years ago. The Classic Python 2.5 code was used by both my TravCalc and TravGen apps, and got looked at
by GitHub visitors who would google-by now and again. But not many programmers will ever use the code because of the simple fact
that Python is now version 3.9+ something. So **diceroll**, along with a slew of other pre-Python 2.6 era modules,
are the Channel 1 stations in the room that no TV can possibly watch.

It really comes down to a philosophy. I waited on learning Python until a version was released where I could say,
*"This is Python."* Or say, *"This is what Python should be."* Something like that. Well... Python 2.5.4 was my Python.

I once said, *"I believe the next great computer programming language will be the one that remains true to its nature/design as
it grows. And doesn't split the party as it grows."* I hung onto Python 2.5.4 for as long as possible. For a good fifteen years. Or I should
say for a *great* fifteen years. Because they were great. But most great things come with an ending to them.

And so it was, that yesterday I would uninstall Python 2.5.4 along with all its things. And today, I would begin the installation of
Python 3.9.4. I guess one could say it was the terminated support for Python 2.x this year that nudged me, along with some of the
older Python 3.x terminations as well. Even Python 3.9+ saw earlier Python 3's as dead weight (Python 3's that I didn't want to deal with either), such
as 3.0, 3.1, 3.2, 3.3, 3.4, and 3.5. And now they are gone. And I can skip ahead to a refined version of Python 3 with no baggage
from 2.6 or 2.7 whatsoever.





| *Shawn Driscoll*
| *April 23rd, 2021*
| *US, California*