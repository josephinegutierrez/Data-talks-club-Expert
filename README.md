## DataTalks.Club Website

### Running Jekyll locally
Use ruby 2.7.0:

```
rvm use ruby-2.7.0

gem install bundler
```

Running it for the first fime:

```
bundle install
```

Running Jekyll:

```
bundle exec jekyll serve
```

Open [http://localhost:4000](http://localhost:4000)


### Generating a cover image

Build the docker image for the cover generator:

```bash
cd previews
docker build -t datatalks-cover-generator .
cd ..
```

Now let's generate the image:

* the article: `_posts/2020-12-07-practical-guide-better-code.md`
* the output file: `images/posts/2020-12-07-practical-guide-better-code/cover.jpg`

```bash
POST="2020-12-23-slack-communities"
docker run -it \
    -v $(pwd)/_posts:/app/_posts \
    -v $(pwd)/_people:/app/_people \
    -v $(pwd)/images:/app/images \
    -u $(id -u ${USER}):$(id -g ${USER}) \
    datatalks-cover-generator \
    _posts/${POST}.md \
    images/posts/${POST}/cover.jpg
```

Test

```bash
cd previews
BOOK=20210125-mastering-ml-algorithms-2ed
node render_book.js \
    ../_books/${BOOK}.md \
    ../images/books/${BOOK}/preview.jpg
```