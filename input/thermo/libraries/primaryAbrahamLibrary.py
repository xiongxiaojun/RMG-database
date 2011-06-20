#!/usr/bin/env python
# encoding: utf-8

name = "primaryAbrahamLibrary"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "O2",
    molecule = 
"""
1     O     1 {2,S}
2     O     1 {1,S}
""",
    thermo = '0.0',
    shortDesc = u"""0.0 0.0 -0.723 0.0 0.191 !experimental descriptors for molecular oxygen""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "HOJ",
    molecule = 
"""
1     O     1
""",
    thermo = '0.524',
    shortDesc = u"""0.378 0.309 0.802 0.348 0.146 !descriptors for H2O but with the contribution of 1 OH group to A""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

