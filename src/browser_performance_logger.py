import json
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict
import time

@dataclass
class BrowserPerformanceMetrics:
    """
    Dataclass to store browser rendering performance metrics.
    
    Attributes:
        timestamp (float): Timestamp of when metrics were collected
        first_contentful_paint (float): Time to first contentful paint (ms)
        largest_contentful_paint (float): Time to largest contentful paint (ms)
        total_blocking_time (float): Total blocking time (ms)
        cumulative_layout_shift (float): Cumulative layout shift score
        time_to_interactive (float): Time to interactive (ms)
    """
    timestamp: float
    first_contentful_paint: Optional[float] = None
    largest_contentful_paint: Optional[float] = None
    total_blocking_time: Optional[float] = None
    cumulative_layout_shift: Optional[float] = None
    time_to_interactive: Optional[float] = None

def log_browser_performance_metrics(performance_data: Dict[str, Any]) -> BrowserPerformanceMetrics:
    """
    Create and validate browser performance metrics log.
    
    Args:
        performance_data (Dict[str, Any]): Dictionary of performance metrics
    
    Returns:
        BrowserPerformanceMetrics: Validated performance metrics object
    
    Raises:
        ValueError: If provided metrics are invalid
    """
    try:
        metrics = BrowserPerformanceMetrics(
            timestamp=time.time(),
            first_contentful_paint=performance_data.get('firstContentfulPaint'),
            largest_contentful_paint=performance_data.get('largestContentfulPaint'),
            total_blocking_time=performance_data.get('totalBlockingTime'),
            cumulative_layout_shift=performance_data.get('cumulativeLayoutShift'),
            time_to_interactive=performance_data.get('timeToInteractive')
        )
        
        # Optional validation logic
        if all(value is None for value in [
            metrics.first_contentful_paint,
            metrics.largest_contentful_paint,
            metrics.total_blocking_time,
            metrics.cumulative_layout_shift,
            metrics.time_to_interactive
        ]):
            raise ValueError("No performance metrics provided")
        
        return metrics
    
    except Exception as e:
        raise ValueError(f"Invalid performance metrics: {str(e)}")

def export_performance_metrics(metrics: BrowserPerformanceMetrics, filename: Optional[str] = None) -> Optional[str]:
    """
    Export performance metrics to a JSON file or return JSON string.
    
    Args:
        metrics (BrowserPerformanceMetrics): Performance metrics to export
        filename (Optional[str]): File to export metrics to. If None, returns JSON string
    
    Returns:
        Optional[str]: JSON string of metrics or filename where metrics were saved
    """
    metrics_dict = asdict(metrics)
    metrics_json = json.dumps(metrics_dict, indent=2)
    
    if filename:
        try:
            with open(filename, 'w') as f:
                f.write(metrics_json)
            return filename
        except IOError as e:
            raise IOError(f"Could not write metrics to file: {e}")
    
    return metrics_json