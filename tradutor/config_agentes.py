CONFIG_AGENTES = {
    "agent_1": {
        "incident": "$.incident_id",
        "additional_information": "$.additional_information.KEY1",
    },
    "agent_2": {
        "incident": {
            "id": "$.incident_id",
            "severity": "$.severity",
            "incident": {
                "id": "$.incident_id",
                "severity": "$.severity",
                "incident": {
                    "id": "$.incident_id",
                    "severity": "$.severity",
                },
            },
        },
        "severity": "$.severity",
    },
    "agent_3": "$",
}
