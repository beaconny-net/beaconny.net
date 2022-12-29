import json
import os

from lib.htmlephant import Document
from templates import (
    index,
    page,
    post as post_tmpl,
)


OUTPUT_PATH = ".."


get_output_path = lambda filename: os.path.join(OUTPUT_PATH, filename)


def render_doc(context, page_type, body_els=(), head_els=()):
    return "".join(
        Document(
            body_els=(
                *page.Body(context, page_type=page_type),
                *body_els
            ),
            head_els=(*page.Head(context), *head_els)
        )
    ).encode("utf-8")


def main():
    context = json.load(open("context.json", "rb"))

    # Normalize base_path.
    base_path = context["site"]["base_path"].rstrip("/")
    if not base_path.startswith("/"):
        base_path = f"/{base_path}"
    context["site"]["base_path"] = base_path

    # Generate index.html
    index_output_path = get_output_path("index.html")
    with open(index_output_path, "wb") as index_fh:
        index_fh.write(
            render_doc(
                context=context,
                page_type="index",
                body_els=index.Body(context),
                head_els=index.Head(context),
            )
        )
        print(f"Wrote: {index_output_path}")

    # Generate an HTML file for each post.
    for post in context["posts"]:
        author = context["authors"][post["author"]]
        post_output_path = get_output_path(f"{post['slug'].lstrip('/')}.html")
        with open(post_output_path, "wb") as fh:
            fh.write(
                render_doc(
                    context=context,
                    page_type="post",
                    body_els=post_tmpl.Body(context, post=post, author=author),
                    head_els=post_tmpl.Head(context, post=post),
                )
            )
            print(f"Wrote: {post_output_path}")


if __name__ == "__main__":
    main()
