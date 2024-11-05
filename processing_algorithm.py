import cv2
import numpy as np
import open3d as o3d
from typing import Tuple
import matplotlib.pyplot as plt

def get_intrinsic(width, height, focal=6000):
        return o3d.core.Tensor([[focal, 0     , width * 0.5], 
                                [0     , focal, height * 0.5],
                                [0     , 0     , 1]])

def get_extrinsic(x = 0, y = 0, z = 30):
        extrinsic = np.eye(4)
        extrinsic[:3,  3] = (x, y, z)

        return extrinsic

def compute_show_reprojection(pcd, width, height, intrinsic, extrinsic, depth_max=40.0, depth_scale=1.0):
    depth_reproj = pcd.project_to_depth_image(width,
                                                height,
                                                intrinsic,
                                                extrinsic,
                                                depth_scale=depth_scale,
                                                depth_max=depth_max)

    projection = np.asarray(depth_reproj.to_legacy())
    projection[projection == 0] = None
    depthmap = cv2.normalize(src=projection, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    
    colormap = plt.get_cmap('inferno')
    heatmap = (colormap(depthmap) * 2**16).astype(np.uint16)[:,:,:3]
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_RGB2BGR)
    
    return depthmap, heatmap

class ProcessingAlgorithm:
    def remove_noise(self, point_cloud: o3d.geometry.PointCloud, params: dict) -> o3d.geometry.PointCloud:
        method = params.get('method')
        # 다른 노이즈 제거 알고리즘도 추가 가능
        if method == 'statistical_outlier_removal':
            cl, ind = point_cloud.remove_statistical_outlier(nb_neighbors=params['nb_neighbors'], std_ratio=params['std_ratio'])
            return point_cloud.select_by_index(ind)
        
    def project_to_2d(self, point_cloud: o3d.geometry.PointCloud, projection_vector: dict) -> Tuple[np.ndarray, np.ndarray]:

        diameter = np.linalg.norm(
            np.asarray(point_cloud.get_max_bound()) - np.asarray(point_cloud.get_min_bound()))
        
        R = point_cloud.get_rotation_matrix_from_axis_angle(projection_vector['vector'])
        point_cloud = point_cloud.rotate(R, center = point_cloud.get_center())

        pcd = o3d.t.geometry.PointCloud.from_legacy(point_cloud)

        width, height = projection_vector['width'], projection_vector['height']
        intrinsic = get_intrinsic(width, height)
        x, y, z = 0, 0, diameter*10

        depth_map, heat_map = compute_show_reprojection(pcd, width, height, intrinsic, get_extrinsic(x, y, z,))

        return depth_map, heat_map        

    def save_depth_map(self, depth_map: np.ndarray, file_path: str):
        # float 타입의 depth_map을 .txt 파일로 저장
        np.savetxt(file_path, depth_map, fmt='%.6f')

    def save_heat_map(self, heat_map: np.ndarray, file_path: str):
        # heat_map을 컬러 이미지로 저장
        cv2.imwrite(file_path, heat_map)
