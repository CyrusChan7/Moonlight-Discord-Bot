def convert_celsius_to_fahrenheit(celsius_number):

    try:
        celsius_number = float(celsius_number)
    except:
        return("```Error, please input a number. Example of proper usage:\n\n*ctf 20```")

    fahrenheit_number = (celsius_number * 9/5) + 32
    fahrenheit_number = round(fahrenheit_number, 4)

    return(f"{celsius_number}°C is {fahrenheit_number}°F.")