#!/usr/bin/env python3

from analysis import load_data, process_features
from data_processor import DataProcessor
import sys

def main():
    """Main entry point for the data science pipeline"""
    print("Starting data analysis pipeline...")
    
    # Load configuration
    processor = DataProcessor()
    
    # Simulated data loading
    sample_data = [
        {"value": 10, "category": "A"},
        {"value": 20, "category": "B"},
        {"value": 30, "category": "C"}
    ]
    
    try:
        results = processor.process_batch(sample_data)
        
        if processor.validate_results(results):
            print("Processing completed successfully")
            for i, result in enumerate(results):
                print(f"Result {i+1}: {result}")
        else:
            print("Processing failed validation")
            sys.exit(1)
            
    except Exception as e:
        print(f"Error in processing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()