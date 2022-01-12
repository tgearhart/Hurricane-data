# names of hurricanes


names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:
def updated_damages(damage):
    updated_damage = []
    for dam in damages:
        if dam[-1] == "B":
            new_num1 = float(dam[:-1])
            new_num2 = new_num1 * 1000000000
            updated_damage.append(new_num2)
        elif dam[-1] == "M":
            new_num1 = float(dam[:-1])
            new_num2 = new_num1 * 1000000
            updated_damage.append(new_num2)
        else:
            updated_damage.append(dam)

    return updated_damage


damages = updated_damages(damages)


# write your construct hurricane dictionary function here:

def hurricane_name(names, months, years, max_winds, area_affected, damages, deaths):
    new_dictionary = {}
    pre_list = zip(names, months, years, max_winds, area_affected, damages, deaths)
    for hurr in pre_list:
        temp_dictionary = {hurr[0]: {'Name': hurr[0], 'Month': hurr[1], 'Year': hurr[2], 'Max Sustained Winds': hurr[3], \
                                     'Areas Affected': hurr[4], 'Damages': hurr[5], 'Deaths': hurr[6]}}
        new_dictionary.update(temp_dictionary)
    return new_dictionary


hurricane_name_dict = hurricane_name(names, months, years, max_sustained_winds, areas_affected, damages, deaths)


# write your construct hurricane by year dictionary function here:
def hurricane_year(dictionary):
    year_dictionary = {}
    for i in dictionary:
        year = dictionary[i]['Year']
        name = dictionary[i]
        if year not in year_dictionary:
            year_dictionary[year] = [name]
        else:
            year_dictionary[year].append(name)
    return year_dictionary


hurricane_year_dict = hurricane_year(hurricane_name_dict)


# print(hurricane_year_dict.get(2005))


# write your count affected areas function here:
def rate_of_affection(dictionary):
    rate_dictionary = {}
    for i in dictionary:
        for a in dictionary[i]['Areas Affected']:
            if a not in rate_dictionary.keys():
                rate_dictionary[a] = 1
            else:
                rate_dictionary[a] += 1
    return rate_dictionary


rate_test = rate_of_affection(hurricane_name_dict)

sorted_rate = sorted(rate_test.items())


# print(sorted_rate)


# write your find most affected area function here:
def most_affected(dictionary):
    most_affected_area = max(dictionary, key=dictionary.get)
    return most_affected_area


# print(most_affected(rate_test))

# write your greatest number of deaths function here:

def most_deaths(dictionary):
    deaths = {}
    for i in dictionary:
        death = dictionary[i]['Deaths']
        name = dictionary[i]['Name']
        deaths[name] = [death]
    deadly = max(deaths, key=deaths.get)
    print("The most deaths are from hurricane: " + str(deadly) + " with " + str(deaths[deadly]) + " killed")
    return deadly, deaths[deadly]


# print(most_deaths(hurricane_name_dict))


# write your catgeorize by mortality function here:


def hurricane_mortality(dictionary):
    mortality_dictionary = {}
    for i in dictionary:
        deaths = dictionary[i]['Deaths']
        if deaths == 0:
            dictionary[i]['Mortality'] = 0
        elif deaths <= 100:
            dictionary[i]['Mortality'] = 1
        elif deaths <= 500:
            dictionary[i]['Mortality'] = 2
        elif deaths <= 1000:
            dictionary[i]['Mortality'] = 3
        elif deaths <= 10000:
            dictionary[i]['Mortality'] = 4
        elif deaths > 10000:
            dictionary[i]['Mortality'] = 5
    for a in dictionary:
        mortal = dictionary[a]['Mortality']
        name = dictionary[a]
        if mortal not in mortality_dictionary:
            mortality_dictionary[mortal] = [name]
        else:
            mortality_dictionary[mortal].append(name)

    return mortality_dictionary


mortality_sorted_dictionary = hurricane_mortality(hurricane_name_dict)


# print(mortality_sorted_dictionary)


# write your greatest damage function here:
def most_damage(dictionary):
    dam = {}
    dam2 = {}
    for i in dictionary:
        d = dictionary[i]['Damages']
        name = dictionary[i]['Name']
        dam[name] = d
    for a in dam:
        if dam[a] != "Damages not recorded":
            dam2[a] = dam[a]
    most = max(dam2, key=dam2.get)
    print("The most damaging hurricane was " + str(most) + " with " + str((dam[most])) + " dollars in damage")
    return most, dam2[most]


most_damage(hurricane_name_dict)


# write your catgeorize by damage function here:

def hurricane_damage(dictionary):
    damage_dictionary = {}
    for i in dictionary:
        dam = dictionary[i]['Damages']
        if dam == 0:
            dictionary[i]['Damage Scale'] = 0
        elif dam <= 100000000:
            dictionary[i]['Damage Scale'] = 1
        elif dam <= 1000000000:
            dictionary[i]['Damage Scale'] = 2
        elif dam <= 10000000000:
            dictionary[i]['Damage Scale'] = 3
        elif dam <= 50000000000:
            dictionary[i]['Damage Scale'] = 4
        elif dam > 50000000000:
            dictionary[i]['Damage Scale'] = 5
    for a in dictionary:
        dam_scale = dictionary[a]['Damage Scale']
        name = dictionary[a]
        if dam_scale not in damage_dictionary:
            damage_dictionary[dam_scale] = [name]
        else:
            damage_dictionary[dam_scale].append(name)

    return damage_dictionary


print(hurricane_damage(hurricane_name_dict))

