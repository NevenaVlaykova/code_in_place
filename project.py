"""
This program is a Carbon Footprint Calculator and it estimates the
environmental cost of your next planned trip. It will help you find out ways to
reduce and offset your footprint by giving you fun suggestions on how to make
some impactful changes in your everyday life.

Side note: this is a simplified version of a carbon footprint calculator and
it assumes some average values for the emissions produced by different
transport options. Future updates would aim to incorporate variations among
vehicle models, date of production, country of origin, and many more
contributing factors. Sources and notes on methodology can be found in the
accompanying 'References_and_Notes' file (in the same folder as the .py file).
"""

import time


def main():
    """
    The vehicles_dict shows greenhouse gas emissions generated by different
    modes of transport. Values are in g CO2-equivalent (CO2-eq) per passenger,
    per km travelled
    """
    vehicles_dict = {'airplane': 254,  # value for domestic flight only
                     'car': 171,  # average diesel car
                     'train': 41,
                     'coach': 27}

    # First get user input on choice of transport, passengers, and distance
    display_intro()
    vehicle = choose_transportation(vehicles_dict)
    passengers = choose_passengers(vehicle)
    distance = choose_distance()
    # Display summary of footprint and offer to change transportation
    footprint = calculate_footprint(vehicles_dict, vehicle, passengers,
                                    distance)
    display_results(vehicles_dict, passengers, distance, footprint)
    footprint = change_vehicle(vehicles_dict, vehicle, passengers, distance)
    # Second part: offer mitigation options
    display_mitigation_intro()
    mitigation_options = ['plant trees',
                          'change diet',
                          'consume less energy']
    pick_mitigation(mitigation_options, footprint)
    # Offer picking different mitigation
    change_mitigation(mitigation_options, footprint)
    display_final_message()


def change_mitigation(mitigation_options, footprint):
    # asks user to pick a different mitigation
    while True:
        question = input('\nSounds like a lot of work? Want to try picking a '
                         'different option? (y/n)')
        answer = answer_check(question)
        if answer == 'y':
            pick_mitigation(mitigation_options, footprint)
        else:
            break


def answer_check(question):
    # checks whether the user gave correct input (either 'y' or 'n')
    answer = question.lower()
    while answer != 'y' and answer != 'n':
        question = input('Please type in either \'y\' or \'n\'.')
        answer = question.lower()
    return answer


def item_check(item, item_dict):
    # checks whether user input is from the relevant dict
    answer = item.lower()
    while answer not in item_dict.keys():
        repeat_question = input('You seem to have typed in an item that is '
                                'not on the list. Please try again: ')
        answer = repeat_question.lower()
    return answer


def consume_less_energy():
    # provides user with a list of tips on how to consume less energy
    energy_list = ['use compact fluorescent bulbs (CFL) bulbs',
                   'make sure to turn off lights when you leave a room',
                   'turn off your computer when not in use or set to'
                   ' sleep/hibernate mode',
                   'print double sided',
                   'take the stairs instead of the elevator',
                   'avoid purchasing new electronics unless it is necessary '
                   '(yes, you don\'t urgently need that new iphone just '
                   'because the next model came out)',
                   'when purchasing new electronics, go for high '
                   'efficiency and energy saving ones',
                   'choose second-hand whenever you can',
                   'try to repair before throwing away',
                   'use rechargeable batteries',
                   'install PV panels',
                   'install a solar water heater',
                   'install low flow showerheads, faucets, toilets',
                   'improve the insulation of your house',
                   'line dry clothing',
                   'reduce your waste and recycle']
    print('\nHere are a few ways to reduce your energy consumption:\n')
    for line in energy_list:
        print('-- ' + line)
    user_input = input('\nCan you pick at least five options from the list and'
                       ' stick to them? (y/n)')
    answer = answer_check(user_input)
    if answer == 'y':
        print('\nGreat job, the planet will thank you!')


def change_diet(footprint):
    # Dict of kg CO2-eq equivalent per kg of food type
    food_dict = {'beef': 59.6,
                 'lamb': 24.5,
                 'cheese': 21.2,
                 'dark chocolate': 18.7,
                 'coffee': 16.5,
                 'shrimps': 11.8,
                 'pork': 7.2,
                 'poultry': 6.1,
                 'fish': 5.1,
                 'eggs': 4.5,
                 'rice': 4,
                 'tofu': 3,
                 'milk': 2.8,
                 'cane sugar': 2.6}
    print('\nWhich of the following foods are you willing to stop consuming?'
          '\n')
    for key in food_dict.keys():
        print('-- ' + key)
    user_input = input('\nSelect one of the above or press Enter to skip: ')
    # keep asking user to pick different food to experiment with results
    while user_input != '':
        answer = item_check(user_input, food_dict)
        calculate_food_footprint(answer, footprint, food_dict)
        user_input = input('\nWant to try again? Type in a new food or press '
                           'Enter to skip: ')


def calculate_food_footprint(answer, footprint, food_dict):
    food = answer.lower()
    # calculate total amount of kilos that need to not be consumed to mitigate
    total_kilos = round(footprint / food_dict[food], 1)
    print('\nTo make up for the emissions you are about to spend on your trip'
          ' you will need to say no to a total of ' + str(total_kilos)
          + ' kilos of ' + food + '.')


def plant_trees(footprint):
    # how many kg CO2-eq emissions does one tree make up for per year
    one_tree = 22
    # calculate how many trees you need ot plant in that year
    total_trees = int(footprint / one_tree)
    if total_trees <= 1:
        total_trees = 1
        plural_string = ''
    else:
        plural_string = 's'
    print('\nTo make up for the CO2-eq emissions from your journey, you will '
          'need to plant ' + str(total_trees) + ' tree' + plural_string
          + '.')


def pick_mitigation(mitigation_options, footprint):
    # ask user to pick a mitigation method
    for elem in mitigation_options:
        print('-- ' + elem)
    user_input = input('\nType in your choice: ')
    mitigation = user_input.lower()
    while mitigation not in mitigation_options:
        user_input = input('You seem to have typed in an item that is not on '
                           'the list. Please try again: ')
        mitigation = user_input.lower()
    if mitigation == 'plant trees':
        plant_trees(footprint)
    elif mitigation == 'change diet':
        change_diet(footprint)
    elif mitigation == 'consume less energy':
        consume_less_energy()
    return mitigation


def display_mitigation_intro():
    message = ['\nWow, looks scary, huh?',
               'Don\'t worry, there are a lot of things you can do to reduce '
               'your yearly carbon footprint.',
               'Which of the following options are you willing to try?\n']
    for line in message:
        print(line)
        time.sleep(2)


def change_vehicle(vehicles_dict, vehicle, passengers, distance):
    # offers user to change vehicle before continuing
    new_choice = input('\nWould you like to change your vehicle? '
                       'Press "y" to try again or "n" to continue.')
    answer = answer_check(new_choice)
    if answer == 'y':
        vehicle = choose_transportation(vehicles_dict)
        if vehicle == 'car':
            passengers = choose_passengers(vehicle)
    # calculate the per capita footprint for this journey in kg
    footprint = calculate_footprint(vehicles_dict, vehicle, passengers,
                                    distance)
    print('\nGreat, we are all set! You have chosen to travel ' + str(distance)
          + ' km by ' + str(vehicle) + '.'
          + '\nSo by going on this trip you will spend ' + str(footprint)
          + ' kg CO2-eq emissions.')
    return footprint


def display_results(vehicles_dict, passengers, distance, footprint):
    summary = ['\nYour estimated footprint for this journey is ' +
               str(footprint) + ' kg CO2-eq emissions per passenger.',
               '\nThis is how your chosen transportation compares to other '
               'alternatives:\n']
    for line in summary:
        print(line)
        time.sleep(2)
    for key in vehicles_dict.keys():
        alternative_footprint = calculate_footprint(vehicles_dict, key,
                                                    passengers, distance)
        print(str(key) + ':  ' + str(alternative_footprint) + ' kg')
    print('-' * 20)


def calculate_footprint(vehicles_dict, vehicle, passengers, distance):
    # for long haul flights emissions need to be adjusted
    if distance > 1000:
        vehicles_dict['airplane'] = 195
    vehicle_emissions = vehicles_dict[vehicle]
    # calculate the per capita footprint for this journey in kg
    footprint = round((((vehicle_emissions * distance) / passengers) / 1000),
                      1)
    return footprint


def choose_distance():
    distance = int(input('\nHow many km are you planning to travel? '))
    return distance


def choose_passengers(vehicle):
    # if the vehicle is a car you can pick more than 1 passenger
    if vehicle == 'car':
        passengers = int(input('\nHow many passengers would there be in the '
                               'car? '))
        if passengers < 1:
            passengers = int(input('\nPlease enter at least one passenger: '))
        if passengers < 2:
            new_choice = input(
                '\nIt seems that when it comes to reducing the carbon'
                ' footprint of your car, the main rule is: the more the '
                'merrier.\nWith that in mind, would you like to take more '
                'passengers along on your journey? (y/n) ')
            answer = answer_check(new_choice)
            if answer == 'y':
                passengers = int(input('\nHow many passengers would there be '
                                       'in the car? '))
        if passengers > 8:
            passengers = int(input('\nThe maximum number of passengers you '
                                   'can have is 8. Please pick again: '))
    else:
        passengers = 1
    return passengers


def choose_transportation(vehicles_dict):
    print('\nSelect your preferred mode of transportation:\n')
    for key in vehicles_dict.keys():
        print('-- ' + key)
    user_input = input('\nType in your choice: ')
    vehicle = item_check(user_input, vehicles_dict)
    return vehicle


def display_intro():
    intro_message = ['Hi there!',
                     'So you are stuck at home during the COVID-19 outbreak, '
                     'huh?',
                     'Longing for a break outside?',
                     'Maybe you find yourself daydreaming of a day on the '
                     'beach...',
                     '...or a hike in the mountains...',
                     'How about we daydream together? Let\'s help you plan '
                     'your next trip!',
                     'But let\'s also do it sustainably and calculate your '
                     'carbon footprint for that journey.']
    for line in intro_message:
        print(line)
        time.sleep(2)


def display_final_message():
    final_message = ['\nFeeling overwhelmed?',
                     'Don\'t want to give up your beef burger?',
                     'You\'re not that much into cycling or hiking, either?',
                     'That\'s fine. If all else fails, you can always just '
                     'stay home and \'code in place\' :)']
    for line in final_message:
        print(line)
        time.sleep(2)


if __name__ == '__main__':
    main()