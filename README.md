Seasonality of submesoscale dynamics in the Kuroshio Extension
============

Authors
--------
[Cesar B. Rocha](https://crocha700.github.io)<sup>1</sup>, [Sarah T. Gille](http://www-pord.ucsd.edu/~sgille/)<sup>1</sup>
, [Teresa K. Chereskin](http://tryfan.ucsd.edu)<sup>1</sup>,
and [Dimitris Menemenlis](https://science.jpl.nasa.gov/people/Menemenlis/)<sup>2</sup>.

1: [Scripps Institution of Oceanography](https://scripps.ucsd.edu),
[University of California San Diego](http://www.ucsd.edu), La Jolla, CA, USA.

2: [Earth Sciences Division, Jet Propulsion Laboratory](Earth Sciences Division, Jet Propulsion Laboratory), [California Institute of Technology](https://www.caltech.edu), Pasadena, CA, USA.

Key Points
----------

  - Upper-ocean submesoscale (10-100 km) turbulence and inertia-gravity waves undergo strong seasonal cycles that are out of phase.
  - Submesoscale turbulence dominates the horizontal velocity and sea-surface height variability in late winter/early spring.
  - Submesoscale inertia-gravity waves dominate the horizontal velocity and sea-surface height variability in late summer/early fall.

Abstract
--------
Recent studies show that the vigorous seasonal cycle of the mixed layer modulates 
upper-ocean submesoscale turbulence. 
Here we provide model-based evidence that the seasonally-changing upper-ocean 
stratification in the Kuroshio Extension also modulates submesoscale (here 10-100 km) 
inertia-gravity waves. Summertime re-stratification weakens submesoscale 
turbulence but enhances inertia-gravity waves near the surface. Thus, 
submesoscale turbulence and inertia-gravity waves undergo vigorous out-of-phase 
seasonal cycles. These results imply a strong seasonal modulation of 
the accuracy of geostrophic velocity diagnosed from submesoscale 
sea-surface height delivered by the Surface Water and Ocean Topography (SWOT) 
satellite mission.

Status
----------
  The [paper](https://crocha700.github.io/UpperOceanSeasonality/) is *in press* in
  in [Geophysical Research Letters](http://agupubs.onlinelibrary.wiley.com/agu/journal/10.1002/(ISSN)1944-8007/),
  [doi: 10.1002/2016GL071349](http://onlinelibrary.wiley.com/doi/10.1002/2016GL071349/full).
  [Supporting information](https://github.com/crocha700/UpperOceanSeasonality/blob/master/writeup/rocha_etal_supporting-info.pdf) and [figures](https://github.com/crocha700/UpperOceanSeasonality/blob/master/writeup/figs/) are also available. Comments, questions, and suggestions are extremely welcome
  and warmly appreciated. Feedback can be submitted through github [issues](https://github.com/crocha700/UpperOceanSeasonality/issues) or via e-mail to
  Cesar Rocha (crocha@ucsd.edu).

Code
----
The analysis for this paper has been performed on NASA's [Pleiades Supercomputer](http://www.nas.nasa.gov/hecc/resources/pleiades.html). The project uses two small pieces of code developed by the first author and available on github:  [llctools](https://github.com/crocha700/llctools) and [pyspec](https://github.com/pyspec/pyspec). Those codes leverage on the [Scientific
Python stack](https://www.scipy.org/install.html). Specific processing and plotting codes are available on Jupyter [notebooks](https://github.com/crocha700/UpperOceanSeasonality/blob/master/notebooks/index.ipynb).

Once the heavy computations are performed on Pleiades and the output files are saved in netCDF4, the whole subsequent processing and plotting and LaTeX compiling
is performed in a single-button reproducible workflow using [nbflow](https://github.com/jhamrick/nbflow).  The draft is built online and
published using [gh-puslisher](https://github.com/ewanmellor/gh-publisher).

Data
------
The LLC outputs can be obtained from the [ECCO project](http://ecco2.org/llc\_hires).
The gridded altimeter data were produced by Ssalto/Duacs and distributed by
[AVISO](http://www.aviso.altimetry.fr/duacs/), with support from CNES. The Argo
Roemmich-Gilson climatology can be downloaded from the [SIO Argo group](http://sio-argo.ucsd.edu/RG_Climatology.html). KEO mooring data are available
from [NOAA PMEL](http://www.pmel.noaa.gov/ocs/KEO). KESS mooring data are available
from the [US KESS project](http://uskess.whoi.edu/?page_id=406).

Support
-------
This research was funded by NSF (OCE1357047) and NASA (NNX13AE44G,NNX13AE85G,NNX16AH67G).

Acknowledgments
----------------
[William R. Young](http://www-pord.ucsd.edu/~wryoung) provided helpful feedback on the first draft. Thanks to our colleagues at the [NASA Advanced Supercomputing Division](http://www.nas.nasa.gov) and the MITgcm
and SciPy communities for their awesome support.
