# -*- coding: utf-8 -*-

"""Console script for paperless."""

from pathlib import Path
import click
from paperless import convert, read_paperless, read_csv, write_csv


@click.command()
@click.option('--output', default=None, help='Todoist CSV task file')
@click.option('--template', default=None, help='Todoist exported template')
@click.option('--drop_duplicates', default=True,
              help='Remove duplicate Paperless tasks')
@click.argument('xml_input')
def main(xml_input: str, output: str, template: str,
         drop_duplicates: bool) -> None:
    """Console script for paperless."""

    df = read_paperless(xml_input, drop_duplicates=drop_duplicates)

    if template is None:
        dfnew = convert(df)
    else:
        dfnew = convert(df, columns=read_csv(template=template))

    if output is None:
        output = Path(xml_input).stem + '.csv'

    write_csv(dfnew, output)


if __name__ == "__main__":
    main()
