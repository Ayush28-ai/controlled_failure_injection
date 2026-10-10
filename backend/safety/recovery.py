
async def recover_experiment(
    experiment_id: int,
    simulation_mode: bool = True,
) -> dict:
    if not simulation_mode:
        raise RuntimeError(
            "Real recovery actions are not implemented"
        )

    return {
        "experiment_id": experiment_id,
        "status": "not_required",
        "simulation_mode": True,
        "message": (
            "No infrastructure changes were made; "
            "therefore no rollback was required."
        ),
    }
