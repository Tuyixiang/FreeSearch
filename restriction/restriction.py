"""Advanced Search Restrictions"""

from __future__ import annotations
from typing import *
from pprint import PrettyPrinter
import re


class GeneralRestriction:
    """
    General advanced search restriction with multi-select and include-exclude options.
    Allows '-' operator to indicate exclusion and various binary operations.
    """
    include: Set[str]
    exclude: Set[str]

    def __init__(self, include: Union[str, List[str], Set[str]] = None, exclude: Union[List[str], Set[str]] = None):
        """Construct a restriction with an inclusion, or with two sets."""
        if isinstance(include, str):
            self.include = {include}
        else:
            self.include = set(include or [])
        self.exclude = set(exclude or [])
        # remove conflicts
        self.include, self.exclude = self.include - self.exclude, self.exclude - self.include

    def __add__(self, other: GeneralRestriction) -> GeneralRestriction:
        """Add two restrictions together."""
        return GeneralRestriction(self.include | other.include, self.exclude | other.exclude)

    def __sub__(self, other: GeneralRestriction) -> GeneralRestriction:
        """Add the reverse of second restriction."""
        return self + -other

    def __neg__(self) -> GeneralRestriction:
        """Reverse restriction."""
        return GeneralRestriction(self.exclude, self.include)

    def __and__(self, other: GeneralRestriction) -> GeneralRestriction:
        """Strict intersection of two restrictions."""
        return GeneralRestriction(self.include & other.include, self.exclude | other.exclude)

    def __or__(self, other: GeneralRestriction) -> GeneralRestriction:
        """Conjunction of two restrictions."""
        return GeneralRestriction(self.include | other.include, self.exclude & other.exclude)

    def __bool__(self) -> bool:
        """Whether there are any restrictions."""
        return bool(self.include or self.exclude)

    def __str__(self) -> str:
        """Convert to str representation."""
        return '%s {\n\t\'include\': %s,\n\t\'exclude\': %s\n}' % (
            type(self).__name__,
            re.sub('\n', '\n\t           ', PrettyPrinter().pformat(list(self.include))),
            re.sub('\n', '\n\t           ', PrettyPrinter().pformat(list(self.exclude))),
        )

    def __repr__(self) -> str:
        """Same representations as __str__."""
        return self.__str__()


class Term(GeneralRestriction):
    """Represent terms to search or to exclude"""
    pass


class Site(GeneralRestriction):
    """Represent sites to search or to exclude"""
    pass
