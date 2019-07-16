"# study-python"

<!-- 2019/07/16 k.konishi create -->

「py27env」について
・環境は"python2.7"
・python の「仮想環境」として作成
　 →「~\study-python」で「py -2 -m virtualenv py27env」を実行すれば同環境を構築可
Ex:
C:\Project\study-python>py -2 -m virtualenv py27env

注意:
オプションの「-2」は「同環境に python3.x 系が共存している場合」のみ必要。
端末内に 2 系しかインストールしていなければコマンドオプションは不要

==========
「py37env」について
・環境は"python3.7"
・python の「仮想環境」として作成
　 →「~\study-python」で「py -3 -m virtualenv py37env」を実行すれば同環境を構築可
Ex:
C:\Project\study-python>py -3 -m virtualenv py37env

注意:
オプションの「-3」は「同環境に python3.x 系が共存している場合」のみ必要。
端末内に 3 系しかインストールしていなければコマンドオプションは不要

【注意:仮想環境構築時のコマンドオプション「-2(-3)」について】
https://www.python.jp/install/windows/virtualenv.html
