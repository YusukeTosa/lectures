# Intro
このリポジトリは、初心者向けのデータベースとスクレイピングの勉強資料を収録しています。\
(202210追記)Stable Diffusionの非機械学習エンジニア向け解説資料を追加しました。

## myenv
本リポジトリに収録されているコードは、以下の環境でテスト済みです。  

Python 3.6  
Ubuntu 18.04

# Setup
以下のパッケージが使用可能なPCを用意してください。  
* python3
* pip3  
* postgresql

postgresqlのインストールは以下のコマンドで可能です。
## for linux

    sudo apt install postgresql

## for mac

    brew install postgresql

次に、以下のコマンドに従って環境設定を行ってください。

## for linux
    git clone https://github.com/YusukeTosa/lectures.git
    cd lectures
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    ipython kernel install --user --name=.venv

## for mac
    git clone https://github.com/YusukeTosa/lectures.git
    cd lectures
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    ipython kernel install --user --name=.venv

