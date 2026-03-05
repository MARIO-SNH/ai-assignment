import csv
from dataclasses import dataclass
from typing import List, Tuple, Dict

# NOTE:
# Breakpoints differ by country/standard. For assignment: okay if you document your chosen breakpoints.
# These are common US AQI breakpoints for PM2.5 and PM10.

@dataclass(frozen=True)
class BP:
    aqi_lo: int
    aqi_hi: int
    c_lo: float
    c_hi: float
    category: str

PM25: List[BP] = [
    BP(0,   50,   0.0,  12.0,  "Good"),
    BP(51,  100,  12.1, 35.4,  "Moderate"),
    BP(101, 150,  35.5, 55.4,  "Unhealthy for Sensitive Groups"),
    BP(151, 200,  55.5, 150.4, "Unhealthy"),
    BP(201, 300,  150.5, 250.4,"Very Unhealthy"),
    BP(301, 500,  250.5, 500.4,"Hazardous"),
]

PM10: List[BP] = [
    BP(0,   50,   0,   54,   "Good"),
    BP(51,  100,  55,  154,  "Moderate"),
    BP(101, 150,  155, 254,  "Unhealthy for Sensitive Groups"),
    BP(151, 200,  255, 354,  "Unhealthy"),
    BP(201, 300,  355, 424,  "Very Unhealthy"),
    BP(301, 500,  425, 604,  "Hazardous"),
]

def lin_aqi(c: float, bp: BP) -> int:
    # AQI formula: I = (Ihi-Ilo)/(Ch-Cl)*(C-Cl)+Ilo
    return round(((bp.aqi_hi - bp.aqi_lo) / (bp.c_hi - bp.c_lo)) * (c - bp.c_lo) + bp.aqi_lo)

def sub_index(c: float, table: List[BP]) -> Tuple[int, str]:
    for bp in table:
        if bp.c_lo <= c <= bp.c_hi:
            return lin_aqi(c, bp), bp.category
    # out-of-range fallback
    if c < table[0].c_lo:
        return table[0].aqi_lo, table[0].category
    return table[-1].aqi_hi, table[-1].category

def overall_aqi(pm25: float, pm10: float) -> Dict[str, object]:
    i25, cat25 = sub_index(pm25, PM25)
    i10, cat10 = sub_index(pm10, PM10)

    # Simple reflex rule: overall AQI = max(sub-indexes)
    if i25 >= i10:
        return {"aqi": i25, "category": cat25, "dominant": "PM2.5"}
    return {"aqi": i10, "category": cat10, "dominant": "PM10"}

def read_latest_row(path: str) -> Dict[str, str]:
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            rows.append(row)
    if not rows:
        raise ValueError("Sensor file has no rows.")
    return rows[-1]

def main():
    import argparse
    p = argparse.ArgumentParser(description="Simple Reflex AQI Agent (reads sensor CSV)")
    p.add_argument("--file", required=True, help="CSV with columns: timestamp, pm25, pm10")
    args = p.parse_args()

    latest = read_latest_row(args.file)
    pm25 = float(latest["pm25"])
    pm10 = float(latest["pm10"])

    result = overall_aqi(pm25, pm10)

    print("=== AQI REFLEX AGENT ===")
    print(f"Timestamp: {latest.get('timestamp', 'N/A')}")
    print(f"PM2.5: {pm25} ug/m3 | PM10: {pm10} ug/m3")
    print(f"Overall AQI: {result['aqi']}")
    print(f"Category: {result['category']}")
    print(f"Dominant pollutant: {result['dominant']}")

if __name__ == "__main__":
    main()