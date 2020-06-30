from typing import *
import httpx
from ..restriction.restriction import Term, Site, GeneralRestriction
from ..restriction.country import Country
from ..restriction.language import Language
from .country import COUNTRY_IDENT
from .. import results
from ..api_keys import GOOGLE_API_KEY, GOOGLE_CUSTOM_ID
import json
import math
import copy
import asyncio


async def google_search(result_count: int = 10, **kwargs) -> List[results.SearchResult]:
    """Returns list of objects. May throw ConnectionError."""
    requests = []
    params = build_params(**kwargs)
    for i in range(math.ceil(result_count / 10)):
        params_clone = copy.deepcopy(params)
        params_clone['start'] = i * 10 + 1
        requests.append(single_request(params_clone))
    return [entry for result in await asyncio.gather(*requests) for entry in result]


async def single_request(params: dict) -> List[results.SearchResult]:
    """Send search request and retrieve result list. May throw ConnectionError."""
    try:
        # Send request to Google Custom Search API
        async with httpx.AsyncClient() as client:
            response = await client.get('https://customsearch.googleapis.com/customsearch/v1', params=params)
    except ConnectionError:
        # Timeout or internet unreachable
        raise results.ConnectionFailure()
    # Check HTTP status
    if response.status_code != 200:
        raise results.ConnectionFailure(response.status_code)
    # Check response validity
    try:
        response_object = json.loads(response.text)
    except json.JSONDecodeError:
        raise results.APIFailure('Response is not JSON', response.text)
    if not isinstance(response_object, dict):
        raise results.APIFailure('Response is not dict', response_object)
    if 'error' in response_object:
        raise results.APIFailure(response_object.get('message', 'Error received'), response_object)
    # Parse result
    search_results = []
    for item in response_object.get('items', []):
        if not isinstance(item, dict) or not all(field in item for field in ['title', 'link']):
            continue
        search_results.append(results.SearchResult(
            item['title'], item['link'], item.get('snippet')
        ))
    return search_results


def warn(argument: str, value: Any, message: str):
    """Print argument incompatibilities"""
    results.incompatible_argument('Google', **locals())


def format_restriction(restriction: GeneralRestriction, mapping: Dict[str, str]) -> str:
    """Format restrictions using Google boolean expression"""
    assert restriction
    if restriction.include:
        return '.'.join(
            ['(%s)' % '|'.join(mapping[i] for i in restriction.include)] +
            ['(-%s)' % mapping[e] for e in restriction.exclude]
        )
    else:
        return '.'.join('(-%s)' % mapping[e] for e in restriction.exclude)


def build_params(
        keyword: Union[str, List[str]] = None,
        strict_terms: Union[str, List[str], Term] = None,
        multiple_choice_terms: Union[List[str], Term] = None,
        date_range: int = None,
        page_number: int = 0,
        site: Union[str, List[str], Site] = None,
        country: Country = None,
        language: Language = None,
        file_type: str = None,
        mix_simplified_traditional_chinese: bool = True,
        safe_search: bool = False,
) -> dict:
    params = {}
    if keyword:
        if isinstance(keyword, str):
            params['q'] = keyword
        else:
            params['q'] = ' '.join(keyword)
    if strict_terms:
        if isinstance(strict_terms, str):
            params['exactTerms'] = strict_terms
        elif isinstance(strict_terms, list):
            params['exactTerms'] = ' '.join(strict_terms)
        else:
            params['exactTerms'] = ' '.join(strict_terms.include)
            params['excludeTerms'] = ' '.join(strict_terms.exclude)
    if multiple_choice_terms:
        if isinstance(multiple_choice_terms, list):
            params['orTerms'] = ' '.join(multiple_choice_terms)
        else:
            params['orTerms'] = ' '.join(multiple_choice_terms.include)
            if multiple_choice_terms.exclude:
                warn('multiple_choice_terms', multiple_choice_terms, 'Exclude terms are ignored.')
    if date_range:
        params['dateRestrict'] = 'd%d' % date_range
    if page_number > 0:
        params['start'] = 1 + page_number * 10
    if site:
        if isinstance(site, str):
            params['siteSearch'] = site
            params['siteSearchFilter'] = 'i'
        elif isinstance(site, list):
            params['siteSearch'] = site[0]
            params['siteSearchFilter'] = 'i'
            if len(site) > 1:
                warn('site', site, 'Cannot specify more than one sites. Only the first is used.')
        else:
            if site.include:
                params['siteSearch'] = next(iter(site.include))
                params['siteSearchFilter'] = 'i'
                if len(site.include) > 1:
                    warn('site', site, 'Cannot specify more than one sites. Only the first is used.')
                if site.exclude:
                    warn('site', site, 'Does not support both include and exclude sites. Only include site is used')
            elif site.exclude:
                params['siteSearch'] = next(iter(site.exclude))
                params['siteSearchFilter'] = 'e'
                if len(site.exclude) > 1:
                    warn('site', site, 'Cannot specify more than one sites. Only the first is used.')
    if country:
        params['cr'] = format_restriction(country, COUNTRY_IDENT)
    if language:
        """unimplemented"""
    if file_type:
        """unimplemented"""
    params['c2coff'] = '0' if mix_simplified_traditional_chinese else '1'
    params['safe'] = 'active' if safe_search else 'off'
    params['key'] = GOOGLE_API_KEY
    params['cx'] = GOOGLE_CUSTOM_ID
    return params
