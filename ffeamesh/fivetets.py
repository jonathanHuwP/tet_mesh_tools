"""
 This file is part of the FFEA simulation package

 Copyright (c) by the Theory and Development FFEA teams,
 as they appear in the README.md file.

 FFEA is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 FFEA is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with FFEA.  If not, see <http://www.gnu.org/licenses/>.

 To help us fund FFEA development, we humbly ask that you cite
 the research papers on the package.

    Authors: Joanna Leng, Jonathan Pickering - University of Leeds
    Emails: J.Leng@leeds.ac.uk, J.H.Pickering@leeds.ac.uk
"""
# set up linting
# pylint: disable = import-error

import datetime
import getpass
import numpy as np
import mrcfile
import vtk.util.numpy_support
from ffeamesh.writers import write_ffea_output

def even_cube_tets(cube):
    """
    convert a list of the eight vertices of a an even cube
    into a list of lists representing tets
    Args:
        cube (list): the eight vertices of a cube
    Returns
        lits(list) : five lists of four vertices representing the tets
    """
    tet1 = np.array([cube[0], cube[4], cube[5], cube[7]])
    tet2 = np.array([cube[0], cube[1], cube[2], cube[5]])
    tet3 = np.array([cube[2], cube[5], cube[6], cube[7]])
    tet4 = np.array([cube[0], cube[2], cube[3], cube[7]])
    tet5 = np.array([cube[0], cube[2], cube[5], cube[7]])

    tet_list = [tet1, tet2, tet3, tet4, tet5]

    return tet_list

def odd_cube_tets(cube):
    """
    convert a list of the eight vertices of a an odd cube
    into a list of lists representing tets
    Args:
        cube (list): the eight vertices of a cube
    Returns
        lits(list) : five lists of four vertices representing the tets
    """
    tet1 = np.array([cube[0], cube[1], cube[3], cube[4]])
    tet2 = np.array([cube[1], cube[4], cube[5], cube[6]])
    tet3 = np.array([cube[1], cube[2], cube[3], cube[6]])
    tet4 = np.array([cube[3], cube[4], cube[6], cube[7]])
    tet5 = np.array([cube[1], cube[3], cube[4], cube[6]])

    tet_list = [tet1, tet2, tet3, tet4, tet5]

    return tet_list

def is_odd(x, y, z):
    '''
    Logic to decide if a voxel is an odd or and even.
    Args:
        x (int) Index for x value in values array.
        y (int) Index for y value in values array.
        z (int) Index for z value in values array.
    Returns:
        (int)   0 represnt voxel in an even position and 1 represents a voxel in an odd position
    '''
    flag = None
    # Logic for alternating tet division 0 (even) or 1 (odd) - to identify the odd and even voxels
    if z % 2 == 0:
        if y % 2 == 0:
            if x % 2 == 0:
                flag = 0
            else:
                flag = 1
        else:
            if x % 2 == 0:
                flag = 1
            else:
                flag = 0
    else:
        if y % 2 == 0:
            if x % 2 == 0:
                flag = 1
            else:
                flag = 0
        else:
            if x % 2 == 0:
                flag = 0
            else:
                flag = 1

    return flag

def create_cube_coords(x, y, z, x_trans, y_trans, z_trans, res, coords, ncoord):
    '''
    Caluculates the next 8 coords for the next volxel that has been thresholded
    previously (logic in loop that calls this one).
    Args:
        x (int)           Indecies to the x coord in the coords array.
        y (int)           Indecies to the y coord in the coords array.
        z (int)           Indecies to the z coord in the coords array.
        x_trans  (float)  Offset in x axis for the data.
        y_trans  (float)  Offset in y axis for the data.
        z_trans  (float)  Offset in z axis for the data.
        res  (float)    Resolution of the data.
        coords (float numpy array)  The coordinates of the thresholded voxels passed by reference to this function.
        ncoord (int)    Index to the coords array which is a vertex of a voxel passed by reference to this function.
    Returns:
        None
    '''

    # Calculate the cordinates of each vertex of the voxel so it aligns with the isosurface
    coord1 = [((x-0.5)*res)+x_trans, ((y-0.5)*res)+y_trans, ((z-0.5)*res)+z_trans]
    coords[ncoord] = coord1
    coord2 = [((x+0.5)*res)+x_trans, ((y-0.5)*res)+y_trans, ((z-0.5)*res)+z_trans]
    coords[ncoord+1] = coord2
    coord3 = [((x+0.5)*res)+x_trans, ((y+0.5)*res)+y_trans, ((z-0.5)*res)+z_trans]
    coords[ncoord+2] = coord3
    coord4 = [((x-0.5)*res)+x_trans, ((y+0.5)*res)+y_trans, ((z-0.5)*res)+z_trans]
    coords[ncoord+3] = coord4
    coord5 = [((x-0.5)*res)+x_trans, ((y-0.5)*res)+y_trans, ((z+0.5)*res)+z_trans]
    coords[ncoord+4] = coord5
    coord6 = [((x+0.5)*res)+x_trans, ((y-0.5)*res)+y_trans, ((z+0.5)*res)+z_trans]
    coords[ncoord+5] = coord6
    coord7 = [((x+0.5)*res)+x_trans, ((y+0.5)*res)+y_trans, ((z+0.5)*res)+z_trans]
    coords[ncoord+6] = coord7
    coord8 = [((x-0.5)*res)+x_trans, ((y+0.5)*res)+y_trans, ((z+0.5)*res)+z_trans]
    coords[ncoord+7] = coord8







def convert_mrc_to_5tets(input_file, output_file, threshold, ffea_out, vtk_out):
    """
    convert the contents of an mrc file to a tetrohedron array
    Args:
        input_file (pathlib.Path)
        output_file (pathlib.Path)
        threshold (float)
        ffea_out (bool)
        vtk_out (bool)
    Returns:
        None
    """

    """
    An explanation of the various data strucutres and what python packages need them.

    Coords (numpy array)    A 2d array for the 1st axis it is (x, y, z) float values and
                            2nd it is all verticies of all the thresholded volxes which
                            includes duplicates.
    ncoords (int)           Probably not needed. Number or length of the coords array i.e. the number of voxels
                            in the coords array.
    Values/Densitys (float python array) It is used for the threshold and is not needed by ffea but can be used by vtk
    nvalues (int)             Probably not needed. Number or length of the coords array
    ConnectVoxs (int numpy array) Could be an array of arrays. An array that holds indexes to the
                                  coords array that make it clear which coords are vertexies of each voxel
    nconnectvoxs (int)     Number or length of the cnnectvoxs array
    ConnetTets (int numpy array) Could be an array of arrays. An array that holds indexes to the
                                 coords array that make it clear which coords are vertexies of each cell/tetrahedron
    nconnecttets (int)     Number or length of the connecttets array
    CellType (int)               Lets vtk know what type of cell it is. A value of 10 is a tetrahedron.


    mrc (mrc utility)      A map which is the fastest way to work with the data and has
                                 a header and data section in it.

    cube (int numpy array)    Numpy array of 3 values represnting the x, y, z indecies into the coords array.
    """

    # Reads mrc file into a map which is the fastest way to work with the data and has
    # a header and data section in it.
    mrc = mrcfile.mmap(input_file, mode='r+')


    '''
    move this here so you go through the data less times
    # Calulate the size of the numpy arrays needed by vtk writer.
    #nvoxel = np.count_nonzero(mrc.data)
    # Calulate size of all arrays that will be needed by the vtk writer array
    for z in range(0, mrc.header.nz):
        for y in range(0, mrc.header.ny):
            for x in range(0, mrc.header.nx):
                # Threshold the voxels out of the mrc map data


                if mrc.data[z,y,x] > threshold:
                    nvox = nvox + 1


    ncoord = nvox * 8
    nconnect = nvox * 20
    cubecoords (float numpy array) the x, y, z coordinate vlaues for each vertex of a voxel.
    '''

    nvoxel = sum([np.count_nonzero(x>=threshold) for x in mrc.data.flatten()])

    coords = np.zeros((nvoxel*8, 3))
    ncoord = 0
    res = float(mrc.header.cella['x'])/mrc.header.nx
    x_trans = float(mrc.header.origin['x'])
    y_trans = float(mrc.header.origin['y'])
    z_trans = float(mrc.header.origin['z'])
    alternate = np.zeros((nvoxel,))
    location = 0

    # Create an array of array of 8 point (co-ordinates) for each hexahedron (voxel)
    for z in range(0, mrc.header.nz):
        for y in range(0, mrc.header.ny):
            for x in range(0, mrc.header.nx):
                # Threshold the voxels out of the mrc map data
                if mrc.data[z,y,x] > threshold:

                    create_cube_coords(x, y, z, x_trans, y_trans, z_trans, res, coords, ncoord)
                    ncoord=ncoord+8

                    alternate[location]=is_odd(x, y, z)
                    location=location+1

    # make the connectivity data for voxels
    points, cells = make_voxel_connectivity(nvoxel, coords)

    # make the connectivity for tets
    tet_array = make_tet_connectivity(nvoxel, cells, alternate)

    write_tets_to_files(nvoxel, points, cells, tet_array, output_file, ffea_out, vtk_out)

def write_tets_to_files(nvoxel, points, cells, tet_array, output_file, ffea_out, vtk_out):
    """
    outupt the files
    Args:
        nvoxel (int): voxel count
        points (numpy.ndarray): coordinates of vertices (no duplicates)
        cells (numpy.ndarray): nvoxel by 8 array listing indices of
                               vertices in points for each voxel
        tet_array (int np.ndarray): 2D number of tets by four, the entry for each tet
                                    is a list of its four vertices in the points array
        output_file (pothlib.Path): name stem for ouput files
        ffea_out (bool): if true write ffea input files
        vtk_out (bool): if true write a vtk file
    Returns:
        None
    """
    # make the vtk tet connectivity
    cells_con = make_vtk_cell_connectivity(tet_array, len(cells))

    # make the gris (vtk scene)
    vtkPts = vtk.vtkPoints()
    vtkPts.SetData(vtk.util.numpy_support.numpy_to_vtk(points, deep=True))
    grid = vtk.vtkUnstructuredGrid() #create unstructured grid
    grid.SetPoints(vtkPts) #assign points to grid
    grid.SetCells(vtk.VTK_TETRA, cells_con) #assign tet cells to grid

    #write vtk file
    if vtk_out:
        vtk_output(grid, output_file)

    # write tetgen file for ffea input
    if ffea_out:
        ffea_output(grid, points, output_file, nvoxel, tet_array)

def vtk_output(grid, output_file):
    """
    setup and use vtk writer
    Args:
        grid (vtk.vtkUnstructuredGrid): vtk scene
        output_file (pathlib.Path)
    """
    writer = vtk.vtkUnstructuredGridWriter()
    writer.SetFileName(str(output_file.with_suffix(".vtk")))
    writer.SetInputData(grid)
    writer.Update()
    writer.Write()

def ffea_output(grid, points, output_file, nvoxel, tet_array):
    """
    construct the faces and output the ffea input files
    Args:
        grid (vtk.vtkUnstructuredGrid): vtk scene
        points (float np.ndarray): duplicate free list of vertices
        output_file (pathlib.Path): name stem of output files
        nvoxel (int): the number of voxels
        tet_array (int np.ndarray): 2D number of tets by four, the entry for each tet
                                    is a list of its four vertices in the points array
    Returns:
        None
    """
    # make a surface filter to extract the geometric boundary
    surfFilt2 = vtk.vtkDataSetSurfaceFilter()
    surfFilt2.SetInputData(grid)
    surfFilt2.Update()

    # get the geometric boundary (the suface of the volume)
    surf = surfFilt2.GetOutput()

    # get the points in the surface geomatry
    surf_points=np.array(surf.GetPoints().GetData())

    # get the surface polygons
    cells = surf.GetPolys()
    nCells = cells.GetNumberOfCells()
    array = cells.GetData()

    # make a connectivity into the tets points
    original_ids = np.zeros((len(surf_points),), dtype='int16')
    for pos in range(len(surf_points)):
        # surface point
        point = surf_points[pos]
        # index of sourface point in the tet's points array
        original_ids[pos] = np.where((points==point).all(axis=1))[0]

    # This holds true if all polys are of the same kind, e.g. triangles.
    assert(array.GetNumberOfValues()%nCells==0)

    # reshape the cells array to match tet gen output standard
    nCols = array.GetNumberOfValues()//nCells
    numpy_cells = np.array(array)
    faces = numpy_cells.reshape((-1,nCols))

    #write to tetgen .ele, .node, .face
    date = datetime.datetime.now().strftime("%x")
    comment = f'# created by {getpass.getuser()} on {date}'
    write_ffea_output(output_file,
                      nvoxel,
                      tet_array,
                      points,
                      faces,
                      original_ids,
                      comment)

def make_voxel_connectivity(nvoxel, coords):
    """
    construct a duplicate free list of vertices coordinates and a
    connectivity list mapping voxles to lists of eight vertices
    Args:
        nvoxel (int):                  the number of voxels
        coords (float numpy.ndarray):  an 2d array with each element being an array of length 8
                                       (one element for each vertex of a voxel and is the index
                                        of a value in the coords array) and the length
                                        of the overall array is the number of voxels that have
                                        been thresholded.

    Returns:
        points (float numpy.ndarray):  duplicate free list of voxel vertices
        cells (int numpy.ndarray):     nvoxel by 8 array listing indices of
                                       vertices in points for each voxel

    """
    # make unique list of vertices for indexing purposes
    points = np.unique(coords, axis=0)

    # create empty connectivity array, of vertex indices into the points list
    connectivity = np.zeros((nvoxel*8,), dtype='int16')

    # for each vertex in the orginal array the connectivity of
    # that index is assigned to the index of that vertex in the points
    for vertex_index, _ in enumerate(coords):
        point = coords[vertex_index]
        connectivity[vertex_index] = np.where((points==point).all(axis=1))[0]

    # convert connectivity to array of length nvoxel in which each entry
    # is an array of eight indices into the points array; the eight points
    # represent the eight corners of the voxel
    cells = np.resize(connectivity, (nvoxel,8))

    return points, cells

def make_tet_connectivity(nvoxel, cells, alternate):
    """
    convert voxel connectivity to tetrohedron connectivity
    Args:
        nvoxel (int): number of voxels
        cells (int numpy.ndarray): nvoxel by 8 array listing indices of
                                    vertices in points for each voxel
        alternate (int numpy.ndarray): indexed by voxel number, zero if voxel is
                                        odd else voxel is even
    Returns:
        tet_array (int np.ndarray): 2D number of tets by four, the entry for each tet
                                    is a list of its four vertices in the points array
    """
    tet_array = np.zeros((nvoxel*5,4), dtype='int16') #tet array for .ele

    #iterate over cubes and convert to tets
    for i, cube in enumerate(cells):
        if alternate[i] == 0:
            connectivity_one_vox = even_cube_tets(cube)
        elif alternate[i] == 1:
            connectivity_one_vox = odd_cube_tets(cube)

        for tet_index, con_one_tet in enumerate(connectivity_one_vox):
            tet_array[(i*5)+tet_index] = con_one_tet

    return tet_array

def make_vtk_cell_connectivity(tet_array, cell_count):
    """
    setup and use vtk writer
    Args:
        tet_array (int np.ndarray): 2D number of tets by four, the entry for each tet
                                    is a list of its four vertices in the points array
        cell_count (int): the number of voxels
    Returns:
        (vtk.vtkCellArray): array holding the tet's connectivity as vtk data
    """
    #create vtk array for holding cells
    cells_con = vtk.vtkCellArray()

    # add tetrahedron cells to array
    for i in range(cell_count):
        for tet in range(5):
            tet_con = tet_array[(i*5) + tet]

            tetra = vtk.vtkTetra()
            tetra.GetPointIds().SetId(0, tet_con[0])
            tetra.GetPointIds().SetId(1, tet_con[1])
            tetra.GetPointIds().SetId(2, tet_con[2])
            tetra.GetPointIds().SetId(3, tet_con[3])

            cells_con.InsertNextCell(tetra) #add tet data to vtk cell array

    return cells_con