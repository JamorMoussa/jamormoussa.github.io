from datetime import datetime
from pathlib import Path
import click
import re


post_folder = Path("./_posts")

def slugify(title: str) -> str:
    title = title.lower()
    title = re.sub(r'[^\w\s-]', '', title)
    title = re.sub(r'[-\s]+', '-', title).strip('-_')
    return title

@click.group()
def cli():
    """Blog post management CLI."""
    pass

@cli.command()
@click.argument('title')
def create(title):

    today = datetime.today()
    date_str = today.strftime('%Y-%m-%d')
    year_str = today.strftime('%Y')
    slug = slugify(title)

    directory = post_folder / year_str 
    directory.mkdir(parents=True, exist_ok=True)

    filename = f'{date_str}-{slug}.md'
    filepath = directory / filename

    if filepath.exists():
        click.echo(f"⚠️  Post already exists: {filepath}")
        if not click.confirm("Do you want to overwrite it?"):
            click.echo("❌ Aborted.")
            return

    with open(filepath, 'w') as f:
        # with open(post_folder / "template.txt", "r") as templ:
        #     f.write(templ.read())

        f.write("\n".join([
                "---",
                "author: <mj>",
                f"title: {title}",
                f"date: {date_str}",
                "categories: [ ]",
                "tags: [ ]     # TAG n ames should always be lowercase",
                "description: # add some description here",
                "math: true # optional",
                "--- ",
        ]))

    click.echo(f"✅ Post created: {filepath}")

if __name__ == '__main__':
    cli()
