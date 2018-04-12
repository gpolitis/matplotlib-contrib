#!/usr/bin/env python2.7
#
# Copyright @ 2018 Atlassian Pty Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# author: George Politis

import argparse
import numpy as np
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description=""" Plots one or more
    comma-separated values (CSV) file, each in its own figure.""")

    parser.add_argument('--min', type=int)
    parser.add_argument('--max', type=int)
    parser.add_argument('files', metavar='FILE',
            type=argparse.FileType('r'), nargs='+',
            help='The CSV files to plot.')

    args = parser.parse_args()

    for i in range(len(args.files)):
        x, y = np.loadtxt(
                args.files[i], delimiter=',', unpack=True, usecols=(0, 1))
        plt.figure(i)
        if args.min:
            plt.ylim(ymin=args.min)
        if args.max:
            plt.ylim(ymax=args.max)
        plt.plot(x, y)

    plt.show()

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
