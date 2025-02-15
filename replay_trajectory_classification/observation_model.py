"""Class for representing an environment and a condition (trial type, etc.)"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(order=True)
class ObservationModel:
    """Determines which environment and data points data correspond to.

    Attributes
    ----------
    environment_name : str, optional
    encoding_group : str, optional

    """

    environment_name: str = ""
    encoding_group: str = 0
