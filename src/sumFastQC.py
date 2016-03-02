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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fastqcs", type=str, dest="path_to_fastqcs", help="Input path to fastQC directories.", required=True)
    # parser.add_argument("-o", "--output", type=str, dest="out", help="Output file name (html).", required=True)

    parser.add_argument("-v", "--verbosity", action="count", default=0)

    args = parser.parse_args()

    outputfile = open(args.out, "w")
    # path_to_fastqcs = sys.argv[1]

    fastqc_summary_html = open(path_to_fastqcs + '/fastqcsum.html', mode='wb')

    html_str = getHtmlHeader()

    # walk a directory containing FastQC output for multiple samples
    for root, dirs, files in os.walk(path_to_fastqcs):
        for name in files:
            if (name == "fastqc_data.txt"):
                # use string slicing here if you only want part of the filename as
                # the id
                fileid = fileid = root.split("/")[-1][:-7]

                html_str += """
                <div id="row">
                """
                html_str += """
                <div id="name">
                """
                html_str += fileid
                html_str += """
                </div>
                """

                with open(os.path.join(root, name), "r") as f:
                    for line in f.readlines():
                        line = line.strip()
                        # summary data
                        if (line[:2] == ">>" and line[:12] != ">>END_MODULE"):
                            module = line[2:-5]  # grab module name
                            status = line[-4:]  # and overall status pass/warn/fail

                            #image_file = root + "/Images/" + module.replace(" ", "_") + ".png"
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
