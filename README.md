# Literaki

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
