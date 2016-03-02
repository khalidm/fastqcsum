'''
A program to summarize FastQC data.

Author: Khalid Mahmood (khalid.mahmood@unimelb.edu.au).

Copyright: 2016

See README.md for details about how to use the program.

Repository: https://github.com/khalidm/fastqcsum
'''

import os
import sys

def getHtmlHeader():
    html_str = """
        <!DOCTYPE html>
        <html lang="en-US">
        <head>

        <title>FastQC Summary</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <style type="text/css" media="screen">
            .comment .button {
                visibility: hidden;
            }
            .comment:hover .button {
                visibility: visible;
            }
            #tab {
                //width: 600px;
                color: #FFFFFF;
                padding:0px;
                display: table;
                border: 1px solid black;
                //border: 1px solid black;
            }
            #row  {
                display: table-row;
            }
            #name {
                padding:0px;
                width: 280px;
                background:#b3cde3;
                border: 1px solid black;
                display: table-cell;
                color:#000000;
            }
            #pass {
                //width:150px;
                padding:0px;
                background: #ccebc5;
                border: 1px solid black;
                display: table-cell;
                //background:#BF721B url("none") top left repeat-y;
            }
            #fail {
                //width:150px;
                padding:0px;
                background:#fbb4ae;
                display: table-cell;
                border: 1px solid black;
                //background:#446E2C url("none") top right repeat-y;
            }
            #warn {
                padding:0px;
                width: 280px;
                background:#fdcdac;
                border: 1px solid black;
                display: table-cell;
            }

            /* optional div height ,width, color */
            width:400px;
            height:200px;
            background-color:#ffffff;
            font-size:28px;
            /*color:#ffffff;*/
            color:#ffffff;
        </style>
        <body>
        <p>
            <div id="tab">
                <div id="row">
                        <div id="name">
                        File
                        </div>
                        <div id="name">
                        Basic Statistics
                        </div>
                        <div id="name">
                        Per base sequence quality
                        </div>
                        <div id="name">
                        Per tile sequence quality
                        </div>
                        <div id="name">
                        Per sequence quality scores
                        </div>
                        <div id="name">
                        Per base sequence content
                        </div>
                        <div id="name">
                        Per sequence GC content
                        </div>
                        <div id="name">
                        Per base N content
                        </div>
                        <div id="name">
                        Sequence Length Distribution
                        </div>
                        <div id="name">
                        Sequence Duplication Levels
                        </div>
                        <div id="name">
                        Overrepresented sequences
                        </div>
                        <div id="name">
                        Adapter Content
                        </div>
                        <div id="name">
                        Kmer Content
                        </div>
                </div>
        """
    return html_str


def getImageName(module):
    '''Build a string to match module name and image file name'''
    im = ""
    im_ex = False

    if module == "Basic Statistics":
        im_ex = False
        im = ""
    elif module == "Per base sequence quality":
        im = "per_base_quality.png"
        im_ex = True
    elif module == "Per tile sequence quality":
        im = "per_tile_quality.png"
        im_ex = True
    elif module == "Per sequence quality scores":
        im = "per_sequence_quality.png"
        im_ex = True
    elif module == "Per base sequence content":
        im = "per_base_sequence_content.png"
        im_ex = True
    elif module == "Per sequence GC content":
        im = "per_sequence_gc_content.png"
        im_ex = True
    elif module == "Per base N content":
        im = "per_base_n_content.png"
        im_ex = True
    elif module == "Sequence Length Distribution":
        im = "sequence_length_distribution.png"
        im_ex = True
    elif module == "Sequence Duplication Levels":
        im = "duplication_levels.png"
        im_ex = True
    elif module == "Overrepresented sequences":
        im = ""
        im_ex = False
    elif module == "Adapter Content":
        im = "adapter_content.png"
        im_ex = True
    elif module == "Kmer Content":
        im = "kmer_profiles.png"
        im_ex = True
    else:
        im = ""
        im_ex = False

    return im, im_ex
