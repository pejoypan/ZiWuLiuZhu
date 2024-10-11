# Requirements

# Modify UI Design

```
pyside6-designer
```

# Generate UI Python Code

```
pyside6-uic mainwindow.ui -o ui_mainwindow.py
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

```
pyinstaller mainwindow.py --onefile --noconsole --icon=hexagram.ico
```