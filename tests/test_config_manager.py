import pytest

# 모듈경로 지정
import sys
sys.path.append(r'/home/bp/taek_project')

from config_manager import ConfigManager

def test_load_config():
    config_manager = ConfigManager("config.yaml")
    config = config_manager.load_config()
    
    assert "3d_data_path" in config
    assert "depth_map_path" in config
    assert "heat_map_path" in config
    assert "log" in config
    assert "algorithm" in config
