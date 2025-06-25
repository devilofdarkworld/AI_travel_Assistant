# from typing import TypedDict
# from langgraph.graph import StateGraph
# from agent_config import agent
# from agent2 import image_agent  # ✅ your lightweight image-only agent

# # Define workflow state
# class TravelState(TypedDict, total=False):
#     preferences: dict
#     suggestion: str
#     itinerary: str
#     support: str
#     visuals: str  # ⬅️ new for image response


# # ✅ User input
# def user_input_node(state: TravelState) -> TravelState:
#     return {
#         "preferences": state.get("preferences", {
#             "interests": ["beach"],
#             "budget": "medium",
#             "duration": 5
#         })
#     }

# # ✅ Suggest a destination using main agent
# def suggest_destinations_node(state: TravelState) -> TravelState:
#     prefs = state["preferences"]
#     prompt = (
#         f"Suggest one Indian travel destination based on:\n"
#         f"- Interests: {', '.join(prefs['interests'])}\n"
#         f"- Budget: {prefs['budget']}\n"
#         f"- Duration: {prefs['duration']} days\n"
#         f"Return only the best destination name."
#     )
#     result = agent.invoke({"input": prompt})
#     return {**state, "suggestion": result["output"].strip()}

# # ✅ Create itinerary using main agent
# def itinerary_node(state: TravelState) -> TravelState:
#     dest = state["suggestion"]
#     days = state["preferences"]["duration"]
#     interests = ", ".join(state["preferences"]["interests"])

#     prompt = (
#         f"Plan a detailed {days}-day trip to {dest} for a traveler interested in {interests}.\n"
#         f"Give 2–3 places per day with a short note.\n"
#         f"Format:\nDay 1: Place A, Place B (notes)\nDay 2: ..."
#     )
#     result = agent.invoke({"input": prompt})
#     return {**state, "itinerary": result["output"]}

# # ✅ Get weather & attractions using main agent
# def agent_support_node(state: TravelState) -> TravelState:
#     dest = state["suggestion"]
#     prompt = (
#         f"User is traveling to {dest}.\n"
#         f"Use tools to fetch:\n"
#         f"1. Current weather\n"
#         f"2. Top 3–5 attractions\n"
#         f"Return it in a short friendly summary."
#     )
#     result = agent.invoke({"input": prompt})
#     return {**state, "support": result["output"]}

# # ✅ Get place + hotel images using image_agent
# def image_summary_node(state: TravelState) -> TravelState:
#     dest = state["suggestion"]
#     prompt = (
#         f"Show destination images and 3–5 hotel previews in {dest}.\n"
#         f"Return URLs or summaries for visual display."
#     )
#     result = image_agent.invoke({"input": prompt})
#     return {**state, "visuals": result["output"]}


# # ✅ Build the updated graph
# def create_workflow(preferences: dict = None):
#     builder = StateGraph(TravelState)

#     def user_input_node_override(state: TravelState) -> TravelState:
#         return {"preferences": preferences or {
#             "interests": ["beach"], "budget": "medium", "duration": 5
#         }}

#     builder.add_node("Input", user_input_node_override)
#     builder.add_node("Suggest", suggest_destinations_node)
#     builder.add_node("Itinerary", itinerary_node)
#     builder.add_node("Support", agent_support_node)
#     builder.add_node("Visuals", image_summary_node)  # 🔥 new image node

#     builder.set_entry_point("Input")
#     builder.add_edge("Input", "Suggest")
#     builder.add_edge("Suggest", "Itinerary")
#     builder.add_edge("Itinerary", "Support")
#     builder.add_edge("Support", "Visuals")  # 🔁 call image_agent last
#     builder.set_finish_point("Visuals")

#     return builder.compile()
# 📁 graph.py
from typing import TypedDict, Optional
from langgraph.graph import StateGraph
from langchain_core.runnables import Runnable, RunnableLambda
from agent_config import agent
# from agent2 import image_agent


# --------------------------
# Define State
# --------------------------
class TravelState(TypedDict, total=False):
    preferences: dict
    suggestion: str
    itinerary: str
    support: str
    visuals: str


# --------------------------
# Node Functions
# --------------------------
def user_input_node(preferences: Optional[dict] = None):
    def _func(state: TravelState) -> TravelState:
        return {
            "preferences": preferences or {
                "interests": ["beach"],
                "budget": "medium",
                "duration": 5
            }
        }
    return RunnableLambda(_func)


def suggest_destinations_node(state: TravelState) -> TravelState:
    prefs = state["preferences"]
    prompt = (
        f"Suggest one Indian travel destination based on:\n"
        f"- Interests: {', '.join(prefs['interests'])}\n"
        f"- Budget: {prefs['budget']}\n"
        f"- Duration: {prefs['duration']} days\n"
        f"Return only the best destination name."
    )
    result = agent.invoke({"input": prompt})
    return {**state, "suggestion": result["output"].strip()}


def itinerary_node(state: TravelState) -> TravelState:
    dest = state["suggestion"]
    days = state["preferences"]["duration"]
    interests = ", ".join(state["preferences"]["interests"])
    prompt = (
        f"Plan a detailed {days}-day trip to {dest} for a traveler interested in {interests}.\n"
        f"Give 2–3 places per day with a short note.\n"
        f"Format:\nDay 1: Place A, Place B (notes)\nDay 2: ..."
    )
    result = agent.invoke({"input": prompt})
    return {**state, "itinerary": result["output"]}


def agent_support_node(state: TravelState) -> TravelState:
    dest = state["suggestion"]
    prompt = (
        f"User is traveling to {dest}.\n"
        f"Use tools to fetch:\n"
        f"1. Current weather\n"
        f"2. Top 3–5 attractions\n"
        f"Return it in a short friendly summary."
    )
    result = agent.invoke({"input": prompt})
    return {**state, "support": result["output"]}


def image_summary_node(state: TravelState) -> TravelState:
    dest = state["suggestion"]
    prompt = (
        f"Show destination images and 3–5 hotel previews in {dest}.\n"
        f"Return URLs or summaries for visual display."
    )
    result = agent.invoke({"input": prompt})
    return {**state, "visuals": result["output"]}


# --------------------------
# Build LangGraph
# --------------------------
def create_workflow(preferences: Optional[dict] = None):
    builder = StateGraph(TravelState)

    # Add nodes as RunnableLambda
    builder.add_node("Input", user_input_node(preferences))
    builder.add_node("Suggest", RunnableLambda(suggest_destinations_node))
    builder.add_node("Itinerary", RunnableLambda(itinerary_node))
    builder.add_node("Support", RunnableLambda(agent_support_node))
    builder.add_node("Visuals", RunnableLambda(image_summary_node))

    # Connect nodes
    builder.set_entry_point("Input")
    builder.add_edge("Input", "Suggest")
    builder.add_edge("Suggest", "Itinerary")
    builder.add_edge("Itinerary", "Support")
    builder.add_edge("Support", "Visuals")
    builder.set_finish_point("Visuals")

    return builder.compile()
