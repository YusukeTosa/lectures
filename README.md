# Intro
このリポジトリは、初心者向けのデータベースとスクレイピングの勉強資料を収録しています。

# Setup
## myenv
本リポジトリに収録されているコードは、以下の環境でテスト済みです。  

Python 3.6  
Ubuntu 18.04

以下のパッケージが使用可能なPCを用意してください。  
* python3
* pip3  
* postgresql

インストールは以下のコマンドで可能です。
## for linux

    sudo apt install python3.6 python3-pip postgresql

## for mac

    brew install python3.6 postgresql

次に以下のコマンドに従って環境設定を行ってください。

## for linux
    git clone https://github.com/YusukeTosa/lectures.git
    cd lecture
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    ipython kernel install --user --name=.venv


