# mioti-platforms-j3-sls

## Instalar AWS Cli en Windows
```
https://github.com/aws/aws-sam-cli/releases/latest/download/AWS_SAM_CLI_64_PY3.msi
```

## Instalar AWS Cli en Ubuntu
```
sudo apt-get update
sudo apt install awscli
aws configure
```

## Instalar NPM, Node and Serverless en Windows
```
https://nodejs.org/dist/v16.18.1/node-v16.18.1-x64.msi
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

## IOT project

### Install dependencies

```
cd iot-backend
pip3 install --platform manylinux2014_x86_64 --target=src/vendor --implementation cp --python 3.8 --only-binary=:all: -r requirements.txt
```

## Instalar WSL2 (Ubuntu 20.04)

```
wsl --install -d Ubuntu-20.04
```