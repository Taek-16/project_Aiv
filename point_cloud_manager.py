import open3d as o3d
class PointCloudManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_point_cloud(self) -> o3d.geometry.PointCloud:
        point_cloud = o3d.io.read_point_cloud(self.file_path)
        center = point_cloud.get_center()
        point_cloud = point_cloud.translate(-center)
        return point_cloud
