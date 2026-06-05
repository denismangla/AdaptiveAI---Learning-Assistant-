from typing import Dict, List

DEPENDENCY_GRAPH: Dict[str, List[str]] = {
    "Arrays": [],
    "Stack": ["Arrays"],
    "Queue": ["Stack"],
    "Linked List": ["Queue"],
}

CORE_CONCEPT_STEPS: Dict[str, List[str]] = {
    "Arrays": [
        "Review arrays and index access.",
        "Practice array creation and traversal.",
        "Solve simple array operations.",
    ],
    "Stack": [
        "Review LIFO behavior and push/pop operations.",
        "Practice stack use cases and top-of-stack handling.",
        "Attempt stack application questions.",
    ],
    "Queue": [
        "Review FIFO behavior and enqueue/dequeue operations.",
        "Practice queue order and scheduling examples.",
        "Attempt queue application questions.",
    ],
    "Linked List": [
        "Review linked nodes and pointer traversal.",
        "Practice inserting and removing nodes.",
        "Attempt linked list application questions.",
    ],
}


def get_prerequisite_chain(topic: str) -> List[str]:
    chain: List[str] = []
    current = topic
    while current in DEPENDENCY_GRAPH and DEPENDENCY_GRAPH[current]:
        prerequisite = DEPENDENCY_GRAPH[current][0]
        if prerequisite in chain:
            break
        chain.insert(0, prerequisite)
        current = prerequisite
    return chain


def get_dependency_edges() -> List[Dict[str, List[str]]]:
    return [{"topic": topic, "depends_on": dependencies} for topic, dependencies in DEPENDENCY_GRAPH.items()]


def build_dependency_recommendations(weak_topics: List[str]) -> List[str]:
    recommendations: List[str] = []
    for topic in weak_topics:
        prerequisites = get_prerequisite_chain(topic)
        for prereq in prerequisites:
            recommendation = f"Review {prereq}"
            if recommendation not in recommendations:
                recommendations.append(recommendation)
        if topic not in recommendations:
            recommendations.append(f"Reinforce {topic} fundamentals")
    return recommendations


def build_learning_path(profile: Dict) -> List[str]:
    weak_topics = profile.get("weak_topics", [])
    if not weak_topics:
        return [
            "Review the foundational programming concepts that support your learning path.",
            "Practice a mix of recognition, understanding, application, and debugging tasks.",
        ]

    learning_path: List[str] = []
    for topic in weak_topics:
        prerequisites = get_prerequisite_chain(topic)
        for dependency in prerequisites:
            step = f"Review {dependency}."
            if step not in learning_path:
                learning_path.append(step)

        if topic == "Stack":
            learning_path.extend(
                [
                    "Review LIFO behavior and stack operations.",
                    "Practice Push and Pop examples.",
                    "Attempt Stack application questions.",
                ]
            )
        elif topic == "Queue":
            learning_path.extend(
                [
                    "Review FIFO behavior and queue operations.",
                    "Practice Enqueue and Dequeue examples.",
                    "Attempt Queue application questions.",
                ]
            )
        elif topic == "Linked List":
            learning_path.extend(
                [
                    "Review how linked nodes differ from arrays.",
                    "Practice inserting and traversing nodes.",
                    "Attempt Linked List application questions.",
                ]
            )
        else:
            learning_path.extend(
                [
                    f"Review {topic} concepts.",
                    f"Practice core operations for {topic}.",
                    f"Attempt {topic} application questions.",
                ]
            )

    seen: set[str] = set()
    ordered_learning_path: List[str] = []
    for step in learning_path:
        if step not in seen:
            seen.add(step)
            ordered_learning_path.append(step)
    return ordered_learning_path


def get_knowledge_dependency_summary(profile: Dict) -> List[str]:
    weak_topics = profile.get("weak_topics", [])
    summary: List[str] = []
    for topic in weak_topics:
        prerequisites = get_prerequisite_chain(topic)
        if prerequisites:
            summary.append(f"{topic} depends on {', '.join(prerequisites)}.")
        else:
            summary.append(f"{topic} is a foundational concept.")
    if not summary:
        summary.append("No dependencies are currently highlighted.")
    return summary
