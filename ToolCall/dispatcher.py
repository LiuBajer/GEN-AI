from tools import sum, uppercase
import json

def execute(functionEx):  # functionEx is now a Function object
    args = json.loads(functionEx.arguments)  # No .function needed
    if functionEx.name == "sum":
        return sum(**args)
    elif functionEx.name == "uppercase":
        return uppercase(**args)