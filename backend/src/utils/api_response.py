from typing import Any, Optional, Tuple, Dict

class ApiResponse:
    @staticmethod
    def success(data: Any = None, message: str = "OK", status_code: int = 200) -> Tuple[Dict, int]:
        return {"success": True, "message": message, "data": data}, status_code

    @staticmethod
    def error(message: str = "Error", status_code: int = 400, data: Any = None) -> Tuple[Dict, int]:
        return {"success": False, "message": message, "data": data}, status_code
