import socket
import requests
import pyfiglet
import qrcode
import whois
import phonenumbers
from phonenumbers import geocoder, carrier
import hashlib
import os
import time
from datetime import datetime
from colorama import Fore, Back, Style, init
from gtts import gTTS

# Initialize Colorama
init(autoreset=True)

def intro():
    ascii_banner = pyfiglet.figlet_format("Lokimux Tool-Kit")
    print(Fore.CYAN + ascii_banner)
    print(Fore.YELLOW + "Choose an option:")
    print(Fore.GREEN + "1. IP to Address Finder")
    print(Fore.GREEN + "2. Website to IP Address")
    print(Fore.GREEN + "3. URL Shortener")
    print(Fore.GREEN + "4. Link to QR Code")
    print(Fore.GREEN + "5. Website Age Finder")
    print(Fore.GREEN + "6. Phone Number Location Finder")
    print(Fore.GREEN + "7. Hash Generator (MD5, SHA1, SHA256)")
    print(Fore.GREEN + "8. File Size Finder")
    print(Fore.GREEN + "9. Current Time")
    print(Fore.GREEN + "10. Currency Converter")
    print(Fore.GREEN + "11. Weather Information")
    print(Fore.GREEN + "12. Random Password Generator")
    print(Fore.GREEN + "13. Check Internet Connectivity")
    print(Fore.GREEN + "14. Get Public IP")
    print(Fore.GREEN + "15. DNS Lookup")
    print(Fore.GREEN + "16. Email Validator")
    print(Fore.GREEN + "17. Reverse DNS Lookup")
    print(Fore.GREEN + "18. Text to Speech")
    print(Fore.GREEN + "19. IP Geolocation")
    print(Fore.GREEN + "20. URL Expander")
    print(Fore.RED + "0. Exit")

def ip_to_address(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return Fore.RED + "Could not find address."

def website_to_ip(website):
    try:
        return socket.gethostbyname(website)
    except socket.gaierror:
        return Fore.RED + "Could not resolve website."

def url_shortener(url):
    response = requests.get(f"https://tinyurl.com/api-create.php?url={url}")
    return response.text

def link_to_qr_code(link):
    qr = qrcode.make(link)
    qr.save("qrcode.png")
    return Fore.GREEN + "QR Code saved as qrcode.png"

def website_age(website):
    try:
        w = whois.whois(website)
        return str(w.creation_date)
    except Exception as e:
        return Fore.RED + str(e)

def phone_number_location(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        location = geocoder.description_for_number(parsed_number, "en")
        return Fore.GREEN + location
    except Exception as e:
        return Fore.RED + str(e)

def hash_generator(text, hash_type):
    if hash_type == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif hash_type == 'sha1':
        return hashlib.sha1(text.encode()).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(text.encode()).hexdigest()
    else:
        return Fore.RED + "Unsupported hash type."

def file_size(filename):
    try:
        size = os.path.getsize(filename)
        return f"{size} bytes"
    except FileNotFoundError:
        return Fore.RED + "File not found."

def current_time():
    return Fore.GREEN + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def currency_converter(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    rates = response.json().get("rates", {})
    if to_currency in rates:
        return Fore.GREEN + str(amount * rates[to_currency])
    return Fore.RED + "Currency not found."

def weather_info(city):
    api_key = 'your_api_key_here'  # Get your API key from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response["cod"] == 200:
        return Fore.GREEN + f"{response['weather'][0]['description'].capitalize()}, Temperature: {response['main']['temp']}°C"
    return Fore.RED + "City not found."

def random_password(length=12):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=3)
        return Fore.GREEN + "Internet is connected."
    except requests.ConnectionError:
        return Fore.RED + "No internet connection."

def get_public_ip():
    return Fore.GREEN + requests.get('https://api.ipify.org').text

def dns_lookup(domain):
    try:
        result = socket.gethostbyname(domain)
        return Fore.GREEN + f"IP address: {result}"
    except socket.gaierror:
        return Fore.RED + "Could not resolve domain."

def email_validator(email):
    import re
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return Fore.GREEN + "Valid Email" if re.match(regex, email) else Fore.RED + "Invalid Email"

def reverse_dns_lookup(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return Fore.GREEN + f"Domain: {result[0]}"
    except socket.herror:
        return Fore.RED + "Could not resolve IP."

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("speech.mp3")
    return Fore.GREEN + "Speech saved as speech.mp3"

def ip_geolocation(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    return Fore.GREEN + str(response.json())

def url_expander(short_url):
    response = requests.get(short_url)
    return Fore.GREEN + response.url

def main():
    while True:
        intro()
        choice = input(Fore.YELLOW + "Enter your choice (0 to exit): ")

        if choice == '1':
            ip = input(Fore.YELLOW + "Enter IP address: ")
            print(ip_to_address(ip))
        elif choice == '2':
            website = input(Fore.YELLOW + "Enter website URL: ")
            print(website_to_ip(website))
        elif choice == '3':
            url = input(Fore.YELLOW + "Enter URL to shorten: ")
            print(url_shortener(url))
        elif choice == '4':
            link = input(Fore.YELLOW + "Enter link for QR code: ")
            print(link_to_qr_code(link))
        elif choice == '5':
            website = input(Fore.YELLOW + "Enter website URL: ")
            print(website_age(website))
        elif choice == '6':
            phone_number = input(Fore.YELLOW + "Enter phone number: ")
            print(phone_number_location(phone_number))
        elif choice == '7':
            text = input(Fore.YELLOW + "Enter text to hash: ")
            hash_type = input(Fore.YELLOW + "Choose hash type (md5, sha1, sha256): ")
            print(hash_generator(text, hash_type))
        elif choice == '8':
            filename = input(Fore.YELLOW + "Enter filename: ")
            print(Fore.YELLOW + f"File size: {file_size(filename)}")
        elif choice == '9':
            print(Fore.YELLOW + f"Current time: {current_time()}")
        elif choice == '10':
            amount = float(input(Fore.YELLOW + "Enter amount: "))
            from_currency = input(Fore.YELLOW + "From currency (e.g., USD): ")
            to_currency = input(Fore.YELLOW + "To currency (e.g., EUR): ")
            print(currency_converter(amount, from_currency, to_currency))
        elif choice == '11':
            city = input(Fore.YELLOW + "Enter city name: ")
            print(weather_info(city))
        elif choice == '12':
            length = int(input(Fore.YELLOW + "Enter password length: "))
            print(Fore.YELLOW + f"Random Password: {random_password(length)}")
        elif choice == '13':
            print(check_internet())
        elif choice == '14':
            print(Fore.YELLOW + f"Public IP: {get_public_ip()}")
        elif choice == '15':
            domain = input(Fore.YELLOW + "Enter domain: ")
            print(dns_lookup(domain))
        elif choice == '16':
            email = input(Fore.YELLOW + "Enter email: ")
            print(email_validator(email))
        elif choice == '17':
            ip = input(Fore.YELLOW + "Enter IP address: ")
            print(reverse_dns_lookup(ip))
        elif choice == '18':
            text = input(Fore.YELLOW + "Enter text to convert to speech: ")
            print(text_to_speech(text))
        elif choice == '19':
            ip = input(Fore.YELLOW + "Enter IP address: ")
            print(ip_geolocation(ip))
        elif choice == '20':
            short_url = input(Fore.YELLOW + "Enter short URL: ")
            print(url_expander(short_url))
        elif choice == '0':
            print(Fore.RED + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

        # Ask if the user wants to use another tool
        again = input(Fore.YELLOW + "Would you like to use another tool? (yes/no): ").strip().lower()
        if again != 'yes':
            print(Fore.RED + "Exiting...")
            break

if __name__ == "__main__":
    main()
