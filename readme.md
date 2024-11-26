# Requirements

pip install -r requirements.txt

# Modify UI Design

```
pyside6-designer
```

# Generate UI Python Code

## Windows
```
uic.cmd
```

## Mac OS X
```
uic.sh
```

# Generate Resource

```
pyside6-rcc icons.qrc -o icons_rc.py
pyside6-rcc csv_rc.qrc -o csv_rc.py
```

# Run

```
python mainwindow.py
```

# Deploy

## Windows

```
pyinstaller mainwindow.py --onefile --noconsole --icon=hexagram.ico
```

## Mac OS X

```
pyinstaller mainwindow.py --onefile --noconsole
```
