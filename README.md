# Literaki

Todo Krzycha:
- Sprawdzic kod, ktory nie jest uzywany i go albo wyrzucic, albo zrefaktorowac tak, by byl uzywany w nowym konstrukcie pair_game
    - Player nie jest używany
    - część kodu z PlayerManager też nie jest używane. PlayerManager powinien zmienic nazwę na lobby, czy jakoś tak
    - GamePlusMinus nie jest wcale używane, ale można zrefaktorować to z kodem z pair_game


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

- Lobby to poczekalnia, gdzie parujemy graczy