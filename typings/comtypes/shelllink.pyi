from ctypes import *

from _typeshed import Incomplete
from comtypes import (
    COMMETHOD as COMMETHOD,
    GUID as GUID,
    HRESULT as HRESULT,
    CoClass as CoClass,
    IUnknown as IUnknown,
)

SLGP_SHORTPATH: int
SLGP_UNCPRIORITY: int
SLGP_RAWPATH: int
ITEMIDLIST = c_int
LPITEMIDLIST: Incomplete
LPCITEMIDLIST: Incomplete

class IShellLinkA(IUnknown):
    def GetPath(self, flags=...): ...
    def GetDescription(self): ...
    def GetWorkingDirectory(self): ...
    def GetArguments(self): ...
    def GetIconLocation(self): ...

class IShellLinkW(IUnknown):
    def GetPath(self, flags=...): ...
    def GetDescription(self): ...
    def GetWorkingDirectory(self): ...
    def GetArguments(self): ...
    def GetIconLocation(self): ...

class ShellLink(CoClass): ...
