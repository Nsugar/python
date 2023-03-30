def get_string(city,country,population = ''):
    if not population:
        get_combination = f"{city},{country}"
        return get_combination.title()
    else:
        get_combination = f"{city},{country} - population {population}"
        return get_combination.title()