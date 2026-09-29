from __future__ import annotations

import sys
from pathlib import Path

QA_ROOT = Path(__file__).parents[1]
if str(QA_ROOT) not in sys.path:
    sys.path.insert(0, str(QA_ROOT))
