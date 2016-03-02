'''
A program to summarize FastQC data.

Author: Khalid Mahmood (khalid.mahmood@unimelb.edu.au).

Copyright: 2016

See README.md for details about how to use the program.

Repository: https://github.com/khalidm/fastqcsum
'''

from utils import *

import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fastqcs", type=str, dest="path_to_fastqcs", help="Input path to fastQC directories.", required=True)
    # parser.add_argument("-o", "--output", type=str, dest="out", help="Output file name (html).", required=True)

    parser.add_argument("-v", "--verbosity", action="count", default=0)
    args = parser.parse_args()

    path_to_fastqcs = args.path_to_fastqcs
    fastqc_summary_html = open(path_to_fastqcs + '/fastqcsum.html', mode='wb')
    html_str = getHtmlHeader2(path_to_fastqcs)

    # look for fastqc_data.txt files through all sub-directories
    for root, dirs, files in os.walk(path_to_fastqcs):
        for name in files:
            if (name == "fastqc_data.txt"):
                sample_name = sample_name = root.split("/")[-1][:-7]

                html_str += """
                <div id="row">
                """
                html_str += """
                <div id="name">
                """
                html_str += sample_name
                html_str += """
                </div>
                """

                with open(os.path.join(root, name), "r") as f:
                    for line in f.readlines():
                        line = line.strip()
                        if (line[:2] == ">>" and line[:12] != ">>END_MODULE"):
                            module = line[2:-5]
                            status = line[-4:]
                            image_file = ""

                            img, img_exists = getImageName(module)
                            if img_exists:
                                image_file = root + "/Images/" + img

                            temp_str = "<div id=\"" + status + "\" onclick=\"location.href='" + image_file + "';\" " + "style=\"cursor:pointer;\">"
                            html_str += temp_str

                            html_str += """
                            </div>
                            """
                        elif (line[:2] != ">>" and line[:2] != "##"):
                            cols = line.split("\t")
                            col1 = cols[0]
                            ocols = "|".join(cols[1:])

                html_str += """
                </div>
                """
    html_str += """
    </div>
    </body>
    </html>
    """

    fastqc_summary_html.write(html_str)
    fastqc_summary_html.close()


if __name__ == '__main__':
    main()
