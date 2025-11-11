import os
import yaml

class HealthInfoMW:
    def __init__(self, yaml_path=None):
        if yaml_path is None:
            yaml_path = os.path.join(os.path.dirname(__file__), "data/health_data.yml")
        with open(yaml_path, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f).get("health", [])

    def get_all_districts(self):   
        return [d["district"] for d in self.data]   

    def get_district_health(self, name, fields=None):
        name = name.strip().lower()
        for district in self.data:
            if district["district"].lower() == name:
                if fields is None:
                    return district   
                return {field: district.get(field, "N/A") for field in fields}
        return None
    

    def get_region_health(self, name, fields=None):
        name = name.strip().lower()
        for region in self.data:
            if region["region"].lower() == name:
                if fields is None:
                    return region
                return {field: region.get(field, "N/A") for field in fields}
            return None
        

    def filter_by_facility_count(self, facility_type, threshold):
        """
        Example: filter_by_facility_count("hospitals", 3)
        """
        facility_type = facility_type.lower()
        return [
            d for d in self.data
            if d.get(facility_type, 0) >= threshold
        ]

    def get_all_health_data(self):
        return self.data
    
    
    def get_dispensaries(self, name):
        d = self._find_district(name)   
        return d.get("dispensaries") if d else None 

    def get_dispensaries_reg(self, name):
        d = self._find_region(name)   
        return d.get("dispensaries") if d else None 
    
    
    def get_hospitals(self, name):
        d = self._find_district(name)   
        return d.get("hospitals") if d else None 
    
    def get_hospitals_reg(self, name):   
        d = self._find_region(name)   
        return d.get("hospitals") if d else None 
    
    
    def get_health_posts(self, name):
        d = self._find_district(name)   
        return d.get("health_posts") if d else None 
    
    def get_health_posts_reg(self, name):
        d = self._find_region(name)   
        return d.get("health_posts") if d else None    
    
         
    def get_health_centers(self, name):
        d = self._find_district(name)   
        return d.get("health_centers") if d else None 
    
    def get_health_centers_reg(self, name):
        d = self._find_region(name)
        return d.get("health_centers") if d else None 

    def get_Govt_hospital(self, name):
        d = self._find_district(name)
        return d.get("Govt_hospitals") if d else None

    
    def get_Govt_hospital_reg(self, name):
        d = self._find_region(name)
        return d.get("Govt_hospitals") if d else None 
    
    def _find_district(self, name):
        name = name.strip().lower()
        return next((d for d in self.data if d["district"].lower() == name), None)
    
    def _find_region(self, name):
        name = name.strip().lower()
        return next((d for d in self.data if d["region"].lower() == name), None)