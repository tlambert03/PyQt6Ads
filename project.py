import os
from pathlib import Path
import subprocess

from pyqtbuild import PyQtBindings, PyQtProject

ROOT = Path(__file__).parent


class PyQt6Ads(PyQtProject):
    def __init__(self):
        super().__init__()
        # self.dunder_init = True
        self.bindings_factories = [QtAds]

    # def setup(self, pyproject, tool, tool_description):
    #     super().setup(pyproject, tool, tool_description)
    #     self._gen_bindings = self.builder._generate_bindings
    #     self.builder._generate_bindings = self._generate_bindings

    # def _generate_bindings(self):
    #     self._gen_bindings()
    #     # create an empty file at py_typed_path
    #     with open(os.path.join(self.build_dir, "py.typed"), "w") as f:
    #         pass

    def apply_user_defaults(self, tool):
        if tool == "sdist":
            return super().apply_user_defaults(tool)
        qmake_path = "bin/qmake"
        if os.name == "nt":
            qmake_path += ".exe"
        try:
            qmake_bin = str(next(ROOT.rglob(qmake_path)).absolute())
        except StopIteration:
            raise RuntimeError(
                "qmake not found.\n"
                "Please run `uvx --from aqtinstall aqt install-qt <plat> "
                "desktop <qtversion> <arch> --outputdir Qt`"
            )
        self.builder.qmake = qmake_bin
        return super().apply_user_defaults(tool)

#     def get_dunder_init(self):
#         """Return the contents of the __init__.py file to install."""
#         if self.py_platform != "win32":
#             return "from ._ads import *\n"
#         else:
#             return """
# def find_qt():
#     import os, sys

#     qtcore_dll = '\\\\Qt6Core.dll'

#     dll_dir = os.path.dirname(sys.executable)
#     if not os.path.isfile(dll_dir + qtcore_dll):
#         path = os.environ['PATH']

#         site_pkg = os.path.dirname(os.path.dirname(__file__))
#         dll_dir = site_pkg + 'PyQt6\\\\Qt6\\\\bin'
#         if os.path.isfile(dll_dir + qtcore_dll):
#             path = dll_dir + ';' + path
#             os.environ['PATH'] = path
#         else:
#             for dll_dir in path.split(';'):
#                 if os.path.isfile(dll_dir + qtcore_dll):
#                     break
#             else:
#                 return

#     try:
#         os.add_dll_directory(dll_dir)
#     except AttributeError:
#         pass


# find_qt()
# del find_qt

# from ._ads import *
# """

    def build_wheel(self, wheel_directory):
        # use lowercase name for wheel, for
        # https://packaging.python.org/en/latest/specifications/binary-distribution-format/
        self.name = self.name.lower()
        return super().build_wheel(wheel_directory)




class QtAds(PyQtBindings):
    def __init__(self, project):
        super().__init__(project, "QtAds")

    def apply_user_defaults(self, tool):
        resource_file = os.path.join(
            self.project.root_dir, "Qt-Advanced-Docking-System", "src", "ads.qrc"
        )
        self.builder_settings.append("RESOURCES += " + resource_file)
        super().apply_user_defaults(tool)
