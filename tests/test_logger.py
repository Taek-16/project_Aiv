import pytest
from logger import Logger

def test_logger():
    logger_config = {
        "path": "tests/test.log",
        "file_log": True,
        "print_log": False
    }
    logger = Logger(logger_config)
    
    # 로그 파일에 기록하기
    logger.info("Test log message")
    
    # 로그 파일에 기록이 남았는지 확인
    with open("tests/test.log", "r") as f:
        log_content = f.read()
    
    assert "Test log message" in log_content
