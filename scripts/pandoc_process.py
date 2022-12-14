#!/usr/bin/env python
# coding: utf-8

import re
import frontmatter

from datetime import datetime
from pathlib import Path

import utils



re_span = re.compile('<span.+</span>')
re_md_links = re.compile(r'(\[.+?\]\(http.+?\))')
re_img = re.compile(r'<img .+?/>')
re_underline = re.compile('<u>(.+?)</u>')
re_style = re.compile('style=".+?"')
re_scr = re.compile('src="(.+?)"')


figure_template = """
<figure>
{img}
<figcaption></figcaption>
</figure>
""".strip()


def clean_title(title):
    title = re_span.sub('', title)  
    title = title.replace('\<', '<')
    title = title.replace('\>', '>')
    return title


def create_post_id(title):
    title = utils.slugify_title(title)
    today = datetime.today().strftime('%Y-%m-%d')
    post_id = f'{today}-{title}'
    return post_id

def prepare_content(post_id, content):
    
    content, _ = re_md_links.subn(r'\1{:target="_blank"}', content)

    def replace_path(m):
        src = m.group(1)
        name = Path(src).parts[-1]
        path = f'/images/posts/{post_id}/{name}'
        return f'src="{path}"'

    def replace_image(m):
        img = m.group(0)
        img = re_style.sub('', img)
        img = re_scr.sub(replace_path, img)
        return figure_template.format(img=img)

    result = []

    for line in content.split('\n'):
        line = line.replace('\u200a', ' ')
        if '<u>' in line:
            line = re_underline.sub(r'\1', line)
        if '<img' in line:
            line = re_img.sub(replace_image, line)
        if line.startswith('#'):
            line = '#' + line
        
        result.append(line)

    return '\n'.join(result)


def load_and_process(document_path, author, tags):
    post = frontmatter.load(document_path)

    post['title'] = clean_title(post['title'])
    post['subtitle'] = clean_title(post['subtitle'])

    post_id = create_post_id(post['title'])
    post.content = prepare_content(post_id, post.content)

    post['layout'] = 'post'
    post['description'] = post['subtitle']
    post['image'] = f'images/posts/{post_id}/cover.jpg'
    post['authors'] = [author]
    post['tags'] = tags

    post_path = Path(f'_posts/{post_id}.md')

    with post_path.open('wb') as f_out:
        frontmatter.dump(post, f_out)

    return post_id
