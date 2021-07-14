def convert_fahrenheit_to_celsius(fahrenheit_number):

    try:
        fahrenheit_number = float(fahrenheit_number)
    except:
        return("```Error, please input a number. Example of proper usage:\n\n*ftc 25```")

    celsius_number = (fahrenheit_number - 32) * 5/9
    celsius_number = round(celsius_number, 4)

    return(f"{fahrenheit_number}°F is {celsius_number}°C.")
