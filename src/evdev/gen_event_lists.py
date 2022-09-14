#!/usr/bin/env python3

# evtest-qt - A graphical joystick tester
# Copyright (C) 2015 Ingo Ruhnke <grumbel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import re


LINUX_INPUT_EVENT_CODES_HEADER="/usr/include/linux/input-event-codes.h"


def gen_event_list(rgx, outfilename):
    with open(outfilename, 'w') as fout:
        fout.write("// autogenerated by '{}', do not edit by hand\n\n".format(
            os.path.basename(__file__)))

        with open(LINUX_INPUT_EVENT_CODES_HEADER, 'r') as fin:
            for line in [l for l in fin.readlines() if re.search(rgx, l)]:
                name = line.split()[1]
                if not re.search(r'(_MAX|_CNT)$', name):
                    fout.write("#ifdef {}\n".format(name))
                    fout.write("  add({}, \"{}\");\n".format(name, name))
                    fout.write("#endif\n\n")

        fout.write("/* EOF */\n")


if __name__ == "__main__":
    gen_event_list(r'^#define (BTN|KEY)', 'key_list.x')
    gen_event_list(r'^#define REL', 'rel_list.x')
    gen_event_list(r'^#define ABS', 'abs_list.x')


# EOF #