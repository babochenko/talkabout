# talkabout

[![PyPI version](https://badge.fury.io/py/talkabout.svg)](https://badge.fury.io/py/talkabout)

_(inspired by [https://github.com/awwaiid/gremllm](https://github.com/awwaiid/gremllm))_

Ask anything about any Python object using natural language and get Python code executed automatically. Passes the object's `repr()` and your query to Claude API

## Installation

```bash
pip install talkabout
```

## Setup

You'll need an Anthropic API key. Set it as an environment variable:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Or pass it directly when creating a Talk instance:

```python
from talkabout import Talk
talk = Talk(my_object, api_key="your-api-key-here")
```

## Usage

A simple example:

```python
import numpy as np
from talkabout import Talk

x = np.random.uniform(size=50)

talk = Talk(x)
talk('90th percentile')
```

Prints:
```
Executing code: np.percentile(obj, 90)
```

Returns:
```python
np.float64(0.8442100946036629)
```

## Dry mode
You can also do a dry run, which prints out the code without executing it:

```python
talk.dry('90th percentile')
```

Returns a string:
```
'np.percentile(obj, 90)'
```

## Chat without running code
The .chat() method just asks a question and returns a textual response:

```python
import torch
from talkabout import Talk

optimizer = torch.optim.Adam([torch.Tensor([0.0])], lr=0.001)
talk = Talk(optimizer)
talk.chat('is this the best optimiser ever?')
```

Returns a string:
```
'Let me help you evaluate the Adam optimizer:\n\nAdam is generally considered ...'
```

## External libraries support
A more complicated example - inspect financials of a company using Yahoo Finance API (this use-case actually motivated this package, because those yfinance dataframes are messy):

```python
import yfinance as yf
from talkabout import Talk

pypl = yf.Ticker('PYPL')

talk = Talk(pypl)
talk('qoq Oper CF over debt; use .loc')
```

Prints:
```
Executing code: pypl.quarterly_cash_flow.loc['Operating Cash Flow'].pct_change() / pypl.quarterly_balancesheet.loc['Total Debt']
```

Returns a `pandas.Series`:
```
2025-03-31             NaN
2024-12-31    1.076823e-10
2024-09-30   -3.265984e-11
2024-06-30   -5.669014e-12
2024-03-31    2.654644e-11
2023-12-31             NaN
dtype: float64
```

