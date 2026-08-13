# Copyright 2026 Adobe. All rights reserved.
# This file is licensed to you under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy
# of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS
# OF ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

from __future__ import annotations

import pytest

from json_formula import JsonFormula


@pytest.fixture
def engine() -> JsonFormula:
    return JsonFormula()


def test_datedif_yd_leap_year(engine: JsonFormula) -> None:
    # date1 is in non-leap year (2023), date2 is Feb 29 in leap year (2024) -> 59 days
    assert engine.search('datedif(datetime(2023, 1, 1), datetime(2024, 2, 29), "yd")', {}) == 59

    # date1 is in leap year (2020-04-15), date2 is Feb 29 in leap year (2024) -> 320 days
    assert engine.search('datedif(datetime(2020, 4, 15), datetime(2024, 2, 29), "yd")', {}) == 320

    # date1 is Feb 29 (2024), date2 is Jan 1 in non-leap year (2025) -> 307 days
    assert engine.search('datedif(datetime(2024, 2, 29), datetime(2025, 1, 1), "yd")', {}) == 307

    # date1 is Feb 29 (2020), date2 is Feb 29 (2024) -> 0 days
    assert engine.search('datedif(datetime(2020, 2, 29), datetime(2024, 2, 29), "yd")', {}) == 0

    # date1 is Feb 29 (2024), date2 is Mar 1 (2024) -> 1 day
    assert engine.search('datedif(datetime(2024, 2, 29), datetime(2024, 3, 1), "yd")', {}) == 1

    # date1 is Feb 28 in non-leap year (2023), date2 is Feb 29 in leap year (2024) -> 1 day
    assert engine.search('datedif(datetime(2023, 2, 28), datetime(2024, 2, 29), "yd")', {}) == 1
