# IBKR Private Data Connector

Mira can read from a local Interactive Brokers Gateway or TWS API session as a
private, authorized data source. The connector is read-only: it does not place,
modify, or cancel orders.

## Privacy Boundary

Keep the following out of tracked files:

- account ids
- positions, cost basis, balances, margin values, and order data
- entitlement details
- raw broker exports

Use `private/mira-data.env` or environment variables for local settings. Use
`private/ibkr/` and `private/portfolio/` for emitted artifacts. The public
repository may include connector code, schemas, templates, and sanitized
examples only.

## Local Configuration

Copy `templates/mira-data-config.example` to `private/mira-data.env` and set the
IBKR fields:

```text
MIRA_IBKR_HOST=127.0.0.1
MIRA_IBKR_PORT=4002
MIRA_IBKR_CLIENT_ID=19
MIRA_IBKR_ACCOUNT=
MIRA_IBKR_READONLY=1
MIRA_IBKR_MARKET_DATA_TYPE=3
```

Typical API ports:

| Session | Port |
| --- | --- |
| TWS live | `7496` |
| TWS paper | `7497` |
| IB Gateway live | `4001` |
| IB Gateway paper | `4002` |

## Commands

List accounts, masked by default:

```sh
PYTHONPATH=tools python -m mira_data ibkr accounts
```

Fetch a private market snapshot bundle:

```sh
PYTHONPATH=tools python -m mira_data fetch ibkr_market_price AAPL --out private/ibkr/AAPL
```

Fetch historical bars:

```sh
PYTHONPATH=tools python -m mira_data fetch ibkr_historical_bars AAPL --out private/ibkr/AAPL-bars
```

Fetch account summary for the default account:

```sh
PYTHONPATH=tools python -m mira_data fetch ibkr_account_summary --out private/ibkr/account-summary
```

Fetch positions for the default account:

```sh
PYTHONPATH=tools python -m mira_data fetch ibkr_positions --out private/ibkr/positions
```

Write a private position snapshot CSV for portfolio review intake:

```sh
PYTHONPATH=tools python -m mira_data ibkr position-snapshot --out private/portfolio
```

## Research Use

IBKR data can support:

- live or delayed market-pricing context
- private position review
- portfolio exposure review
- margin, cash, and liquidity context
- option and instrument workflows when extended with chain/Greek data

It should not be used as an autonomous execution path. Mira outputs remain
research support and must preserve the usual evidence, freshness, and
actionability boundaries.
