"""
output a tetrahedron mesh in VTK format (https://vtk.org/)

-----------------------------------------

Licensed under the GNU General Public License, Version 3.0 (the "License"); you
may not use this file except in compliance with the License. You may obtain a
copy of the License at <https://www.gnu.org/licenses/gpl-3.0.html>.

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

This work was funded by Joanna Leng's EPSRC funded RSE Fellowship (EP/R025819/1)

@copyright 2023
@author: j.h.pickering@leeds.ac.uk and j.leng@leeds.ac.uk
"""
# set up linting
# pylint: disable = import-error
# the following avoids problem with vtk's c++
# pylint: disable = no-member
# pylint: disable = no-name-in-module
import vtk.util.numpy_support

def vtk_output(grid, output_file):
    """
    Setup and use vtk writer.
    Args:
        grid (vtk.vtkUnstructuredGrid): vtk scene
        output_file (pathlib.Path)
    """
    writer = vtk.vtkUnstructuredGridWriter()
    writer.SetFileName(str(output_file.with_suffix(".vtk")))
    writer.SetInputData(grid)
    writer.Update()
    writer.Write()
