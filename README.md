# Literaki

## Instalacja

### Backend

- Backend napisany jest w Pythonie, dlatego wymaga zainstaowanego interpretera w wersji przynajmniej `3.7`. Interpreter można pobrać stąd: https://www.python.org/downloads/
- Dodatkowo, potrzebujemy zainstalowanej biblioteki `websockets`:
```
pip install websockets
```

### Frontend
- todo


## Uruhomienie
- **Backend (serwer)** - serwer uruchomimy komendą
```
python run.py 
```
- **Frontend (klient)** - klienta uruchomimy komendą: 
```
todo
```



## Ważne info do backendu w pythonie:
- Każdą funkcję, która ma w definicji `async` trzeba wywoływać se słówkiem kluczowym `await`
- Każda funkcja, która używa innej funkcji z `await`, musi mieć prefix w definicji `async`