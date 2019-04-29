# Literaki

## Rozgrywka
Literaki to dwu-osobowa gra, która polega na zgadywaniu przysłowia z wylosowanej kategorii.
Pierwsza osoba, która otworzy grę musi poczekać na dołączenie drugiego gracza. W zależności od postępów dostaje odpowiednie komunikaty:

![obraz](https://user-images.githubusercontent.com/28162772/56924590-8e50a300-6acd-11e9-8d9f-f1efe180e8bf.png)

Gdy dwóch graczy pomyślnie połączy się ze sobą, to tworzona jest między nimi nowa rozgrywka:

![obraz](https://user-images.githubusercontent.com/28162772/56923641-5cd6d800-6acb-11e9-9a90-0a8328509391.png)

Na górze strony mamy belkę z dwiema informacjami - aktualnie rozgrywającą osoba i wylosowaną kategorią. Na środku strony mamy zakryte litery hasła, które w trakcie zgadywania będą systematycznie odsłaniane.

Na dole znajduje się belka z miejscem do wysyłania literek do przysłowia, informację o aktualnej rundzie oraz pole do wysyłania wiadomości do naszego rywala. 
Każdy gracz może od razu odgadnąć hasło, wpisując całe przysłowie zamiast pojedynczego znaku.
Gdy hasło zostanie zgadnięte to każdy gracz dostaję o tym informację.

![obraz](https://user-images.githubusercontent.com/28162772/56924810-1afb6100-6ace-11e9-9b18-fefaeca6c30c.png)

Dodatkowym udogodnieniem pozwalającym na komunikację między uczestnikami gry jest chat. 
Po wysłaniu naszej wiadomości do drugiego gracza, jest ona wyświetlana w polu po prawej stronie wraz z informacją o nadawcy i czasem wysłania.

![obraz](https://user-images.githubusercontent.com/28162772/56925246-2d29cf00-6acf-11e9-97f4-71bbdc34f7ff.png)

## Instalacja

### Backend

- Backend napisany jest w Pythonie, dlatego wymaga zainstaowanego interpretera w wersji przynajmniej `3.7`. Interpreter można pobrać stąd: https://www.python.org/downloads/
- Dodatkowo, potrzebujemy zainstalowanej biblioteki `websockets`. Zainstalujemy ją komendą:
```
pip install websockets
```

### Frontend
- Frontend napisany został w React.js. Wymagany jest zaintalowany serwer node.js wraz z npm: https://nodejs.org/en/download/. Dodatkowo musimy mieć zainstalowanego w systemie `yarna`: https://yarnpkg.com/
- Aby zainstalować wszystkie zależności, przechodzimy do katalogu `frontend` i wykonujemy komendę `yarn install`:
 
 ```
 cd frontend
 yarn install
 ```

## Uruchomienie
- **Backend (serwer)** - serwer uruchomimy komendą
```
python run.py 
```

- **Frontend (klient)** - aby uruchomić klienta, przechodzimy do folderu `frontend` i wykonujemy polecenie `yarn start`: 
```
cd frontend
yarn start
```

- Istnieje możliwość uruchomienia całości jedną komendą. Na windowsie będzie to:
```
run.bat
```
