
# # # # # # # # # # # my_library # # # # # # # # # # # 

my_library to biblioteka zawierająca bardzo prosty zestaw funkcji do przetwarzania tekstu, oraz do operacji matematycznych. 

# Zawiera funkcje 
    # konwersji tekstu na wielkie i małe litery
    # sprawdzające czy string jest w liście
    # funkcje liczenia wyrazów i znaków w stringu
    # funkcje odwrócenia stringu
    # sprawdzenia czy liczba jest pierwsza oraz czy jest pozytywna

# Instalacja 
Aby zainstalować bibliotekę:
    trzeba sklonować repozytorium poleceniem 
    'git clone https://github.com/kingslayer335/python-intro.git'
    wejsc do katalogu 'cd python-intro'
    wpisac 'pip install -e .'
    można też po prostu skopiować pliki do swojego projektu i zaimportować odpowiednie moduły

# Przykłady wywołań funkcji 

## data_utils.py
```python
from data_utils import convert_to_uppercase, convert_to_lowercase, is_on_list
print(convert_to_uppercase("hello"))  # HELLO
print(convert_to_lowercase("HELLO"))  # hello
print(is_on_list([1, 2, 3], 2))  # True
```
## math_tools.py
```python
from math_tools import is_number_prime, is_number_positive
print(is_number_prime(7))  # True
print(is_number_positive(-5))  # False
```
## text_processing.py
```python
from text_processing import count_words, count_characters, reverse_text
print(count_words("Hello world!"))  # 2
print(count_characters("Hello"))  # 5
print(reverse_text("abc"))  # "cba"
```
## Testy 
Testy dla każdej funkcji znajdują się w katalogu `zadanie_3/tests`. Aby uruchomić testy, użyj:

```
'python -m unittest discover tests'
```
Testy są przeprowadzane przez każdą komendę push/pull, można je znaleźć na githubie w 'Actions'

## .gitignore 
Umieszczony tam został folder __pycache__

## black 
Narzędzie black zostało użyte do formatowania

## Licencja 
MIT License

## Autor 
Piotr Artym, 122212

## Wersja 
1.0.0

