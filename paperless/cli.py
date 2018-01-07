# -*- coding: utf-8 -*-

"""Console script for paperless."""

from pathlib import Path
import click
from paperless import convert, read_paperless, read_csv, write_csv


@click.command()
@click.option('--output', type=click.Path(exists=True), default=None,
              help='Todoist CSV task file (default: XML_INPUT.csv)')
@click.option('--template', type=click.Path(exists=True), default=None,
              help='Todoist exported template (default template provided)')
@click.option('--drop-duplicates', type=bool, default=True,
              help='Remove duplicate Paperless tasks [True (default), False]')
@click.argument('xml-input', type=click.Path(exists=True))
def main(xml_input: str = None, output: str = None, template: str = None,
         drop_duplicates: bool = True) -> None:
    """Console script for paperless.

    Convert Paperless_ XML format file (XML_INPUT) to CSV for import to
    Todoist_. The .xml extension is required.

    .. _Todoist: https://support.todoist.com/hc/en-us/articles/208821185

    .. _Paperless: http://crushapps.com/paperless/

    Free software: GNU General Public License v3
    """

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
