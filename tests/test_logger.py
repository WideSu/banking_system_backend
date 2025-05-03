# -------- Logging --------
import logging, time
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def log_test(enable_time_logging=True, level=logging.INFO):
    """Decorator factory that accepts parameters"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Start timer if time logging is enabled
            start_time = time.time() if enable_time_logging else None
            
            # Log test start
            logger.log(level, f"🚀 Starting test: {func.__name__}")
            
            try:
                result = func(*args, **kwargs)
                
                # Log test completion
                if enable_time_logging:
                    duration = time.time() - start_time
                    logger.log(level, f"✅ Test passed in {duration:.4f}s: {func.__name__}")
                else:
                    logger.log(level, f"✅ Test passed: {func.__name__}")
                
                return result
            except Exception as e:
                if enable_time_logging:
                    duration = time.time() - start_time
                    logger.error(f"❌ Test failed after {duration:.4f}s: {func.__name__} - {str(e)}")
                else:
                    logger.error(f"❌ Test failed: {func.__name__} - {str(e)}")
                raise
        return wrapper
    return decorator