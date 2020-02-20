# 目次
1. 基礎知識
2. Pythonによるクローリング・スクレイピング入門
3. 実用
4. Scrapyの紹介
5. クローラーの継続運用

## 目標
* 1回生は3まで  
    1, 2は基礎知識として抑えて欲しい。普段の業務にも活きてくると思います。3は軽く読み流す程度でいいです。必要になったら見返してください。
* 2回生は5まで  
    1, 2は基本的な話なので一読すればＯＫです。3, 5は実用的な話を多く含むので重要度は比較的高いです。4は純粋にフレームワークの勉強になるので、短時間で修得するのは骨が折れると思います。必要になったらやるくらいでいいかと。


# １：基礎知識
<dl>
  <dt>・クローリング</dt>
  <dd>Webページのハイパーリンクをたどって次々にWebページをダウンロードする作業。</dd>
  <dt>・スクレイピング</dt>
  <dd>ダウンロードしたWebページから必要な情報を抜き出す作業。</dd>
</dl>  

## Unixコマンドによる例

### クローリング
Webページをダウンロードするためのコマンド。  

    wget <url> [-O <保存するファイル名>]

標準出力に出力
    
    wget <url> -q -O -

再帰的にリンクをたどる

    wget -r --no-parent -w 1 -l 1 <url>

### スクレイピング
grepや正規表現など。割愛。

## 知っておくべき概念 
* urlの構造
* サーバーとクライアント
* リクエストとレスポンス
* Webサイトの構成
* HTTPヘッダーとボディ  
* エンコーディング  
* ファイルの種類  
    * html
    * xml
    * zip  
など…  
* 保存方式
    * txt
    * csv, tsv
    * json  
など…


# ２：Pythonによるクローリング・スクレイピング入門
前述のUnixコマンドでもWebページのデータは処理できるが、複雑な処理には向かない。  
Pythonには簡単な記述でスクレイピング・クローリングできるライブラリがいくつもある。  
本資料では、RequestsとBeautifulSoupを用いた基本的なクローリング・スクレイピングの流れを紹介。

    pip install requests beautifulsoup4

## クローリング・スクレイピングの基本的な流れ
1. クローラーがファイルをダウンロード(クローリング)
2. ファイルを処理(スクレイピング)
3. データを保存

## この章の構成
1. requestsの基礎
2. beautifulsoupの基礎
3. データをDBに保存
4. クローラーの作成

# ３：実用
* ファイルの種類によって処理が変わる
* 自然言語処理
* APIの利用
* javascriptの解釈&ブラウザの自動操作

# ４：Scrapyの紹介


# ５：クローラーの継続運用