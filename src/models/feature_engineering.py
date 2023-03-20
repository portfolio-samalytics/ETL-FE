from utils.logging import Logger

class FeatureEngineeringOrchestrator:
    logger = Logger("FeatureEngineeringOrchestrator").logger

    def __init__(self, run_config):
        self.run_config = run_config

