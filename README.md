# mioti-platforms-j3-sls

## Instalar WSL2 (Ubuntu 20.04)

```
wsl --install -d Ubuntu-20.04
```

## Instalar AWS Cli
```
sudo apt-get update
sudo apt install awscli
aws configure
```

## Instalar NPM, Node and Serverless en Ubuntu
```
sudo apt-get update
sudo apt-get install curl
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm  bash_completion  
nvm install --lts
npm install -g serverless
```

## Crear primer proyecto serverless e installar serverless offline
```
serverless
// Select aws-python-http-api-project
// Select NO to dashboard
// Select NO to deploy
cd aws-python-http-api-project
npm install serverless-offline --save-dev
```

// Añadir esto al final de serverless.yml
```
plugins:
  - serverless-offline
```

serverless offline

## IOT project

### Abrir VSCode la ruta 
\\wsl$\Ubuntu-20.04\home\

### Install dependencies

```
cd iot-backend
pip3 install --platform manylinux2014_x86_64 --target=/src/vendor --implementation cp --python 3.8 --only-binary=:all: -r requirements.txt
```