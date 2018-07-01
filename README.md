# [Python EOS][docs]

[![pypi-version]][pypi]

**`python-eos` is robust, high-level Python interface to EOS blockchain.**

Full documentation for the project is available at [https://python-eos.readthedocs.io/en/latest/][docs].
This library currently works on Python 3.7.

---

## Installation

Install using `pip`...
```
pip install python-eos
```

## Examples

```
import eos

for transfer_action in eos.Client().stream_actions_from_account('eosio.token', filter_by='transfer'):
    transfer_data = transfer_action['action_trace']['act']['data']
    print('Transfer "{}" from "{}" to "{}".')
```


[pypi-version]: https://img.shields.io/pypi/v/python-eos.svg
[pypi]: https://pypi.org/project/python-eos/
[docs]: https://python-eos.readthedocs.io/en/latest/
