# Requirements

## General

```
pip install -r requirements.txt
```

## On macOS

### Install HomeBrew

```
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```

### Install Python

```
brew install python@3.10
```

### Install & Use virtualenv

```
brew install virtualenv
virtualenv --version
cd <your-project>
virtualenv <your-env>
virtualenv -p /usr/local/bin/python3.10 <your-env>
source <your-env>/bin/activate
pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```

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

## Use pyside6-deploy (Recommended)

```
pyside6-deploy mainwindow.py
```

## Windows

```
pyinstaller mainwindow.py --onefile --noconsole --icon=hexagram.ico
```

## Mac OS X

```
pyinstaller mainwindow.py --onefile --noconsole
```
