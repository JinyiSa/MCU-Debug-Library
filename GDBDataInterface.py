import gdb

class UnacceptableTypeException(Exception):
    pass

class GDBDataExtractor():
    def __init__(self, variableName: str) -> None:
        self.variableName = variableName
    
    def __call__(self):
        buffer = gdb.parse_and_eval(self.variableName)
        if buffer.type.code != gdb.TYPE_CODE_ARRAY:
            raise UnacceptableTypeException(f"{self.variableName} is not an array")
        valueArray = []
        gdbOutputString = buffer.format_string(max_elements=0, max_depth=-1)
        splitArray = gdbOutputString.split(',')
        for string in splitArray:
            leftIndex = string.find('{')
            rightIndex = string.find('}')
            if leftIndex == -1 and rightIndex == -1:
                try:
                    valueArray.append(float(string))
                except ValueError:
                    raise UnacceptableTypeException(f"Unable to interrupt {self.variableName} as an value array")
            elif leftIndex == -1 and rightIndex != -1:
                try:
                    valueArray.append(float(string[:rightIndex]))
                except ValueError:
                    raise UnacceptableTypeException(f"Unable to interrupt {self.variableName} as an value array")
            else:
                try:
                    valueArray.append(float(string[leftIndex+1:-1]))
                except ValueError:
                    raise UnacceptableTypeException(f"Unable to interrupt {self.variableName} as an value array")
        return valueArray
