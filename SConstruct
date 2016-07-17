import os
import glob
from nbflow.scons import setup

env = Environment(ENV=os.environ)
setup(env, ["notebooks"])

figures = sorted(glob.glob("writeup/figs/*.pdf"))
env.PDF("writeup/rocha_etal.pdf", "writeup/rocha_etal.tex")
env.Depends("writeup/rocha_etal.pdf",   figures)
