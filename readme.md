# Requirements

# Modify UI Design

```
pyside6-designer
```

# Generate UI Python Code

```
pyside6-uic mainwindow.ui -o ui_mainwindow.py
pyside6-uic page_NaJia.ui -o ui_page_NaJia.py
pyside6-uic page_NaZi.ui -o ui_page_NaZi.py
pyside6-uic page.ui -o ui_page.py
pyside6-uic output.ui -o ui_output.py
pyside6-uic feiteng_linggui_display.ui -o ui_feiteng_linggui_display.py
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