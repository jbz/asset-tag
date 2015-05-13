# asset-tag
Quick script to generate asset tags using the .ike schema

Enclosed is all data required to generate asset tags using Sailthru's scheme.  Our asset tags consist of two fields, a three-letter adjective and a second field loosely based on the Crayola colors list (designed ot be pronounceable by various cultures, etc.)  The colors have been squashed to single words, ideally of 3 syllables or less, with a few removed due to similarity.

In any case, the tag_gen.py script will, given a number, a file of prefixes, a file of colors and a file of current tags spit out a list of new tags (count 'number') which have been tested against the existing tag list.

It assumes the existing tag list is formatted as follows:

<PREFIX>_<COLOR>

...it will split on the underscore, lowercase everything if necessary, and then run tests.  It will spit out tags in <prefix>_<color> format.

This directory should also contain 'prefixes.txt', 'colors.txt' which are what they claim to be.
