import json
import os

from lib.htmlephant import Document
from templates import (
    drafts,
    index,
    page,
    post as post_tmpl,
)


OUTPUT_PATH = ".."


get_output_path = lambda filename: os.path.join(OUTPUT_PATH, filename)


def render_doc(context, page_name, body_els=(), head_els=()):
    return "".join(
        Document(
            body_els=(
                *page.Body(context, page_name=page_name),
                *body_els
            ),
            head_els=(*page.Head(context), *head_els)
        )
    ).encode("utf-8")


class Context(dict):
    """Class to normalize and provide context-aware helper functions for
    context data."""
    def __init__(self, data):
        super().__init__(data)
        self.normalize()

    def normalize(self):
        # Ensure that paths have a "/" at the beginning but not at the end.
        for k in ("base_path", "css_path", "images_path", "posts_path"):
            path = self["site"][k].strip().rstrip("/")
            if not path.startswith("/"):
                path = f"/{path}"
            self["site"][k] = "" if path == "/" else path

    def css_url(self, filename):
        """Return a absolute CSS file path."""
        return f"{self['site']['base_path']}{self['site']['css_path']}/{filename}"

    def image_url(self, filename):
        """Return a absolute image file path."""
        return f"{self['site']['base_path']}{self['site']['images_path']}/{filename}"

    def post_url(self, slug):
        """Return a absolute post file path."""
        return f"{self['site']['base_path']}{self['site']['posts_path']}/{slug}"


def main():
    context = Context(json.load(open("context.json", "rb")))

    # Generate index.html
    index_output_path = get_output_path("index.html")
    with open(index_output_path, "wb") as index_fh:
        index_fh.write(
            render_doc(
                context=context,
                page_name="index",
                body_els=index.Body(context),
                head_els=index.Head(context),
            )
        )
        print(f"Wrote: {index_output_path}")

    # Generate drafts.html
    drafts_output_path = get_output_path("drafts.html")
    with open(drafts_output_path, "wb") as drafts_fh:
        drafts_fh.write(
            render_doc(
                context=context,
                page_name="drafts",
                body_els=drafts.Body(context),
                head_els=drafts.Head(context),
            )
        )
        print(f"Wrote: {drafts_output_path}")

    # Generate an HTML file for each post.
    for post in context["posts"]:
        author = context["authors"][post["author"]]
        post_output_path = get_output_path(f"{post['slug'].lstrip('/')}.html")
        with open(post_output_path, "wb") as fh:
            fh.write(
                render_doc(
                    context=context,
                    page_name="post",
                    body_els=post_tmpl.Body(context, post=post, author=author),
                    head_els=post_tmpl.Head(context, post=post),
                )
            )
            print(f"Wrote: {post_output_path}")


if __name__ == "__main__":
    main()
