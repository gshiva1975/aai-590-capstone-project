
from logger import setup_logger
logger = setup_logger("Analyst")

class AnalystAgent:
    def __init__(self, model):
        self.model = model

    def run(self, state):
        logger.info("Analyst evaluating sentiment")
        combined = " ".join(state["docs"])
        sentiment = self.model.predict(combined)
        return {**state, "sentiment": sentiment}
