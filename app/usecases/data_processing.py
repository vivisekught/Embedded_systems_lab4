from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData


def process_agent_data(
    agent_data: AgentData,
) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    road_state: str = "ok"
    z = agent_data.accelerometer.z
    if z < 5000:
        road_state = "big_pit"
    elif z < 10000:
        road_state = "pit"
    elif z > 25000:
        road_state = "big_tubercle"
    elif z > 20000:
        road_state = "tubercle"

    return ProcessedAgentData(road_state=road_state, agent_data=agent_data)