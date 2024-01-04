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

 Write tetrohedrons out to tetgen file format.

Authors: Joanna Leng, Jonathan Pickering, Molly Gravett, Jarvellis Rogers - University of Leeds (UK)
"""

def write_ffea_output(output_file, tet_array, points, faces, original_ids, comment=""):
    """
    write the ffea input files
    Args:
        nvoxel (int): number of voxels
        tet_array (int*4 list): for each tet the indices of its vertices in the points list
        points (float np.ndarray): duplicate free list of vertices
        faces (int np.ndarray): connectivity of face polygons
        original_ids (int []): index of surface point in the surface faces's points array
        comment (str): any user comment
    """
    write_ffea_elements(output_file, tet_array, comment)
    write_ffea_nodes(output_file, points, comment)
    write_ffea_faces(output_file, faces, original_ids, comment)

def write_ffea_elements(output_file, tet_array, comment=""):
    """
    write tetgen elements file .ele
    First line: <# of tetrahedra> <nodes per tetrahedron> <# of attributes>
    Remaining lines list of # of tetrahedra:
    <tetrahedron #> <node> <node> <node> <node> ... [attributes]
    Args:
        output_file (pathlib.Path): root name of file, will have .node added
        nvoxel (int): number of voxels
        tet_array ():
        comment (str): any user comment
    """
    with open(output_file.with_suffix(".1.ele"), "w", encoding="utf-8") as ele:
        ele.write(f"{len(tet_array)} 4 0\n")
        for i, tet in enumerate(tet_array):
            ele.write(f"{i+1} {tet[0]+1} {tet[1]+1} {tet[2]+1} {tet[3]+1}\n")
        ele.write(comment)

def write_ffea_nodes(output_file, points, comment=""):
    """
    write ffea .node file
    First line: <num points> <dimension (3)> <num attributes> <num boundary markers (0 or 1)>
    Remaining lines list # of points:
    <point #> <x> <y> <z>
    Args:
        output_file (pathlib.Path): root name of file, will have .node added
        points ():
        comment (str): any user comment
    """
    with open(output_file.with_suffix(".1.node"), "w", encoding="utf-8") as node:
        node.write(f"{len(points)} 3 0 0\n")
        for i, point in enumerate(points):
            node.write(f"{i+1} {point[0]} {point[1]} {point[2]}\n")
        node.write(comment)

def write_ffea_faces(output_file, faces, ids, comment=""):
    """
    write .face file
    First line: <# of faces> <boundary marker (0 or 1)>
    Remaining lines list of # of faces:
    <face #> <node> <node> <node> [boundary marker]
    Args:
        output_file (pathlib.Path): root name of file, will have .face added
        faces (int np.ndarray): connectivity of face polygons
        ids (int []): index of surface point in the surface faces's points array
        comment (str): any user comment
    """
    with open(output_file.with_suffix(".1.face"), "w", encoding="utf-8") as face_file:
        face_file.write(f"{len(faces)} 1\n")
        for i, face in enumerate(faces):
            face_file.write(
                f"{i+1} {ids[face[1]]+1} {ids[face[2]]+1} {ids[face[3]]+1} -1\n")
        face_file.write(comment)
