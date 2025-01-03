from typing import Any
from internals.variable_types.smol_variable_type import SmolVariableType

class ISmolNativeCallable(SmolVariableType):

    def __init__(self):
        super().__init__()

    def getValue(self) -> Any:
        raise RuntimeError("Should not be called on base class")

    def setProp(self, name:str, value:Any) -> None:  
        raise RuntimeError("Should not be called on base class")

    def getProp(self, name:str) -> SmolVariableType:
        raise RuntimeError("Should not be called on base class")
    
    def nativeCall(self, funcName:str, parameters:list[SmolVariableType]) -> SmolVariableType:
        raise RuntimeError("Should not be called on base class")
