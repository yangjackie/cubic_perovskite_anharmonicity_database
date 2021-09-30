# cubic_perovskite_anharmonicity_database

This repository provides the raw data associated with the publication 'An Atlas of Vibrational Anharmonicty for Cubic ABX3 Perovskites'. A set of Jupyter notebooks are also provided for analyzing and visualizing the data. These notebooks can be built with Binder (https://mybinder.org/) to start up a virtual environments for analyzing the data online.

* The db files are the SQLite databases that hold the core data from this work, namely the optimised crystal structures, formation enthalpies and vibrational anharmonicity scores for each perovskite screened computationally. These data are persisted into the SQLite database using the functionalities from the Atomic Simulation Environment Python package. (These databases are organized according to the elemental identity of the X anions in the ABX3 compound). 

* In addition, we provide the following raw data for each compound in separate folders, which may be useful for anyone who's interested in doing some future analysis. These data includes:

1. The SPOSCAR file correponding to the (2x2x2) supercell structure used for the phonon calculations.

2. The vasprun_md.xml VASP output file from the production run of ab initio MD calculations. 

3. The harmonic force constants (force_constants.hdf5 file) from the Phonopy calculations.

4. The second- and third-order force constants (fc2.hdf5 and fc3.hdf5 files) from the Phono3py calculations.
