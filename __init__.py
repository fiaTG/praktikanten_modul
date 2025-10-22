import importlib.util

if importlib.util.find_spec("odoo") is not None:
    from . import models  # type: ignore[misc]
    from . import controllers  # type: ignore[misc]
