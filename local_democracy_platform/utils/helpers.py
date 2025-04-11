# utils/helpers.py
from typing import Dict, List

def paginate(data: List, page: int = 1, size: int = 10) -> Dict:
    start = (page - 1) * size
    end = start + size
    return {
        "page": page,
        "size": size,
        "total": len(data),
        "items": data[start:end]
    }
