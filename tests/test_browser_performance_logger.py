import pytest
import json
import os
import time
from src.browser_performance_logger import log_browser_performance_metrics, export_performance_metrics, BrowserPerformanceMetrics

def test_log_performance_metrics_valid_data():
    """Test logging performance metrics with valid data"""
    test_data = {
        'firstContentfulPaint': 100.5,
        'largestContentfulPaint': 250.3,
        'totalBlockingTime': 50.2,
        'cumulativeLayoutShift': 0.15,
        'timeToInteractive': 300.7
    }
    
    metrics = log_browser_performance_metrics(test_data)
    
    assert isinstance(metrics, BrowserPerformanceMetrics)
    assert metrics.first_contentful_paint == 100.5
    assert metrics.largest_contentful_paint == 250.3
    assert metrics.total_blocking_time == 50.2
    assert metrics.cumulative_layout_shift == 0.15
    assert metrics.time_to_interactive == 300.7
    assert metrics.timestamp is not None

def test_log_performance_metrics_empty_data():
    """Test logging with no performance metrics"""
    with pytest.raises(ValueError, match="No performance metrics provided"):
        log_browser_performance_metrics({})

def test_export_performance_metrics_to_file(tmp_path):
    """Test exporting performance metrics to a file"""
    test_data = {
        'firstContentfulPaint': 100.5,
        'largestContentfulPaint': 250.3
    }
    
    metrics = log_browser_performance_metrics(test_data)
    file_path = tmp_path / "performance_metrics.json"
    exported_file = export_performance_metrics(metrics, str(file_path))
    
    assert exported_file == str(file_path)
    assert os.path.exists(file_path)
    
    with open(file_path, 'r') as f:
        loaded_metrics = json.load(f)
    
    assert loaded_metrics['first_contentful_paint'] == 100.5
    assert loaded_metrics['largest_contentful_paint'] == 250.3

def test_export_performance_metrics_to_string():
    """Test exporting performance metrics to a JSON string"""
    test_data = {
        'firstContentfulPaint': 100.5,
        'largestContentfulPaint': 250.3
    }
    
    metrics = log_browser_performance_metrics(test_data)
    metrics_json = export_performance_metrics(metrics)
    
    loaded_metrics = json.loads(metrics_json)
    assert loaded_metrics['first_contentful_paint'] == 100.5
    assert loaded_metrics['largest_contentful_paint'] == 250.3