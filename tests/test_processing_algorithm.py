import pytest
from processing_algorithm import ProcessingAlgorithm
from point_cloud_manager import PointCloudManager
import numpy as np

def test_remove_noise():
    manager = PointCloudManager("tests/sample.ply")
    algorithm = ProcessingAlgorithm()
    
    point_cloud = manager.load_point_cloud()
    cleaned_cloud = algorithm.remove_noise(point_cloud, {"method": "statistical_outlier_removal", "nb_neighbors": 20, "std_ratio": 1.0})
    
    assert len(cleaned_cloud.points) < len(point_cloud.points)  # 일부 노이즈가 제거되어야 함

def test_project_to_2d():
    manager = PointCloudManager("tests/sample.ply")
    algorithm = ProcessingAlgorithm()
    
    point_cloud = manager.load_point_cloud()
    depth_map, heat_map = algorithm.project_to_2d(point_cloud, {"vector": [0, 0, 1], "width": 640, "height": 480})

    assert isinstance(depth_map, np.ndarray)
    assert isinstance(heat_map, np.ndarray)
    assert depth_map.shape == (480, 640)
    assert heat_map.shape == (480, 640, 3)
