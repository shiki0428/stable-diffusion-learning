# stable-diffusion-learning

macOS 使用

# １日目
## python 環境構築
```
pyenv install 3.10.3
pyenv global 3.10.3
python -V

python -m venv venv
source venv/bin/activvate
pip install -r requirement.txt
```

## Hugging Face
https://huggingface.co/models?language=ja&p=2&sort=downloads

アクセストークンをhuggingfaceから取得
一行目の実行は　~/.git-credentialsに認証の情報を保存できるらしい
gitにアクセスする時に公開鍵認証じゃなくてHTTPSで認証を行なっている人は
毎回password入力しないで済みそう（今の状態だと平文で保存されるから怖い・暗号化する設定もちゃんとある）

二行目でアクセストークン入力
```
git config --global credential.helper
huggingface-cli login
```

## 一旦実行
```
python pokemon_diffusers.py
```
実行で何かしら画像生成までできればオッケー  
deviceをmps使っているためここは適宜変更  
初回はモデルのインストールしているようで実行に時間がかかる。

# 二日目

# やること
- huggingface のチュートリアルを進めつつ裏側でポケモンAPIからポケモンの名前取得して
　呪文(prompt)に入力し実行結果を見る。（遊び）


## 下調べ
https://pokeapi.co/docs/v2
ドキュメントはあった。
poke_apitest.pyでレスポンスも確認

pokeapi
で全体取得する時に
https://pokeapi.co/api/v2/pokemon/ を実行したら20件しか表示されなくて
ページネーションがしっかり行われていた。（LIMIT/OFFSET 型）
次の二十件が必要な場合はレスポンス内のnextというパラメータにURLにリクエストしたら次の20件が取れるようになっている。

確かにポケモンも千を越えるとgetのパフォーマンスも落ちそう。
LIMIT/OFFSET 型の実装わかりやすくて参考になった。

limit に最大数入力したら全取得できる

流れとしては
- 全体取得
- ループ回して　url 取得
- 名前を取得

そもそも全体取得がいらない...

毎回したくないので csvに結果は保存する。

```
python get_pokemon_name_list.py
```
結構時間かかる

csvから名前取得してdiffuser実行
```
python pokemon_diffusers_by_csv.py 
```