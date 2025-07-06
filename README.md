Executes arbitrary queries against any object. Uses ChatGPT under the hood. Requires either an `api_key` param or an `OPENAI_API_KEY` env var

Simple example:

```python
[ins] In [1]: from talkabout import Talk

[ins] In [2]: Talk(3)('+ 1')
Returned code: obj + 1

Out[2]: 4
```

A more complicated example:

```python
[ins] In [3]: import yfinance as yf

[ins] In [4]: pypl = yf.Ticker('PYPL')

[ins] In [5]: from talkabout import Talk

[ins] In [6]: Talk(pypl)('qoq Oper CF over debt')
Returned code: pypl.quarterly_cash_flow.loc['Operating Cash Flow'].pct_change() / pypl.quarterly_balancesheet.loc['Total Debt']

Out[6]:
2025-03-31             NaN
2024-12-31    1.076823e-10
2024-09-30   -3.265984e-11
2024-06-30   -5.669014e-12
2024-03-31    2.654644e-11
2023-12-31             NaN
dtype: float64
```

