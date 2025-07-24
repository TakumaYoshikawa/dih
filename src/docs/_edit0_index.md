# 目次

[TOC]

# 1.はじめに
!!! indent ""
    Document In HTML(DIH)は、<br />
    あらゆるドキュメントをHTML形式にて生成することを目的とする。

# 2.基本構想
!!! indent ""
    本項にて基本構想を説明する。

    生成するドキュメントはHTML形式であるが、生成元たるファイルは用途ごとに以下のようになる。

    | 用途 | ファイル形式 | 数量 |
    | --- | --- | --- |
    | 本文 | MarkDown(.mdファイル) | 生成する1つのHTMLファイルに対して1つのみ。 |
    | 文章デザイン | CSS(.cssファイル) | 生成する1つのHTMLファイルに対して1つのみ。<br />または無し。 |
    | 画像 | PNG(.drawio.pngファイル)<br />SVG(.drawio.svgファイル) | 生成する1つのHTMLファイルに対して1つ以上。<br />または無し。 |

    本文はMarkDown形式で記述する(デザインや文章構造によってはHTMLタグを用いることもある)。<br />
    文章デザインはCSS形式で記述する。<br />
    画像の描画はPNG形式を用いるが、より高度な図を描画したい場合はSVG形式を用いることもある。

    これらのファイルを組み合わせて単一のHTMLファイルを生成する。<br />
    単一のHTMLファイルにするので、CSSファイルや画像ファイルはすべてHTMLファイルに埋め込む。<br />
    これにより、HTMLファイルのみでドキュメントを閲覧できるようになる。

    HTMLファイルの生成は専用の[変換スクリプト](#furoku-convert-script)を用いて行う。<br />
    以下にHTMLファイルの生成過程を図解する。<br />
    ![](./images/img.2.img-1.drawio.svg)<br />
    図: img.2.img-1

# 3.開発環境
!!! indent ""
    本項にて開発環境を説明する。

    **Python3** がインストールされていることが前提となる。<br />
    それ以外は特に指定をしない。

    推奨する開発環境は以下の通りである。

    - **OS:**
        - Windows 10 または Windows 11
    - **仮想化プラットフォーム:**
        - WSL2
    - **Pythonを実行する仮想化プラットフォーム上のOS:**
        - 任意のLinuxディストリビューション
    - **Python:**
        - 3.9 以上

# 4.チュートリアル
!!! indent ""
    本項にてチュートリアルを示す。

    ## 4.a.本文のみのHTMLファイルを生成する
    !!! indent ""
        本文のみのHTMLファイルを生成するチュートリアルである。

        ### 4.a.1.変換スクリプトのインストール
        !!! indent ""
            [md2html.py](#furoku-convert-script-this)を任意の作業ディレクトリに配置する。<br />
            [必要な外部ライブラリ](#furoku-convert-script-require-lib)をインストールする。

        ### 4.a.2.本文たるMarkdownファイルの作成
        !!! indent ""
            以下のMarkdownファイルを作成する。

            `example.md`

                # チュートリアル
                これはチュートリアルです。

        ### 4.a.3.変換処理の実行
        !!! indent ""
            スクリプトを用いてHTMLファイルを生成する。

                $ python3 md2html.py --src-md-path example.md --dist-html-path example.html
            
            これにて**example.html**が生成される。
    
    ## 4.b.文章デザインを適用したHTMLファイルを生成する
    !!! indent ""
        文章デザインを適用したHTMLファイルを生成するチュートリアルである。

        ### 4.b.1.変換スクリプトのインストール
        !!! indent ""
            [md2html.py](#furoku-convert-script-this)を任意の作業ディレクトリに配置する。<br />
            [必要な外部ライブラリ](#furoku-convert-script-require-lib)をインストールする。

        ### 4.b.2.本文たるMarkdownファイルの作成
        !!! indent ""
            以下のMarkdownファイルを作成する。

            `example.md`

                # チュートリアル
                これはチュートリアルです。

        ### 4.b.3.文章デザインたるCSSファイルの作成
        !!! indent ""
            以下のCSSファイルを作成する。

            `example.css`

                h1 {
                    background-color: #64cadcff;
                    padding: 6px 2px;
                }

        ### 4.b.4.変換処理の実行
        !!! indent ""
            スクリプトを用いてHTMLファイルを生成する。

                $ python3 md2html.py --src-md-path example.md --src-css-path example.css --dist-html-path example.html
            
            これにて文章デザインを適用が適用された**example.html**が生成される。<br />
            また、CSSファイルのデータがHTMLファイルに埋め込まれている。

    ## 4.c.画像を埋め込んだHTMLファイルを生成する
    !!! indent ""
        画像を埋め込んだHTMLファイルを生成するチュートリアルである。

        ### 4.c.1.変換スクリプトのインストール
        !!! indent ""
            [md2html.py](#furoku-convert-script-this)を任意の作業ディレクトリに配置する。<br />
            [必要な外部ライブラリ](#furoku-convert-script-require-lib)をインストールする。

        ### 4.c.2.本文たるMarkdownファイルの作成
        !!! indent ""
            以下のMarkdownファイルを作成する。

            `example.md`

                # チュートリアル
                これはチュートリアルです。

                ![画像](./images/img.1.img-1.drawio.png)
            
            Markdownの記法にて画像を埋め込む記述する。

        ### 4.c.3.画像ファイルの配置
        !!! indent ""
            以下の画像ファイルを配置する。<br />

            - `./images/img.1.img-1.drawio.png`

            画像ファイルの作成・編集はdraw.ioのツールを用いて行うものとする。

        ### 4.c.4.変換処理の実行
        !!! indent ""
            スクリプトを用いてHTMLファイルを生成する。

                $ python3 md2html.py --src-md-path example.md --dist-html-path example.html
            
            これにて画像が埋め込まれた**example.html**が生成される。<br />
            また、画像ファイルのデータがHTMLファイルに埋め込まれている。

# 5.より高度な使い方
!!! indent ""
    本項にてより高度な使い方について説明する。

    ## 5.a.インデント
    !!! indent ""
        本文中にインデントを用いることができる。<br />
        インデントは[Python-MarkdwonのAdmonition拡張機能](https://python-markdown.github.io/extensions/admonition/)を用いる。<br />
        
        ### 5.a.1.CSSファイルの記述
        !!! indent ""
            インデントのスタイルを記述するためのCSSファイルに以下の記述をする。

            `example.css`

                .indent {
                    padding-left: 20px;　/* これにより右に字下げ */
                    border-left: 1px solid #eeeeee;　/* 左側の線 */
                }
        
        ### 5.a.2.本文へのインデントの記述
        !!! indent ""
            本文中でインデントを用いる際は以下のように記述する。

            `example.md`

                # インデント
                !!! indent ""
                    ここにインデントする文章を記述する。
                
                この文章はインデントされない。

            これにてインデントされた文章が生成される。

# 付録 <a id="furoku"></a>
!!! indent ""
    ## 変換スクリプト <a id="furoku-convert-script"></a>
    !!! indent ""
        ### スクリプト本文
        !!! indent ""
            [https://github.com/TakumaYoshikawa/dih/blob/master/src/docs/md2html.py](https://github.com/TakumaYoshikawa/dih/blob/master/src/docs/md2html.py)

        ### スクリプト起動方法
        !!! indent ""
            スクリプトは以下のようにして起動する。

                $ python3 md2html.py --src-md-path _edit0_index.md --src-css-path edit0.css --dist-html-path index.html

            #### コマンドライン引数説明
            !!! indent ""
                | 引数名 | 必須 | 説明 |
                | --- | --- | --- |
                | --src-md-path | ○ | 変換元のMarkdownファイルのパス |
                | --src-css-path | - | 変換元のCSSファイルのパス |
                | --dist-html-path | ○ | 変換先のHTMLファイルのパス |
        
        ### 必要な外部ライブラリ <a id="furoku-convert-script-require-lib"></a>
        !!! indent ""
            スクリプトは以下の外部ライブラリを使用する。

            - [Python-Markdown](https://python-markdown.github.io/)
        
        ### 拡張機能カススタイズ
        !!! indent ""
            [スクリプト本文中](#furoku-convert-script-this)の**# 拡張機能を有効化**の部分にて拡張機能のカスタマイズを行うことができる。<br />
            カスタマイズにあたっては[Python-Markdown公式ドキュメント](https://python-markdown.github.io/extensions/)を参照すること。

    ## 生成元ファイルのサンプル
    !!! indent ""
        本ドキュメントの生成元たるファイルの一式は[ここ](https://github.com/TakumaYoshikawa/dih/tree/master/src/docs)。
