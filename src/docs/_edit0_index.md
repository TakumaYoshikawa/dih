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

# 付録 <a id="furoku">
!!! indent ""
    ## 変換スクリプト <a id="furoku-convert-script">
    !!! indent ""
        ### スクリプト本文 <a id="furoku-convert-script-this">
        !!! indent ""
            `md2html.py`

                import sys
                import os
                import base64
                import urllib.parse
                import argparse

                import markdown


                class MainFlow():
                    def __init__(self):
                        parser = argparse.ArgumentParser(description="Markdown to HTML converter")
                        parser.add_argument("--src-md-path", type=str, help="Path to the source Markdown file")
                        parser.add_argument("--src-css-path", type=str, help="Path to the CSS file")
                        parser.add_argument("--dist-html-path", type=str, help="Path to the destination HTML file")

                        self.args = parser.parse_args()
                        self._argsCheck()

                    def _argsCheck(self):
                        if not self.args.src_md_path:
                            raise ValueError('The source Markdown file path is required "--src-md-path"')
                        if not self.args.dist_html_path:
                            raise ValueError('The destination HTML file path is required "--dist-html-path"')

                    def ReadMarkdown(self):
                        with open(self.args.src_md_path, 'r', encoding='utf-8') as file:
                            return file.read()

                    def Convert(self, markdown_content):
                        # 画像のインライン化関数
                        def _inlineImage(src):
                            image_path = os.path.join(os.path.dirname(self.args.src_md_path), src)
                            ext = os.path.splitext(image_path)[1].lower()
                            mime_type = ''

                            if ext == '.svg':
                                mime_type = 'image/svg+xml'
                            elif ext == '.png':
                                mime_type = 'image/png'
                            elif ext in ['.jpg', '.jpeg']:
                                mime_type = 'image/jpeg'
                            elif ext == '.gif':
                                mime_type = 'image/gif'
                            else:
                                raise ValueError(f'Unsupported image type: {ext}')

                            with open(image_path, 'rb') as image_file:
                                image_data = image_file.read()

                            if mime_type == 'image/svg+xml':
                            # SVG データを URL エンコードする
                                return f'data:{mime_type},{urllib.parse.quote(image_data.decode("utf-8"))}'
                            else:
                                # 他の画像データを base64 エンコードする
                                return f'data:{mime_type};base64,{base64.b64encode(image_data).decode("utf-8")}'

                        # カスタム Markdown パーサー
                        class InlineImageMarkdownRenderer(markdown.treeprocessors.Treeprocessor):
                            def run(self, root):
                                for element in root.iter('img'):
                                    src = element.get('src')
                                    inline_src = _inlineImage(src)
                                    element.set('src', inline_src)
                                return root

                        class InlineImageExtension(markdown.extensions.Extension):
                            def extendMarkdown(self, md):
                                md.treeprocessors.register(InlineImageMarkdownRenderer(md), 'inline_image', 15)

                        # HTML 変換
                        md = markdown.Markdown(
                            # 拡張機能を有効化
                            extensions=[
                                InlineImageExtension(), # 画像のインライン化(自作拡張機能)
                                'tables', # テーブル
                                'footnotes', # 脚注
                                'toc', # 目次
                                'admonition', # 注意書き(<div>タグ)
                                'codehilite', # シンタックスハイライト
                            ]
                        )
                        html_content = md.convert(markdown_content)

                        return html_content
                    
                    def AddCSS(self, html_content):
                        if not self.args.src_css_path:
                            return html_content
                        else:
                            with open(self.args.src_css_path, 'r') as f:
                                css_data = f.read()
                                return f'<style>{css_data}</style>' + html_content

                    def WriteHTML(self, html_content):
                        with open(self.args.dist_html_path, 'w', encoding='utf-8') as file:
                            file.write(html_content)
                        print(f'HTML file generated: {self.args.dist_html_path}')

                def main():
                    mian_flow = MainFlow()
                    markdown_content = mian_flow.ReadMarkdown()
                    html_content = mian_flow.Convert(markdown_content)
                    html_content_with_css = mian_flow.AddCSS(html_content)
                    mian_flow.WriteHTML(html_content_with_css)


                if __name__ == '__main__':
                    main()

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
        
        ### 必要な外部ライブラリ <a id="furoku-convert-script-require-lib">
        !!! indent ""
            スクリプトは以下の外部ライブラリを使用する。

            - [Python-Markdown](https://python-markdown.github.io/)
        
        ### 拡張機能カススタイズ
        !!! indent ""
            [スクリプト本文中](#furoku-convert-script-this)の**# 拡張機能を有効化**の部分にて拡張機能のカスタマイズを行うことができる。<br />
            カスタマイズにあたっては[Python-Markdown公式ドキュメント](https://python-markdown.github.io/extensions/)を参照すること。

    ## 生成元ファイルのサンプル
    !!! indent ""
        本ドキュメントの生成元たるファイルの一式は[此処](https://github.com/TakumaYoshikawa/dih/tree/master/src/docs)にあり。