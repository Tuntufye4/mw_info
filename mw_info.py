import os
import yaml

class DistrictInfo:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "data/district_data.yml")
        with open(path, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def get_all_districts(self):
        return [d["district"] for d in self.data.get("districts", [])]  

    def get_district_info(self, name, fields=None):
        name = name.strip().lower()
        for district in self.data.get("districts", []):
            if district["district"].lower() == name:
                if fields is None:
                    return district
                return {field: district.get(field) for field in fields}
        return None

    def filter_by_region(self, region):
        region = region.strip().lower()
        return [
            d for d in self.data.get("districts", [])
            if d.get("region", "").lower() == region
        ]

    def get_all_district_data(self):
        return self.data.get("districts", [])  


     def get_climate(self, name):
        d = self._find_district(name)
        return d.get("climate") if d else None
    
    
    def get_district_type(self, name):
        d = self._find_district(name)
        return d.get("district_type") if d else None
    
    def get_population_density(self, name):
        d = self._find_district(name)   
        return d.get("population_density") if d else None
       
    def get_languages(self, name):
        d = self._find_district(name)
        return d.get("languages") if d else None 
    
    def get_area(self, name):
        d = self._find_district(name)
        return d.get("area_km2") if d else None
    

    def _find_district(self, name):
        name = name.strip().lower()
        return next((d for d in self.data if d["district"].lower() == name), None)

