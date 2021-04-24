**Using roll() in Your Own Code**
=================================

.. figure:: python_screen.png

For Simple Die Rolls
--------------------

Sample Outputting of Die Rolls: ::

    # import the roll() module
    from PyDiceroll import roll

    # enter the roll type to be made
    number_of_dice = input('Number of dice to roll? ')
    dice_type = input('Dice type? ')
    dice_roll_modifier = input('DM? ')

    # make sure that there is a plus or minus sign in the DM string
    if dice_roll_modifier[0] != '-' and dice_roll_modifier[0] != '+':
        dice_roll_modifier = '+' + dice_roll_modifier

    # concatenate the values for the dice string
    dice = number_of_dice + dice_type + dice_roll_modifier

    print()
    print('Rolling', dice)

    # do 20 rolls
    for i in range(20):
        print('You rolled a %d' % roll(dice))

For Probabilites
----------------

Sample Task Resolution: ::
    
	# import the roll() module
	from PyDiceroll import roll

	# Enter your character's chances to succeed at a task
	skilled = input('Is your character trained for the task ([y]/n)? ')
	if skilled == 'n':
		die_mod = -3
	else:
		print("Enter your character's skill level")
		die_mod = int(input('(0 to 4)? '))
	print('Enter the difficulty of the task')
	difficulty = int(input('(Simple: +2 to Impossible: +16)? '))

	# The player must roll the difficulty or higher for their character to succeed
	dice_roll = roll('2D6') + die_mod
	print()
	print('You rolled:', dice_roll)
	if dice_roll >= difficulty:
		print('Your character succeeds with the task.')
		if dice_roll - difficulty >= 6:
			print('Your character saved everyone.')
	else:
		print('Your character fails at the task.')
		if dice_roll - difficulty < -3:
			print('Your character becomes injured.')
		if dice_roll - difficulty < -6:
			print('Your character died from injuries!')

For Repairing Game Code
-----------------------

.. figure:: broken_die.png

Often times, game code will be downloaded or found that contains
incorrect ``randint()`` calls for rolling two 6-sided dice. A line such as: ::

    world_size = randint(2, 12) - 2

Easily becomes: ::
    
    world_size = roll('2d6') - 2

Encountering Errors
-------------------
Entering an invalid string for ``roll()`` will return an error message, as well as a value of 0 from the function: ::

   print(roll('3d1'))

.. error::

   ** DICE ERROR! '3D1' is unknown **
   
   | 0
