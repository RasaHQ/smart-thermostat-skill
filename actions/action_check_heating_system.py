"""Action to check the heating system status via (mock) API.

This is the custom action we show in the video - real Python code
that guarantees consistent, non-hallucinated responses.
"""

import asyncio
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


# Mock thermostat data - simulating what we'd get from a real API
MOCK_THERMOSTAT_DATA = {
    "user_123": {
        "thermostat_online": True,
        "current_temp": 18.5,
        "target_temp": 21.0,
        "heating_active": True,
        "last_seen": "2 minutes ago",
        "device_name": "Living Room Thermostat",
    },
    "user_456": {
        "thermostat_online": False,
        "current_temp": None,
        "target_temp": 20.0,
        "heating_active": False,
        "last_seen": "3 hours ago",
        "device_name": "Living Room Thermostat",
    },
}

DEFAULT_USER = "user_123"


class ActionCheckHeatingSystem(Action):
    """Check the heating system status via (mock) API."""

    def name(self) -> Text:
        return "action_check_heating_system"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Simulate API latency
        await asyncio.sleep(1.5)

        # Get user ID from slot or use default
        user_id = tracker.get_slot("user_id") or DEFAULT_USER

        # "Call" the thermostat API (mocked)
        data = await self._fetch_thermostat_status(user_id)

        if data is None:
            return [
                SlotSet("thermostat_online", None),
                SlotSet("api_error", True),
            ]

        return [
            SlotSet("thermostat_online", data["thermostat_online"]),
            SlotSet("current_temp", data["current_temp"]),
            SlotSet("target_temp", data["target_temp"]),
            SlotSet("heating_active", data["heating_active"]),
            SlotSet("device_name", data["device_name"]),
            SlotSet("last_seen", data["last_seen"]),
            SlotSet("api_error", False),
        ]

    async def _fetch_thermostat_status(self, user_id: str) -> Dict[Text, Any] | None:
        """Fetch thermostat status from the API.

        In production, this would be a real HTTP call to the Hive API.
        For the demo, we return mock data.
        """
        if user_id not in MOCK_THERMOSTAT_DATA:
            return None
        return MOCK_THERMOSTAT_DATA[user_id]
