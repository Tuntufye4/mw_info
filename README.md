# mw_info

A Python library to access structured data about Malawi’s districts, currency exchange rates, and 
agriculture (crops and fish species).

---

## Features

- Query detailed district information (population, geography, climate, languages, etc.)
- Currency conversion based on Malawi Kwacha with multiple foreign currencies
- Query agricultural data by Chichewa, English, or scientific names for crops and fish species

---

## Installation

Clone the repository or download the source files.

```bash
git clone https://github.com/yourusername/mw_info.git
cd mw_info
pip install -r requirements.txt  # if you add dependencies like PyYAML
```

## Usage

## DistrictInfo Class, Methods & Examples

### get_all_districts()

```
districts = DistrictInfo()
all_districts = districts.get_all_districts()
print(all_districts)
# Output: ['Lilongwe', 'Blantyre', 'Machinga', ...]

```

### get_district_info(district_name, fields=None)

```
districts = DistrictInfo()

#### Full info for Lilongwe
info = districts.get_district_info("Lilongwe")
print(info)

#### Selected fields only
selected = districts.get_district_info("Mangochi", fields=["population_2023", "languages", "climate"])
print(selected)

```

### filter_by_region(region_name)

Returns list of district dictionaries for districts in a given region.

```
districts = DistrictInfo()
southern_districts = districts.filter_by_region("Southern")
for d in southern_districts:
    print(d["district"])
### Outputs districts in Southern region
```

### get_all_district_data()

Returns the full raw list of all district dictionaries.

```
districts = DistrictInfo()
all_data = districts.get_all_district_data()
print(all_data[0])  # Print first district data

```

## CurrencyConverter Class, Methods & Examples

### available_currencies()

Returns list of supported currency codes.

```
print(currency.available_currencies())
 Example output: ['USD', 'EUR', 'ZAR', 'GBP', 'KES', ...]

```

### convert_from_base(amount, to_currency)

Convert amount from MWK (base currency) to another currency.

```
mwk_amount = 10000
usd_amount = currency.convert_from_base(mwk_amount, "USD")
print(f"{mwk_amount} MWK is approximately {usd_amount} USD")

```

### convert_to_base(amount, from_currency)

Convert amount from another currency to MWK.

```
usd_amount = 100
mwk_amount = currency.convert_to_base(usd_amount, "USD")
print(f"{usd_amount} USD is approximately {mwk_amount} MWK")

```

## AgriInfoMw Class Methods

from agriculture_info import AgricultureInfoMW

agri = AgricultureInfoMW()

### Query crop or fish info by any name (Chichewa, English, or Scientific)

```
crop = agri.query_info("Chimanga")
print(crop)

fish = agri.query_info("Oreochromis shiranus")
print(fish)
```

### Query by English name

```
crop2 = agri.query_info("Maize")
print(crop2)

```
### List all crops

```
all_crops = agri.list_all_crops()
print(all_crops)

```

### List all fish species

```
all_fish = agri.list_all_fish()
print(all_fish)

```
## License

This project is licensed under the MIT License

## Maintainer

Tuntufye Mwanyongo
