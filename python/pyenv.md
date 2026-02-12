# pyenv
Install and manage multipe version of python

## Install
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

## How to use pyenv
```
pyenv install 3.10.14
pyenv install 3.11.8
```

```
pyenv install --list
```
