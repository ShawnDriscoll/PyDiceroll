from PyDiceroll import roll

rolls_for_test = ['1d2', '1d3', '1d4', '1d5', '1d6', '1d8', '1d09', '1d10', '1d12', '1d20', '1d30', '1d099', '1d100',
                  '4df', 'flux', 'goodflux', 'badflux', 'boon', 'bane',
                  '2d4', '3d4', '4d4',
                  '2d6', '3d6', '4d6',
                  '2d8', '3d8', '4d8',
                  '2d10', '3d10', '4d10',
                  '2d12', '3d12', '4d12',
                  '2d20', '3d20', '4d20', '3d6+1', '2d6-2',
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
print('Increase the value of total_numbers to improve the precision.')
print()
