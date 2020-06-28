"""Unified Search Entry"""

from __future__ import annotations
from typing import *
from .restriction.country import Country
from .restriction.language import Language
from .restriction.restriction import Term, Site
from .google.search import google_search
from . import results


async def search(
        keyword: Union[str, List[str]] = None,
        strict_terms: Union[str, List[str], Term] = None,
        multiple_choice_terms: Union[List[str], Term] = None,
        date_range: int = None,
        result_count: int = 20,
        site: Union[str, List[str], Site] = None,
        country: Country = None,
        language: Language = None,
        file_type: str = None,
        mix_simplified_traditional_chinese: bool = True,
        safe_search: bool = False,
) -> List[results.SearchResult]:
    return await google_search(**locals())
