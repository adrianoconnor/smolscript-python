from typing import Any
from internals.variable_types.smol_variable_type import SmolVariable

class ISmolNativeCallable(SmolVariable):

    def __init__(self):
        super().__init__()

    def getValue(self) -> Any:
        raise RuntimeError("Should not be called on base class")

    def setProp(name:str, value:Any) -> None:  
        raise RuntimeError("Should not be called on base class")

    def getProp(name:str) -> SmolVariable:
        raise RuntimeError("Should not be called on base class")
    
    def nativeCall(funcName:str, parameters:list[SmolVariable]) -> SmolVariable:
        raise RuntimeError("Should not be called on base class")
