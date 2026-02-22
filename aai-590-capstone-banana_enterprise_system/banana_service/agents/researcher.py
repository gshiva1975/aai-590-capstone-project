
from logger import setup_logger
logger = setup_logger("Researcher")

class ResearcherAgent:
    def __init__(self, store, embed):
        self.store = store
        self.embed = embed

    def run(self, state):
        logger.info("Researcher retrieving documents")
        vec = self.embed.encode(state["query"])
        docs = self.store.search(vec)
        return {**state, "docs": docs}
