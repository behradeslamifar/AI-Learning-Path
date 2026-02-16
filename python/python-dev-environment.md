## Manage Multipe Version of Python with pyenv
Install and manage multipe version of python

### Install
```
sudo apt update
sudo apt install -y build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

```
curl https://pyenv.run | bash
```

.bashrc
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

### How to use pyenv
```
pyenv install 3.10.14
pyenv install 3.11.8
```

```
pyenv install --list
```

## Clean environment with venv
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
