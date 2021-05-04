import sys
import json
import subprocess
from pprint import pprint
from collections import OrderedDict

def parse_model_name(model_name, verbose=True):
    """To parse model name into json/dict

    Parameters:
        model_name: a string
        verbose: a bool

    Returns:
        a json/dict
    """
    # template json
    model_name_json = {'host':'', 'gpu config': '',
                        'core model name': '', 'internet source': '',
                        'dax': False, 'timestamp': ''}

    # Parse model name
    model_name = model_name.split('-')

    # Assign to template json
    model_name_json['host'] = model_name[0]
    model_name_json['gpu config'] = model_name[1]
    model_name_json['core model name'] = model_name[2]
    model_name_json['internet source'] = model_name[3]

    if 'dax' in model_name:
        model_name_json['dax'] = True
        model_name_json['timestamp'] = model_name[5]
    else:
        model_name_json['timestamp'] = model_name[4]

    # If verbose is True, print nicely json
    if verbose:
        if sys.version_info >= (3, 8):
            pprint(model_name_json, indent=2, sort_dicts=False)
        else:
            model_name_json = OrderedDict(model_name_json)
            print(json.dumps(model_name_json, indent=2))

    return model_name_json

def pprint_md(markdown_file):
    """To pretty print a markdown file with pygmentize

    Run `pip install Pygments` if there is none

    Parameters:
        markdown_file: a path to markdown file

    Returns: 
        none
    """
    subprocess.run(['pygmentize', markdown_file])

if '__main__' == __name__:
    model_name = 'ICT6-1_K80_12GiB-UNITER-vladsandulescu-dax-2021_04_30_09_39'
    model_name_json = parse_model_name(model_name, verbose=True)

    model_name = 'ICT6-4_K80_12GiB-VilBERT_CC-mmf_hateful_memes-2021_04_21_16_21'
    model_name_json = parse_model_name(model_name, verbose=True)

    pprint_md('Model_Name_Convention.md')
