import pytest
from point_cloud_manager import PointCloudManager
import open3d as o3d

def test_load_point_cloud():
    manager = PointCloudManager("tests/sample.ply")
    point_cloud = manager.load_point_cloud()
    
    assert isinstance(point_cloud, o3d.geometry.PointCloud)
    assert len(point_cloud.points) > 0  # 포인트 클라우드에 데이터가 있어야 합니다.
