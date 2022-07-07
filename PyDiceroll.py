#
#   PyDiceroll.py
#
#   Written for Python 3.9.11
#
#   To use this module: from PyDiceroll import roll
#
#   Make a dice roll
#
##########################################################

'''
PyDiceroll module containing roll()

Usage:
    from PyDiceroll import roll
    print(roll('2D6'))

    Will roll two 6-sided dice, returning an integer
'''

from random import randint
import os
import logging
import sys

__version__ = '3.7'
__release__ = '3.7.1b'
__py_version__ = '3.9.11'
__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'

diceroll_log = logging.getLogger('PyDiceroll')
diceroll_log.setLevel(logging.INFO)

if not os.path.exists('Logs'):
    os.mkdir('Logs')

fh = logging.FileHandler('Logs/PyDiceroll.log', 'w')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s',
                              datefmt = '%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
diceroll_log.addHandler(fh)

diceroll_log.info('Logging started.')
diceroll_log.info('roll() v' + __version__ + ' started, and running...')

number_of_dice = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
simple_dice = ['D3', 'D4', 'D5', 'D6', 'D8', 'D10', 'D12', 'D20', 'D30']
traveller5_dice = ['1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D']
fate_dice = ['1DF', '2DF', '3DF', '4DF']

__error__ = -9999

def _dierolls(dtype, dcount):
    '''
    Takes two integer arguments:
        dtype (the number of sides for the dice)
        dcount (the number of dice to roll)
    
    and returns an integer value.
    
    This function is for internal use and has no error-checking!    
    '''

    dtotal = 0
    if dcount == 1:
        diceroll_log.debug('Using %s %d-sided die...' % (number_of_dice[dcount], dtype))
    else:
        if dcount < 11:
            diceroll_log.debug('Using %s %d-sided dice...' % (number_of_dice[dcount], dtype))
        else:
            diceroll_log.debug('Using %d %d-sided dice...' % (dcount, dtype))
        
    for i in range(dcount):
        rolled = randint(1, dtype)
        if rolled == 8 or rolled == 11 or rolled == 18 or rolled >= 80 and rolled <= 89:
            diceroll_log.debug('Rolled an %s' % rolled)
        else:
            diceroll_log.debug('Rolled a %s' % rolled)
        dtotal += rolled
    return dtotal

def roll(dice):
    '''
    The dice types to roll are:
        '4dF', 'D2', 'D3', 'D4', 'D5', 'D6', 'D8', 'D09', 'D10',
        'D12', 'D20', 'D30', 'D099', 'D100', 'D44', 'D66', 'D88', 'DD',
        'FLUX', 'GOODFLUX', 'BADFLUX', 'BOON', 'BANE', 'ADVANTAGE',
        'DISADVANTAGE', and also Traveller5's 1D thru 10D rolls

    Some examples are:
    roll('D6') or roll('1D6') -- roll one 6-sided die
    roll('2D6') -- roll two 6-sided dice
    roll('D09') -- roll a 10-sided die (0 - 9)
    roll('D10') -- roll a 10-sided die (1 - 10)
    roll('D099') -- roll a 100-sided die (0 - 99)
    roll('D100') -- roll a 100-sided die (1 - 100)
    roll('D66') -- roll for a D66 chart
    roll('FLUX') -- a FLUX roll (-5 to 5)
    roll('3D6+6') -- add +6 DM to roll
    roll('4D4-4') -- add -4 DM to roll
    roll('2DD+3') -- roll (2D6+3) x 10
    roll('BOON') -- roll 3D6 and keep the higher two dice
    roll('4dF') -- make a FATE roll
    roll('4D') -- make a Traveller5 4D roll
    roll('info') -- release version of program
    
    An invalid roll will return a -9999 value.
    '''

    log = logging.getLogger('PyTravCalc.PyDiceroll')

    # make inputted string argument upper case, and remove spaces
    dice = str(dice).upper().replace(' ','')
    
    # was information for this program asked for?
    if dice == 'INFO':
        ver = 'roll(), release version ' + __release__ + ' for Python ' + __py_version__
        diceroll_log.info('Reporting: roll() release version: %s' % __release__)
        return __version__, ver
    
    # was a test asked for?
    if dice == 'TEST':
        diceroll_log.info('A 6x6 test was started...')
        roll_chart_6x6 = {}
        data = []
        for i in range(13):
            data.append(0)
        n = 10000
        
        for i in range(6):
            for j in range(6):
                roll_chart_6x6[(i+1, j+1)] = 0
        print()
        print('      6x6 Roll Chart Test')
        print('     1    2    3    4    5    6')
        for i in range(n):
            die1 = _dierolls(6, 1)
            die2 = _dierolls(6, 1)
            roll_chart_6x6[(die1, die2)] += 1
            result = die1 + die2
            data[result] += 1
                
        for i in range(6):
            print(i+1, end=' ')
            for j in range(6):
                print('%4d' % roll_chart_6x6[(i+1, j+1)], end=' ')
            print()
        
        for i in range(6):
            for j in range(6):
                roll_chart_6x6[(i+1, j+1)] = 0
        print()
        print('            6x6 Roll Chart Percentage')
        print('        1       2       3       4       5       6')
        for x in range(13):
            if x > 1:
                for i in range(6):
                    for j in range(6):
                        if (i+1)+(j+1) == x and roll_chart_6x6[(i+1, j+1)] == 0:
                            roll_chart_6x6[(i+1, j+1)] = data[x]
        
        for i in range(6):
            print(i+1, end=' ')
            for j in range(6):
                print('%6.2f%%' % (roll_chart_6x6[(i+1, j+1)] * 100. / n), end=' ')
            print()
        print()
        diceroll_log.info('6x6 test completed 100%.')
        for x in range(len(data)):
            data[x] = data[x] * 100. / n
        return data[2:13]

    # was a min/max/avg asked for?
    if dice == 'MINMAXAVG':
        rolls_for_test = ['1d2', '1d3', '1d4', '1d5', '1d6', '1d8', '1d09', '1d10', '1d12', '1d20', '1d30', '1d099', '1d100',
                  '1df', '2df', '3df', '4df', 'flux', 'goodflux', 'badflux', 'boon', 'bane', 'advantage', 'disadvantage',
                  '2d4', '3d4', '4d4',
                  '2d6', '3d6', '4d6',
                  '2d8', '3d8', '4d8',
                  '2d09', '3d09', '4d09',
                  '2d10', '3d10', '4d10',
                  '2d12', '3d12', '4d12',
                  '2d20', '3d20', '4d20', '3d6+1', '2d6-2', '2d6-7',
                  '1dd', '2dd', '3dd', '4dd']

        print()
        print('Using brute force...')
        print()

        total_numbers = 2000

        for i in range(len(rolls_for_test)):
            test_roll = rolls_for_test[i]
            minimum = 100000000
            maximum = 0
            total_sum = 0
            for n in range(total_numbers):
                die = roll(test_roll)
                if minimum > die:
                    minimum = die
                if maximum < die:
                    maximum = die
                total_sum += die
            sample = []
            for x in range(10):
                sample.append(roll(test_roll))

            print('Test Roll: %s, Min: %d, Max: %d, Avg: %.1f, ' % (test_roll, minimum, maximum, total_sum / total_numbers) + 'Sample:', sample)

        print()
        print('Increase the value of total_numbers in PyDiceroll to improve its precision.')
        print()
        return

    log.debug(dice)
    diceroll_log.debug("Asked to roll '%s':" % dice)

    # check if a FATE dice roll
    dF_dice = dice
    dice_mod = 0
    ichar2 = dice.find('+')
    if ichar2 != -1:
        dice_mod = int(dice[ichar2:len(dice)])
        dF_dice = dice[0:ichar2]
    else:
        ichar2 = dice.find('-')
        if ichar2 != -1:
            dice_mod = int(dice[ichar2:len(dice)])
            dF_dice = dice[0:ichar2]
    if dF_dice in fate_dice:
        num_dice = int(dF_dice[0:len(dF_dice) - 2])
        rolled = 0
        for rolls in range(num_dice):
            rolled += _dierolls(3, 1) - 2
        rolled += dice_mod
        diceroll_log.info("'%s' = %d%s+%d = %d" % (dice, num_dice, 'dF', dice_mod, rolled))
        return rolled

    # set dice modifier to zero
    dice_mod = 0
    
    # check if FLUX dice are being rolled
    elif dice == 'FLUX':
        flux1 = _dierolls(6, 1)
        flux2 = _dierolls(6, 1)
        rolled = flux1 - flux2
        diceroll_log.info("'%s' = %d - %d = %d" % (dice, flux1, flux2, rolled))
        return rolled

    elif dice == 'GOODFLUX':
        flux1 = _dierolls(6, 1)
        flux2 = _dierolls(6, 1)
        if flux1 < flux2:
            rolled = flux2 - flux1
            diceroll_log.info("'%s' = %d - %d = %d" % (dice, flux2, flux1, rolled))
        else:
            rolled = flux1 - flux2
            diceroll_log.info("'%s' = %d - %d = %d" % (dice, flux1, flux2, rolled))
        return rolled

    elif dice == 'BADFLUX':
        flux1 = _dierolls(6, 1)
        flux2 = _dierolls(6, 1)
        if flux1 > flux2:
            rolled = flux2 - flux1
            diceroll_log.info("'%s' = %d - %d = %d" % (dice, flux2, flux1, rolled))
        else:
            rolled = flux1 - flux2
            diceroll_log.info("'%s' = %d - %d = %d" % (dice, flux1, flux2, rolled))
        return rolled

    # check if a BOON roll is being performed
    elif dice == 'BOON':
        die = [0, 0, 0]
        die[0] = _dierolls(6, 1)
        die[1] = _dierolls(6, 1)
        die[2] = _dierolls(6, 1)
        diceroll_log.info('Start Boon roll: %d %d %d' % (die[0], die[1], die[2]))
        die_swap = True
        while die_swap == True:
            die_swap = False
            for j in range(2):
                if die[j] < die[j+1]:
                    temp_die = die[j]
                    die[j] = die[j+1]
                    die[j+1] = temp_die
                    die_swap = True
        rolled = die[0] + die[1]
        diceroll_log.info('Sorted Boon roll: %d %d %d = %d' % (die[0], die[1], die[2], rolled))
        return rolled
    
    # check if a BANE roll is being performed
    elif dice == 'BANE':
        die = [0, 0, 0]
        die[0] = _dierolls(6, 1)
        die[1] = _dierolls(6, 1)
        die[2] = _dierolls(6, 1)
        diceroll_log.info('Start Bane roll: %d %d %d' % (die[0], die[1], die[2]))
        die_swap = True
        while die_swap == True:
            die_swap = False
            for j in range(2):
                if die[j] > die[j+1]:
                    temp_die = die[j]
                    die[j] = die[j+1]
                    die[j+1] = temp_die
                    die_swap = True
        rolled = die[0] + die[1]
        diceroll_log.info('Sorted Bane roll: %d %d %d = %d' % (die[0], die[1], die[2], rolled))
        return rolled

    # check if an Advantage roll is being performed
    elif dice == 'ADVANTAGE':
        first_d20 = _dierolls(20, 1)
        second_d20 = _dierolls(20, 1)
        diceroll_log.info('Advantage roll: %d and %d' % (first_d20, second_d20))
        if first_d20 < second_d20:
            temp_die = first_d20
            first_d20 = second_d20
            second_d20 = temp_die
        rolled = first_d20
        diceroll_log.info('Advantage roll result: %d' % rolled)
        return rolled

    # check if a Disadvantage roll is being performed
    elif dice == 'DISADVANTAGE':
        first_d20 = _dierolls(20, 1)
        second_d20 = _dierolls(20, 1)
        diceroll_log.info('Disadvantage roll: %d and %d' % (first_d20, second_d20))
        if first_d20 > second_d20:
            temp_die = first_d20
            first_d20 = second_d20
            second_d20 = temp_die
        rolled = first_d20
        diceroll_log.info('Disadvantage roll result: %d' % rolled)
        return rolled
    
    # check if negative number was entered
    elif dice[0] == '-':
        log.error('Negative dice count found! [ERROR]')
        print('Negative dice count found! [ERROR]')
        diceroll_log.error("Negative number of dice = '" + dice + "' [ERROR]")
        return __error__

    else:
        # check if T5 dice are being rolled
        t5_dice = dice
        dice_mod = 0
        ichar2 = dice.find('+')
        if ichar2 != -1:
            dice_mod = int(dice[ichar2:len(dice)])
            t5_dice = dice[0:ichar2]
        else:
            ichar2 = dice.find('-')
            if ichar2 != -1:
                dice_mod = int(dice[ichar2:len(dice)])
                t5_dice = dice[0:ichar2]
        if t5_dice in traveller5_dice:
            num_dice = int(t5_dice[0:len(t5_dice) - 1])
            rolled = _dierolls(6, num_dice) + dice_mod
            diceroll_log.info("Traveller5 '%s' = %d%s+%d = %d" % (dice, num_dice, 'D6', dice_mod, rolled))
            return rolled

    # look for DD in the string (for destructive dice rolls)
    ichar1 = dice.find('DD')
    if ichar1 == -1:
        
        # if not, does the string indicate regular dice for use?
        ichar1 = dice.find('D')
    if ichar1 == 0:
        
        # only one die is being rolled
        num_dice = 1

    if ichar1 != -1:
        if ichar1 != 0:
            
            # is there a number found?
            if dice[0:ichar1].isdigit():
                # how many dice are being rolled?
                num_dice = int(dice[0:ichar1])
            else:
                num_dice = 0
    
        if num_dice >= 1:
            
            # is there a +/- dice modifier for the roll?
            ichar2 = dice.find('+')
            if ichar2 != -1:
                dice_mod = int(dice[ichar2:len(dice)])
            else:
                ichar2 = dice.find('-')
                if ichar2 != -1:
                    dice_mod = int(dice[ichar2:len(dice)])
    
            # what kind of dice are being rolled? D6? D66? etc.
            if ichar2 != -1:
                dice_type = dice[ichar1:ichar2]
            else:
                dice_type = dice[ichar1:len(dice)]
            
            if dice_type in simple_dice:
                rolled = _dierolls(int(dice_type[1:len(dice_type)]), num_dice) + dice_mod
                diceroll_log.info("'%s' = %d%s+%d = %d" % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D2' and num_dice == 1 and dice_mod == 0:
                rolled = _dierolls(2, 1) - 1
                diceroll_log.info("'%s' = %d%s+%d = %d" % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D44' and num_dice == 1 and dice_mod == 0:
                roll_1 = _dierolls(4, 1)
                roll_2 = _dierolls(4, 1)
                rolled = roll_1 * 10 + roll_2
                diceroll_log.info("'%s' = %d%s+%d = %d and %d = %d" % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, rolled))
                return rolled
            elif dice_type == 'D66' and num_dice == 1 and dice_mod == 0:
                roll_1 = _dierolls(6, 1)
                roll_2 = _dierolls(6, 1)
                rolled = roll_1 * 10 + roll_2
                diceroll_log.info("'%s' = %d%s+%d = %d and %d = %d" % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, rolled))
                return rolled
            elif dice_type == 'D88' and num_dice == 1 and dice_mod == 0:
                roll_1 = _dierolls(8, 1)
                roll_2 = _dierolls(8, 1)
                rolled = roll_1 * 10 + roll_2
                diceroll_log.info("'%s' = %d%s+%d = %d and %d = %d" % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, rolled))
                return rolled
            elif dice_type == 'D09':
                roll_total = 0
                for rolls in range(num_dice):
                    rolled = (_dierolls(10, 1) - 1)
                    diceroll_log.debug('Corrected to a roll of %s (because 0-9 values)' % rolled)
                    roll_total += rolled
                roll_total += dice_mod
                diceroll_log.info("'%s' = %d%s+%d = %d" % (dice, num_dice, dice_type, dice_mod, roll_total))
                return roll_total
            elif dice_type == 'D099' and num_dice == 1:
                roll_1 = (_dierolls(10, 1) - 1) * 10
                roll_2 = _dierolls(10, 1) - 1
                rolled = roll_1 + roll_2 + dice_mod
                diceroll_log.info("'%s' = %d%s+%d = %d and %d + %d = %d" % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, dice_mod, rolled))
                return rolled
            elif dice_type == 'D100' and num_dice == 1:
                roll_1 = (_dierolls(10, 1) - 1) * 10
                roll_2 = _dierolls(10, 1)
                rolled = roll_1 + roll_2 + dice_mod
                diceroll_log.info("'%s' = %d%s+%d = %d and %d + %d = %d" % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, dice_mod, rolled))
                return rolled
            elif dice_type == 'DD':
                rolled = (_dierolls(6, num_dice) + dice_mod) * 10
                diceroll_log.info("'%s' = (%d%s+%d) * 10 = %d" % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
                                                    
    log.error('Wrong dice type entered! [ERROR]')
    diceroll_log.error("!!!!!!!!!!!!!!!!!!!!! DICE ERROR! '" + dice + "' is unknown !!!!!!!!!!!!!!!!!!!!!!!!!")
    
    print()
    print("** DICE ERROR! '%s' is unknown **" % dice)
    print("Valid dice rolls are:")
    print("roll('D6') or roll('1D6') -- roll one 6-sided die")
    print("roll('2D6') -- roll two 6-sided dice")
    print("roll('D09') -- roll a 10-sided die (0 - 9)")
    print("roll('D10') -- roll a 10-sided die (1 - 10)")
    print("roll('D099') -- roll a 100-sided die (0 - 99)")
    print("roll('D100') -- roll a 100-sided die (1 - 100)")
    print("roll('D66') -- roll for a D66 chart")
    print("roll('FLUX') -- a FLUX roll (-5 to 5)")
    print("roll('2DD+3') -- roll (2D6+3) x 10")
    print("roll('BOON') -- roll 3D6 and keep the higher two dice")
    print("roll('4D') -- make a Traveller5 4D roll")
    print("roll('4dF') -- make a FATE roll")
    print()
    print("-/+ DMs can be added to rolls:")
    print("roll('3D6+6') -- add +6 DM to roll")
    print("roll('4D4-4') -- add -4 DM to roll")
    print()
    print("roll('info') -- release version of program")
    print()
    return __error__

if __name__ == '__main__':
    diceroll_log.info("PyDiceroll was run without 'roll()' called.  Help will be sent if needed.")
    print()
    if len(sys.argv) < 2:
        print('     Type:')
        print("     'PyDiceroll.py -h' for help")
        print("     'PyDiceroll.py -v' for version")
    elif sys.argv[1] in ['-h', '/h', '--help', '-?', '/?']:
        print('     PyDiceroll is a module (containing a roll function)')
        print('     that needs to be imported into Python.')
        print()
        print('     For example:')
        print('     >>> import PyDiceroll')
        print("     >>> print(PyDiceroll.roll('2d6'))")
        print()
        print('     Or:')
        print('     >>> from PyDiceroll import roll')
        print("     >>> print(roll('2d6'))")
        print()
        print()
        print('     But using the CMD prompt:')
        print("     C:\>PyDiceroll.py roll('2d6')")
        print()
        print('     Or just:')
        print('     C:\>PyDiceroll.py 2d6')
    elif sys.argv[1] in ['-v', '/v', '--version']:
        print('     roll(), release version ' + __release__ + ' for Python ' + __py_version__)
    else:
        dice = ''
        if len(sys.argv) > 2:
            for i in range(len(sys.argv)):
                if i > 0:
                    dice += sys.argv[i]
        else:
            dice = sys.argv[1]
        if "roll('" in dice:
            num = dice.find("')")
            if num != -1:
                dice = dice[6:num]
                dice = str(dice).upper().strip()
                num = roll(dice)
                if dice != 'TEST' and dice != 'INFO':
                    print("Your '%s' roll is %d." % (dice, num))
                    diceroll_log.info("The direct call to PyDiceroll with '%s' resulted in %d." % (dice, num))
                elif dice == 'INFO':
                    print('roll(), release version ' + __release__ + ' for Python ' + __py_version__)
        else:
            dice = str(dice).upper().strip()
            num = roll(dice)
            if dice != 'TEST' and dice != 'INFO':
                print("Your '%s' roll is %d." % (dice, num))
                diceroll_log.info("The direct call to PyDiceroll with '%s' resulted in %d." % (dice, num))
            elif dice == 'INFO':
                print('roll(), release version ' + __release__ + ' for Python ' + __py_version__)
