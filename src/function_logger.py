import functools
import logging
import time
from typing import Callable, Any

def log_execution(logger: logging.Logger = None):
    """
    Decorator to log function execution start and end.
    
    Args:
        logger (logging.Logger, optional): Logger to use. 
               If not provided, uses the root logger.
    
    Returns:
        Callable: Decorated function that logs execution details
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Prepare function signature details
            func_name = func.__name__
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            
            # Log start of function execution
            logger.info(f"Executing {func_name}({signature})")
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Log successful completion
                end_time = time.time()
                execution_time = end_time - start_time
                logger.info(f"Finished {func_name}. Execution time: {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur
                logger.error(f"Exception in {func_name}: {str(e)}")
                raise
        
        return wrapper
    
    return decorator