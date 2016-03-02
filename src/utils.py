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
                color: #FFFFFF;
                padding:0px;
                display: table;
                border: 1px solid black;
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
                padding:0px;
                background: #ccebc5;
                border: 1px solid black;
                display: table-cell;
            }
            #fail {
                padding:0px;
                background:#fbb4ae;
                display: table-cell;
                border: 1px solid black;
            }
            #warn {
                padding:0px;
                width: 280px;
                background:#fdcdac;
                border: 1px solid black;
                display: table-cell;
            }

            width:400px;
            height:200px;
            background-color:#ffffff;
            font-size:28px;
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

def getHtmlHeader2(path):
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
        .lead{
            margin-top:20px;
            margin-bottom:8px;
            margin-left:20px;
            font-size:22px;
            font-weight:350;
            //line-height:8.4;
            font-family:'Trebuchet MS';
        }
        .lead_small{
            margin-top:5px;
            margin-bottom:5px;
            margin-left:20px;
            font-size:18px;
            font-weight:350;
            line-height:4.2;
            font-family:'Trebuchet MS';
        }
        .container {
             width: 28px;
             height: 18px;
             //overflow: auto;
             overflow-x:scroll;
             //position: absolute;
        }
        #tab {
            color: #FFFFFF;
            padding:20px;
            display: table;
            border: 0px solid black;
        }
        #row  {
            display: table-row;
        }
        #name {
            padding:1px;
            background:#d5sdfs;
            // border: 1px solid black;
            border: 0px;
            border-style: solid;
            border-color: #bdbdbd;
            display: table-cell;
            color:#000000;
            font-size:16px;
            font-family:'Trebuchet MS';
            font-weight:300;
            line-height:1.4;
        }
        #pass {
            padding:0px;
            background: #5cb85c;
            // border: 1px solid black;
            border: 1px;
            border-style: solid;
            border-color: #bdbdbd;
            display: table-cell;
        }
        #fail {
            padding:0px;
            background:#d9534f;
            border: 1px;
            border-style: solid;
            border-color: #bdbdbd;
            display: table-cell;
        }
        #warn {
            padding:0px;
            background:#f0ad4e;
            //border: 1px solid black;
            border: 1px;
            border-style: solid;
            border-color: #bdbdbd;
            display: table-cell;
        }

        /*font-size:28px;
        color:#ffffff;*/

    </style>
    <body>
        <div>
        <p class="lead"> FastQC summary </p>
    """
    html_str += """
        <p class="lead_small"> source directory: """
    html_str += path
    html_str += """</p>
    """
    html_str += """
        </div>
        <div id="tab">
            <div class="container" id="row">
                    <div class="container" id="name">
                    File
                    </div>
                    <div class="container" id="name">
                    Basic Statistics
                    </div>
                    <div class="container" id="name">
                    Per base sequence quality
                    </div>
                    <div class="container" id="name">
                    Per tile sequence quality
                    </div>
                    <div class="container" id="name">
                    Per sequence quality scores
                    </div>
                    <div class="container" id="name">
                    Per base sequence content
                    </div>
                    <div class="container" id="name">
                    Per sequence GC content
                    </div>
                    <div class="container" id="name">
                    Per base N content
                    </div>
                    <div class="container" id="name">
                    Sequence Length Distribution
                    </div>
                    <div class="container" id="name">
                    Sequence Duplication Levels
                    </div>
                    <div class="container" id="name">
                    Overrepresented sequences
                    </div>
                    <div class="container" id="name">
                    Adapter Content
                    </div>
                    <div class="container" id="name">
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
