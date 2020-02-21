# 目次
1. 基礎知識
2. DB設計
3. SQL

## 目標
DB設計タスクに共通する基本的な知識と技術を習得する。

# 1.基礎知識
## システムにおけるDBの立ち位置  
データの保管庫。複数のシステムで扱われるデータも統一的に管理。  
システム上では、データを処理するプログラムとは独立に扱われる。  
さらに、DBとシステムの他の要素の間にはDBMS(database management system)というデータを管理するためのインターフェースが存在し、実際のDBからのデータの入出力はDBMSが行っている。  
<br>

## RDBの構造  
データを2次元の表で管理。行をそれぞれのデータ、列をデータを構成する要素とする。  
表と表の間に関連性を持たせることが可能。  
<dl>
    <dt>・エンティティ</dt>
    <dd>データを格納する大きな単位。</dd>
    <dt>・属性</dt>
    <dd>エンティティ内に格納する具体的な情報。</dd>
    <dt>・リレーション</dt>
    <dd>エンティティ間を関連付ける情報。外部キーは必ず主キーを参照する。(後述)
    </dd>
</dl>
<br>

## 主キー、外部キー、正規形  
<dl>
    <dt>・主キー</dt>
    <dd>各テーブルに1つ存在。データ内容の重複がなく、それぞれのデータを区別するためのキー。複数の列をまとめて主キー扱いすることもある。</dd>
    <dt>・外部キー</dt>
    <dd>テーブル間を関連付けるためのキー。1to1, 1toM, MtoMの3種類がある。</dd>
    <dt>・正規形</dt>
    <dd>データがどれだけ管理しやすい形になっているか。</dd>
</dl>
<br>

## 各種制約(not null, unique)
<dl>
    <dt>・not null</dt>
    <dd>データの内容が空の状態で格納されるのを制限する。</dd>
    <dt>・unique</dt>
    <dd>データ間で内容の重複が起こるのを制限する。主キーには必ず付される。複数のキーをまとめてunique制約を課す場合もある。</dd>
</dl>
<br>

# 2.DB設計
## DB設計の手順
1. DBに格納する情報を洗い出す。(正規化されていない論理モデル)
2. 論理モデルの修正
    * 正規化：従属関係を排除して、エンティティをできる限り細かい単位に分ける。
3. 物理モデルの設計(どのDBを使うか、サーバーは何を使うか)
4. 物理モデルの作成

## ER図の書き方  
https://erdplus.com/  
<br>

## 注意すべき事  
* 管理する必要があるデータのみを含める
* 必要なデータは全てそろえる
* 正規化する
* 1to1で十分なリレーションを1toMやMtoMにしない。1toMで十分なリレーションをMtoMにしない。
* 認証情報は分離するのが望ましい
* MtoMは中間テーブルを作成
* logテーブルも必要なら作る
<br>

# 3.SQL
## RDBの種類  
代表的なOSSのみ紹介  
* SQLite
* MySQL
* PostgreSQL
* MariaDB

## postgresqlの設定  

    $sudo /etc/init.d/postgresql start
    $sudo passwd postgres  
    $su - postgres  
    $psql
    #CREATE ROLE {username} LOGIN CREATEDB PASSWORD {password}; 
    #CREATE DATABASE {dbname} OWNER {username};
    #\du
    #\q
    $loguot
    $psql --user {username} --dbname {dbname}

## SQL基本操作
詳細なリファレンスは  
https://www.postgresql.jp/document/10/html/index.html

### postgresql特有のコマンド
* `\q` : 終了
* `\du` : ロール一覧  
* `\l` : DB一覧  
* `\dt` : テーブル一覧

### データ定義
#### create table
新しいtableを作成。

    CREATE TABLE {table_name} (
        {first_column_name} text,
        {second_column_name} integer,
    );  

データ型リファレンス  
https://docs.microsoft.com/ja-jp/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver15  

・ オプション

    stock integer DEFAULT 10,
    price numeric CHECK (price > 0),
    product_name text NOT NULL,
    product_id integer UNIQUE,

    # PRIMARY KEY は主キーに与える。  
    # NOT NULL かつ UMIQUE を表す。 
    product_id integer PRIMARY KEY,

    # REFERENCES は外部キーに与える。  
    {foreign_key} integer REFERENCES {table_name},

#### drop table
指定したtableを削除。

    DROP TABLE {table_name};


#### tableの変更

    ALTER TABLE {table_name} ADD COLUMN {field_name} {data_type};

コマンドは他にもいろいろあるが時間の関係で割愛。
だが全て `ALTER TABLE {table_name} ACTION {…}` 構文で可能。


### データ操作
#### insert
tableに新たなデータを挿入する。

    INSERT INTO {table_name} VALUES {value};

`{value}` は `(1, 'student', 3.5)` のように与える。

#### update
table内に存在するデータの値を変更する。

    UPDATE {table_name} SET {column_name} = {value} WHERE {condition};

例えば、 `UPDATE products SET price = 10 WHERE id = 5;` は、`products`テーブル内で`id`が`5`であるデータの、`price`という列の値を`10`に変更すると言う意味。

#### delete
table内の条件に合致するデータを削除する。

    DELETE FROM {table_name} WHERE {condition};

`{table_name}`内の`{condition}`に合致するデータを全て削除。

#### select
table内の条件に合致するデータを取得する。

    SELECT {condition} FROM {table_name};

例えば、 `SELECT * FROM table1;` は`table1`内の全てのデータを取得。

