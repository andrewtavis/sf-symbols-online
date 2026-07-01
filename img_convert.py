"""
Converts all the black PNGs in /glyphs to white PNGs in /glyphs_white.
"""

import os
from os import listdir
from os.path import isfile, join

from tqdm.auto import tqdm

imgs = [f for f in listdir("./glyphs") if isfile(join("./glyphs", f))]

# The following uses ImageMagick.
# See: https://imagemagick.org/index.php
for img in tqdm(imgs, desc="Images converted", unit="imgs"):
    black_to_white_script = f"convert ./glyphs/{img} -alpha on -fill white -colorize 100 -alpha on ./glyphs_white/{img}"
    os.system(black_to_white_script)
