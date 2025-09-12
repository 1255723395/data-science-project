import datetime
import hashlib

def generate_id(data):
    """Generate unique ID for data item"""
    timestamp = datetime.datetime.now().isoformat()
    combined = f"{data}_{timestamp}"
    return hashlib.md5(combined.encode()).hexdigest()

def format_timestamp(ts):
    """Format timestamp for display"""
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

# bug fix - handle timezone issues
def safe_parse_date(date_string):
    try:
        return datetime.datetime.fromisoformat(date_string.replace('Z', '+00:00'))
    except:
        return datetime.datetime.now()

def calculate_metrics(values):
    """Calculate basic statistical metrics"""
    if not values:
        return {"mean": 0, "std": 0, "count": 0}
    
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    
    return {
        "mean": mean_val,
        "std": variance ** 0.5,
        "count": len(values),
        "min": min(values),
        "max": max(values)
    }