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
            # 拡張機能を有効化(https://python-markdown.github.io/extensions/)
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
