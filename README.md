# mw_info

A Python library providing detailed information about Malawi’s districts along with currency conversion based on Malawi Kwacha (MWK).

---

## Features

- Retrieve detailed info on all 28 districts of Malawi  
- Query district data by district name or region  
- Get specific fields like population, climate, languages, elevation, etc.  
- Convert MWK to multiple foreign currencies and vice versa using exchange rates loaded from YAML  
- Easy to extend with updated district or currency data

---

## Installation

Clone the repository or download the source files.

```bash
git clone https://github.com/yourusername/mw_info.git
cd mw_info
pip install -r requirements.txt  # if you add dependencies like PyYAML
```

## Usage

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

