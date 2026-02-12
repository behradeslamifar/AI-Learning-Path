# venv
Built-in tools from version 3.3

## Install venv
- Check the version
```
python3 --version
```

- Install pip and venv module
```
sudo apt install python3-pip python3-venv
```

## Create virutal environment
```
python3 -m venv <venv_folder>
```

## Use venv
```
python3 -m venv .venv
source .env/bin/activate
pip install requests
```

to deactive
```
deactivate
```


## venv trick
- Use global package also
```
python3 -m venv venv --system-site-packages
```

- Clear the environment
```
python3 -m venv venv --clear
```

- keep dependencies list
```
pip freeze > requirements.txt
```

```
pip install -f requirements.txt
```

- If python updated
```
python3 -m venv venv --upgrade
```
