"""Khutbah: Quranic quotation detection and annotation."""

from khutbah.matcher import Matcher, Quotation  # Ajuste os imports conforme os arquivos reais do repo
from khutbah.api import find, annotate          # Ou de onde essas funções estiverem definidas

__all__ = [
    "Matcher",
    "Quotation",
    "find",
    "annotate",
]