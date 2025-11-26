import requests
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

API_URL = "https://open.er-api.com/v6/latest/"

def get_rates(base_currency):
    url = f"{API_URL}{base_currency.upper()}"
    response = requests.get(url, timeout=8)
    response.raise_for_status()
    data = response.json()

    if data.get("result") != "success":
        raise Exception("Failed to fetch data. Check the currency code or API.")

    return data["rates"], data

def get_rate_and_updated(base_currency, to_currency):
    rates, data = get_rates(base_currency)
    tgt = to_currency.upper()
    if tgt not in rates:
        raise Exception(f"Currency '{to_currency}' not found in API.")
    rate = rates[tgt]

    last_updated_raw = data.get("time_last_update_utc") or data.get("time_last_update_iso")
    last_updated_sgt = None

    if last_updated_raw:
        dt = None
        # try parsing RFC-2822 / HTTP-date
        try:
            dt = parsedate_to_datetime(last_updated_raw)
        except Exception:
            pass
        # fallback to ISO format
        if dt is None:
            try:
                dt = datetime.fromisoformat(last_updated_raw)
            except Exception:
                dt = None

        if dt is not None:
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            sgt = dt.astimezone(timezone(timedelta(hours=8)))
            last_updated_sgt = sgt.strftime("%Y-%m-%d %H:%M:%S SGT")
        else:
            # keep original raw string if parsing fails
            last_updated_sgt = last_updated_raw
    else:
        unix_ts = data.get("time_last_update_unix")
        if unix_ts:
            dt = datetime.fromtimestamp(int(unix_ts), tz=timezone.utc)
            sgt = dt.astimezone(timezone(timedelta(hours=8)))
            last_updated_sgt = sgt.strftime("%Y-%m-%d %H:%M:%S SGT")

    return rate, last_updated_sgt

def convert_currency(amount, from_currency, to_currency):
    rate, last_updated = get_rate_and_updated(from_currency, to_currency)
    return amount * rate, rate, last_updated


print("WELCOME TO CURRENCY CONVERTER\n")
print("This converter supports ALL currencies.")
print("Example of currency code: SGD, INR, USD, EUR, GBP, JPY, etc.")
print("Convert amount from one currency to another using live rates.\n")

try:
    amount = float(input("Enter amount: "))
    from_currency = input("Convert currency code FROM (NOT Caps sensitive): ").upper()
    to_currency = input("Convert currency code TO (NOT Caps sensitive): ").upper()

    result, rate, last_updated = convert_currency(amount, from_currency, to_currency)
    print(f"\n{amount} {from_currency} = {round(result, 2)} {to_currency}\n")
    print(f"Exchange rate: 1 {from_currency} = {rate} {to_currency}")
    if last_updated:
        print(f"Last updated: {last_updated}\n")
    else:
        print("Last updated: (timestamp not provided)\n")

except Exception as e:
    print("Error:", e)
