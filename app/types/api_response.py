from typing import TypedDict,  Dict, Any, List, Union
class APIResponse(TypedDict, total=False):
    success: bool
    status: str
    message: str
    data: Union[Dict[str, Any], List[Dict[str, Any]], None]   
    error: Union[Dict[str, Any], None]
    meta: Union[Dict[str, Any], None]
