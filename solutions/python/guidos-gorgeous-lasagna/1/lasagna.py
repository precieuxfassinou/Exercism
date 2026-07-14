"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):

    """Calculate the bake time remaining.
    
    Parameters:
        elapsed_bake_time (int): Baking time already elapsed in minutes.
        
    Returns:
        int: Remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    This function takes an integer representing the minutes the lasagna 
    has been baking in the oven. It calculates the remaining minutes 
    needed to finish baking.
    
    """
    
    elapsed_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return(elapsed_bake_time)

bake_time_remaining(25)

def preparation_time_in_minutes(minutes_of_layers):

    """Calculate the preparation time in minutes.
    
    Parameters:
        minutes_of_layers (int): The number of layers added to the lasagna.
        
    Returns:
        int: The total time elapsed (in minutes) to prepare the layers.

    This function takes an integer representing the number of layers 
    in the lasagna. It calculates the total preparation time, assuming 
    each layer takes 2 minutes to prepare.
    
    """

    minutes_of_layers = minutes_of_layers * 2
    return(minutes_of_layers)

preparation_time_in_minutes(2)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """

    number_of_layers = number_of_layers * 2
    return(number_of_layers + elapsed_bake_time)
    
elapsed_time_in_minutes(3, 20)
