
def main():
    print_the_header()

    code = input('What zipcode do you want the weather for (01010)? ')

    get_html_from_web(code)


def print_the_header():
    print('-------------------------------')
    print('          WEATHER APP')
    print('-------------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    print(url)


if __name__ == '__main__':
    main()
