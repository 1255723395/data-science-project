import json
import os

class DataProcessor:
    def __init__(self, config_path="config.json"):
        self.config = self.load_config(config_path)
        
    def load_config(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                return json.load(f)
        return {"default": True}
        
    def process_batch(self, data_list):
        """Process a batch of data items"""
        results = []
        for item in data_list:
            # Fix memory leak issue
            processed = self.transform_item(item)
            results.append(processed)
            del processed  # Manual cleanup
        return results
        
    def transform_item(self, item):
        """Transform a single data item"""
        if isinstance(item, dict):
            return {k: v * 2 if isinstance(v, (int, float)) else v 
                   for k, v in item.items()}
        return item

    def validate_results(self, results):
        """Quick validation of processing results"""
        return len(results) > 0 and all(r is not None for r in results)