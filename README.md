Overview {#overview}
============

ffea-meshing are a series of Python tools for [FFEA](https://bitbucket.org/FFEA/ffea/downloads/) meshes.


Scripts {#scripts}
=============

   * **tet_from_pix.py** - Processes MRC files and produces a regular
    tetrahedral volumetric mesh for FFEA using the "marching tet" algorithm.
    This is written out in the tetgen .ele, .face, and .node file format for
    later use in FFEA, and .vtk for mesh analysis.

   * **mrc_zoom.py** - Coarsens MRC files to a user-defined resolution and
    outputs them as a new .mrc file. Can be called by tet_from_pix.

   * **ffea_convert_to_vtk.py** - Converts FFEA systems into VTK files for
    analysis in ParaView and other compatible software.


Prerequisites {#prerequisites}
=============

   * [Python (>= 3.8)](https://www.python.org/).
     Required for running the tool scripts.

   * [NumPy](https://numpy.org/).
     Required Python library.

   * [SciPy](https://scipy.org/).
     Required Python library.

   * [VTK for Python](https://pypi.org/project/vtk/).
     Required Python library.

   * [mrcfile for Python](https://pypi.org/project/mrcfile/).
     Required Python library.


How to Use {#how}
=============

As these are simply scripts there is no installation required other than the
 [prerequisites](\ref prerequisites).

tet_from_pix {#tetfrompix}
-------------

tet_from_pix inputs MRC files and processes them to produce volumetric mesh
 files for use with FFEA. VTK files are also produced for mesh analysis.

To get started quickly, the usage message can be viewed with the following command:

      python tet_from_pix.py -h

In order to run tet_from_pix to produce volumetric mesh files, there are three
 required flags:

   * `-i` or `--input` - The filepath to the input MRC file to be processed.
   * `-o` or `--output` - The name to be given to the output files. A filepath
    can also be provided for this. Do not include a file extension suffix as
    there will be multiple different kinds.
   * `-t` or `--threshold` - <!-- Molly - can you explain this -->

Running the required flags on an MRC would look something like the example
 command:

      python tet_from_pix.py -i /path/to/input.mrc -o /path/to/output -t 0.12345

Optionally, an MRC file can first be coarsened to a user-specified resolution
 before producing mesh files using the flag `-r` or `--resolution`, followed by
 the resolution value. See [mrc_zoom](\ref mrczoom) for further explanation, as
 this flag passes the input MRC file to this script and returns the output.

In the output directory defined by `-o` or `--output`, the following files will
 be found after running tet_from_pix successfully, where [outputname] is the
 user-defined name of the output files:

   * [outputname].1.ele
   * [outputname].1.face
   * [outputname].1.node
   * [outputname].mrc (if the `-r` or `--resolution` flag was called)
   * [outputname].vtk

mrc_zoom {#mrczoom}
-------------

mrc_zoom inputs MRC files and allows a user to coarsen them to a defined
 resolution, and outputs them as a new MRC file. This is seperated from
 tet_from_pix as a standalone script for users that only wish to coarsen an
 MRC file, rather than go through the whole process of producing volumetric
 mesh files.

To get started quickly, the usage message can be viewed with the following command:

      python mrc_zoom.py -h

In order to run tet_from_pix to produce volumetric mesh files, there are three
required flags:

   * `-i` or `--input` - The filepath to the input MRC file to be coarsened.
   * `-o` or `--output` - The name to be given to the output file. A filepath
    can also be provided for this. A file extension suffix is not needed.
   * `-r` or `--resolution` - A number value of the resolution to coarsen the
    MRC file to. <!-- Molly - you might be able to give more detail here -->

Running the required flags on an MRC would look something like the example
 command:

      python mrc_zoom.py -i /path/to/input.mrc -o /path/to/output -r 10

In the output directory defined by `-o` or `--output`, a new .mrc file will be
 found after running mrc_zoom successfully of the coarsened MRC, named after the
 user-defined output name.

<!-- Note: This README style is inconsistent because of format changes made in the branch interpolation which will be merged at a later date. I had to compromise. -->
## ffea_convert_to_vtk {#ffea-vtk}

ffea_convert_to_vtk inputs FFEA scripts to find their input mesh(s), apply any
 transformations as dictated by the script, and then output them as points-only
 VTK files for mesh analysis.

**NOTE**: This tool is currently incomplete. This will not yet process transformations
 dictated by coupling in FFEA scripts. This feature is to be added at a later date.

In order to run ffea_convert_to_vtk there are two required flags:

   * `-i` or `--input` - The filepath to the input FFEA file to be converted.
   * `-o` or `--output` - The destination filepath of the output VTK file.

Running the conversion tool would look something like the example command:

     python fea_convert_to_vtk.py -i /path/to/input.ffea -o /path/to/output

In the output directory defined by `-o` or `--output`, the file [outputname].vtk
 will be found, where [outputname] is the name of the input FFEA script.

The output VTK file can be viewed in ParaView for analysis. When the VTK file is
 first loaded into ParaView, there will be nothing to see. A Glyphs filter needs
 to be applied to it first. This is done by selecting the VTK in the Pipeline
 Browser on the left, and then applying the Glyphs filter found in Filters >
 Alphabetical/Common. When adding these glyphs, ensure that in their properties
 that the Glyph Mode under Masking is set to All Points (see example in image
 below) or there will be vertices missing. The size and shape of the glyphs can
 also be adjusted in this properties panel.

![VTK converted from FFEA script viewed in Paraview](docs/ffea-vtk.png)


Unit Tests {#unit}
=============

The directory `tests` contain unit tests for developers working on ffea-meshing.
 Inside is a script called `unit_tests.py` which executes the tests, and the
 required input and output files for these tests.

To get started quickly, the usage message can be viewed with the following command:

      python unit_tests.py -h

There are three unit tests, which are as follows:

   1. Tests running tet_from_pix without coarsening the input MRC file.
   2. Tests running mrc_zoom.
   3. Tests running tet_from_pix with coarsening of the input MRC file.

If unit_tests is called with no flags, all three tests will run. To run specific
 tests, use the `t` or `--test` flag with the number(s) of test(s). For example,
 to run tests 1 and 3, run the following command:

      python unit_tests.py -t 1,3

The command line will print out each test ran and state if they passed or failed.
