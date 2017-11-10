# -*- coding: utf-8 -*-

"""Main module."""
from typing import Union
from xml.etree import ElementTree

import pkgutil
import io
import os
import pandas

RESOURCE_PATH: str
RESOURCE_PACKAGE: str
RESOURCE_PATH, _ = os.path.split(__file__)
# RESOURCE_PACKAGE = os.path.join(RESOURCE_PATH, 'templates', 'tasks.csv')
TEMPLATE = os.path.join(RESOURCE_PATH, 'templates', 'tasks.csv')
# TEMPLATE: io.BytesIO = io.BytesIO(pkgutil.get_data(RESOURCE_PACKAGE, RESOURCE_PATH))
"""
Default Todoist task template.
"""

def read_csv(template: Union[str, io.BytesIO] = TEMPLATE, **kwargs
            ) -> pandas.Index:
    """read_csv

    Longer description is....

    Parameters
    ----------
    template : Union[str, io.BytesIO]
        `template` is a csv file containing the headers expected by Todoist.
    **kwargs :
        See `pandas.read_csv` for key word arguments.

    Returns
    -------
    pandas.Index
        Returns the column Index from the template.

    """
    return pandas.read_csv(template, **kwargs).columns

def xml2df(xml_data: str) -> pandas.DataFrame:
    """Convert an XML string into a DataFrame.

    Parameters
    ----------
    xml_data : str
        xml_data is a string containing XML data.

    Returns
    -------
    pandas.DataFrame
        Return is a table of XML records.

    """
    root = ElementTree.XML(xml_data) # element tree
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
            all_records.append(record)
    return pandas.DataFrame(all_records)

# reveal_type(xml_data)
def read_paperless(file: str, drop_duplicates: bool = True
                  ) -> pandas.DataFrame:
    """Convert the Paperless XML file to a DataFrame.

    Convert the Paperless XML file to a DataFrame and remove duplicate entries
    if desired. The default is to remove.

    Parameters
    ----------
    file : str
        file is....
    drop_duplicates : bool
        If drop_duplicates is True, duplicate Paperless entries are removed.

    Returns
    -------
    pandas.DataFrame
        Return a DataFrame of the Paperless XML input.

    """
    xml_data: str = open(file).read()
    df: pandas.DataFrame = xml2df(xml_data)
    if drop_duplicates is True:
        df.drop_duplicates(inplace=True)
    return df

def convert(new_tasks: pandas.DataFrame, columns: pandas.Index = read_csv()
           ) -> pandas.DataFrame:
    """convert

    Longer description is....

    Parameters
    ----------
    new_tasks : pandas.DataFrame
        Paperless data imported from XML.
    columns : pandas.Index
        Todoist import template from CSV.

    Returns
    -------
    None

    """
    column_map = {'TYPE': list(), 'CONTENT': list()}
    for item in new_tasks.itertuples():
        column_map['TYPE'] += ['task']
        column_map['CONTENT'] += [item.itemName]
        if item.itemNote is not None:
            column_map['TYPE'] += ['note']
            column_map['CONTENT'] += [item.itemNote]

    df = pandas.DataFrame(columns=columns)
    df.TYPE = column_map['TYPE']
    df.CONTENT = column_map['CONTENT']
    return df

def write_csv(tasks: pandas.DataFrame, file: str) -> None:
    """Output the converted tasks in Todoist template format.

    Parameters
    ----------
    tasks : pandas.DataFrame
        Todoist tasks.
    file : str
        Output file name.

    Returns
    -------
    None

    """
    tasks.to_csv(file, index=False)
