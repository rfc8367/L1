def menu():
    print("1. Перевести градус Цельсия °C в градусы Фаренгейта °F и Кельвина °K")
    print("2. Перевести градус Фаренгейта °F в градусы Цельсия °C и Кельвина °K")
    print("3. Перевести градус Кельвина °K в градусы Цельсия °C и Фаренгейта °F")
    print("4. Выход")
    return int(input("Выберите действие: "))




def CelsiusToFahrenheit(celsius):
    return float((celsius * 1.8) + 32)

def CelsiusToKelvin(celsius):
    return float((celsius + 273.15))




def FahrenheitToCelsius(fahrenheit):
    return float((fahrenheit-32) / 1.8)

def FahrenheitToKelvin(fahrenheit):
    return float((fahrenheit + 459.67) * 0.555556)




def KelvinToCelsius(kelvin):
    return float(kelvin - 273.15)

def KelvinToFahrenheit(kelvin):
    return float((kelvin * 1.8) - 459.67)




def temperatures():
    choice = menu()
    while choice != 4:
        if choice == 1:
            celsius = float(input("Введите градусы Цельсия: "))
            CF = (str(CelsiusToFahrenheit(celsius)) + " °F")
            CK = (str(CelsiusToKelvin(celsius)) + " °K")
            print(CF, CK)

        elif choice == 2:
            fahrenheit = int(input("Введите градусы Фаренгейта: "))
            FC = (str(FahrenheitToCelsius(fahrenheit)) + " °C")
            FK = (str(FahrenheitToKelvin(fahrenheit)) + " °K")
            print(FC, FK)

        elif choice == 3:
            kelvin = int(input("Введите градусы Кельвина: "))
            KC = (str(KelvinToCelsius(kelvin)) + " °C")
            KF = (str(KelvinToFahrenheit(kelvin)) + " °F")
            print(KC, KF)
        else:
            print("Неправильный ввод данных")
        choice = menu()
temperatures()    
