import yaml
from config_manager import ConfigManager
from point_cloud_manager import PointCloudManager
from processing_algorithm import ProcessingAlgorithm
from logger import Logger

def main():
    # 설정 읽기
    config_manager = ConfigManager("config.yaml")
    config = config_manager.load_config()

    # 로거 초기화
    logger = Logger(config['log'])

    try:
        # 3D 포인트 클라우드 로드
        point_cloud_manager = PointCloudManager(config['3d_data_path'])
        point_cloud = point_cloud_manager.load_point_cloud()

        # 노이즈 제거
        processing_algorithm = ProcessingAlgorithm()
        processed_cloud = processing_algorithm.remove_noise(point_cloud, config['algorithm']['noise_reduction'])

        # 2D 이미지 생성
        depth_map, heat_map = processing_algorithm.project_to_2d(processed_cloud, config['algorithm']['projection'])

        # 이미지 저장
        if config['depth_map_path']:
            processing_algorithm.save_depth_map(depth_map, config['depth_map_path'])
        if config['heat_map_path']:
            processing_algorithm.save_heat_map(heat_map, config['heat_map_path'])

        logger.info("Program executed successfully")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
