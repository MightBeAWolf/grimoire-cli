import re
import shlex
import click
import sys
from rich.console import Console
from rich.syntax import Syntax
import subprocess

class CodeBlock:
    def __init__(self, title, args, language, block):
        self.title = title.strip()
        self.args = args
        self.language = language.strip()
        self.block = block

    def markdown_format(self):
        formatted_args = None
        if self.args:
            arg_list = "\n".join([f"- `{arg}`" for arg in self.args]) if self.args else ''
            formatted_args = f"Arguments:\n{arg_list}\n\n"
        return f"#### {self.title}\n\n{formatted_args or ''}```{self.language}\n{self.block}\n```"

def parse_markdown(md_content):
    pattern = r"#### (?P<title>.+)\n(\nArguments:\n(?P<args>(- (.+)\n)*))?\n*```(?P<language>[^\n]+)\n(?P<block>(.*\n)*?)```"

    code_blocks = []
    for match in re.finditer(pattern, md_content):
        args = None
        if match.group('args'):
            args = [arg.strip('- \n') for arg in match.group('args').split('\n') if arg]
        code_blocks.append(CodeBlock(
           match.group('title'), 
           args,
           match.group('language'),
           match.group('block')))
    return code_blocks

@click.group()
def cli():
    pass

@click.command()
@click.argument('md_content', type=click.File('r'))
def list(md_content):
    """List all Markdown code blocks by their title."""
    code_blocks = parse_markdown(md_content.read())
    for block in code_blocks:
        click.echo(block.title)

@click.command()
@click.argument('md_content', type=click.File('r'))
@click.argument('titles', nargs=-1)
def show(md_content, titles):
    """Show one or more of the code blocks in their original markdown format."""
    code_blocks = parse_markdown(md_content.read())
    console = Console()

    for block in code_blocks:
        if not titles or block.title in titles:
            syntax = Syntax(block.markdown_format(), "markdown", theme="monokai", word_wrap=True)
            console.print(syntax)

@click.command()
@click.argument('md_content', type=click.File('r'))
@click.argument('title')
@click.argument('args', nargs=-1)
@click.option('--verbose', '-v', is_flag=True, help='Enables verbose mode.')
@click.option('--debug', '-d', is_flag=True, help='Enables debug mode.')
def exec(md_content, title, args, verbose=False, debug=False):
    """Execute the code block using the appropriate interpreter."""
    code_blocks = parse_markdown(md_content.read())

    for block in code_blocks:
        if block.title == title:
            if block.language == "bash":
                command_args = shlex.quote(" ".join(args))
                command = f'bash -{"xc" if debug else "c"} {shlex.quote(block.block)} {md_content.name} {command_args}'
                if verbose or debug:
                    print(command)
                process = subprocess.Popen(command, shell=True, executable='/bin/bash')
                process.communicate()
                process.wait()
                sys.exit(process.returncode)
            else:
                click.echo(f"Execution for language {block.language} not supported.")
            break

cli.add_command(list)
cli.add_command(show)
cli.add_command(exec)

if __name__ == '__main__':
    cli()
