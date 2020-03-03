import os
import pytest
from django.test import TestCase, Client
from nabclockd.models import Config


@pytest.mark.skipif(
    not os.path.isfile("/etc/timezone"),
    reason="Test requires /etc/timezone to exist",
)
class TestView(TestCase):
    def setUp(self):
        Config.load()

    def test_get_settings(self):
        c = Client()
        response = c.get("/nabclockd/settings")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, "nabclockd/settings.html")
        self.assertTrue("config" in response.context)
        config = Config.load()
        self.assertEqual(response.context["config"], config)
        self.assertEqual(config.chime_hour, True)
        self.assertEqual(config.wakeup_hour, 7)
        self.assertEqual(config.wakeup_min, 0)
        self.assertEqual(config.sleep_hour, 22)
        self.assertEqual(config.sleep_min, 0)
        self.assertEqual(config.wakeup_hour_monday, 7)
        self.assertEqual(config.wakeup_min_monday, 0)
        self.assertEqual(config.sleep_hour_monday, 22)
        self.assertEqual(config.sleep_min_monday, 0)
        self.assertEqual(config.wakeup_hour_tuesday, 7)
        self.assertEqual(config.wakeup_min_tuesday, 0)
        self.assertEqual(config.sleep_hour_tuesday, 22)
        self.assertEqual(config.sleep_min_tuesday, 0)
        self.assertEqual(config.wakeup_hour_wednesday, 7)
        self.assertEqual(config.wakeup_min_wednesday, 0)
        self.assertEqual(config.sleep_hour_wednesday, 22)
        self.assertEqual(config.sleep_min_wednesday, 0)
        self.assertEqual(config.wakeup_hour_thursday, 7)
        self.assertEqual(config.wakeup_min_thursday, 0)
        self.assertEqual(config.sleep_hour_thursday, 22)
        self.assertEqual(config.sleep_min_thursday, 0)
        self.assertEqual(config.wakeup_hour_friday, 7)
        self.assertEqual(config.wakeup_min_friday, 0)
        self.assertEqual(config.sleep_hour_friday, 22)
        self.assertEqual(config.sleep_min_friday, 0)
        self.assertEqual(config.wakeup_hour_saturday, 7)
        self.assertEqual(config.wakeup_min_saturday, 0)
        self.assertEqual(config.sleep_hour_saturday, 22)
        self.assertEqual(config.sleep_min_saturday, 0)
        self.assertEqual(config.wakeup_hour_sunday, 7)
        self.assertEqual(config.wakeup_min_sunday, 0)
        self.assertEqual(config.sleep_hour_sunday, 22)
        self.assertEqual(config.sleep_min_sunday, 0)

    def test_set_chime_hour(self):
        c = Client()
        response = c.post("/nabclockd/settings", {"chime_hour": "false"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, "nabclockd/settings.html")
        self.assertTrue("config" in response.context)
        config = Config.load()
        self.assertEqual(response.context["config"], config)
        self.assertEqual(config.chime_hour, False)
        self.assertEqual(config.wakeup_hour, 7)
        self.assertEqual(config.wakeup_min, 0)
        self.assertEqual(config.sleep_hour, 22)
        self.assertEqual(config.sleep_min, 0)
        self.assertEqual(config.wakeup_hour_monday, 7)
        self.assertEqual(config.wakeup_min_monday, 0)
        self.assertEqual(config.sleep_hour_monday, 22)
        self.assertEqual(config.sleep_min_monday, 0)
        self.assertEqual(config.wakeup_hour_tuesday, 7)
        self.assertEqual(config.wakeup_min_tuesday, 0)
        self.assertEqual(config.sleep_hour_tuesday, 22)
        self.assertEqual(config.sleep_min_tuesday, 0)
        self.assertEqual(config.wakeup_hour_wednesday, 7)
        self.assertEqual(config.wakeup_min_wednesday, 0)
        self.assertEqual(config.sleep_hour_wednesday, 22)
        self.assertEqual(config.sleep_min_wednesday, 0)
        self.assertEqual(config.wakeup_hour_thursday, 7)
        self.assertEqual(config.wakeup_min_thursday, 0)
        self.assertEqual(config.sleep_hour_thursday, 22)
        self.assertEqual(config.sleep_min_thursday, 0)
        self.assertEqual(config.wakeup_hour_friday, 7)
        self.assertEqual(config.wakeup_min_friday, 0)
        self.assertEqual(config.sleep_hour_friday, 22)
        self.assertEqual(config.sleep_min_friday, 0)
        self.assertEqual(config.wakeup_hour_saturday, 7)
        self.assertEqual(config.wakeup_min_saturday, 0)
        self.assertEqual(config.sleep_hour_saturday, 22)
        self.assertEqual(config.sleep_min_saturday, 0)
        self.assertEqual(config.wakeup_hour_sunday, 7)
        self.assertEqual(config.wakeup_min_sunday, 0)
        self.assertEqual(config.sleep_hour_sunday, 22)
        self.assertEqual(config.sleep_min_sunday, 0)

    def test_set_wakeup_time(self):
        c = Client()
        response = c.post("/nabclockd/settings", {"wakeup_time": "09:42"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, "nabclockd/settings.html")
        self.assertTrue("config" in response.context)
        config = Config.load()
        self.assertEqual(response.context["config"], config)
        self.assertEqual(config.chime_hour, True)
        self.assertEqual(config.wakeup_hour, 9)
        self.assertEqual(config.wakeup_min, 42)
        self.assertEqual(config.sleep_hour, 22)
        self.assertEqual(config.sleep_min, 0)
        self.assertEqual(config.wakeup_hour_monday, 7)
        self.assertEqual(config.wakeup_min_monday, 0)
        self.assertEqual(config.sleep_hour_monday, 22)
        self.assertEqual(config.sleep_min_monday, 0)
        self.assertEqual(config.wakeup_hour_tuesday, 7)
        self.assertEqual(config.wakeup_min_tuesday, 0)
        self.assertEqual(config.sleep_hour_tuesday, 22)
        self.assertEqual(config.sleep_min_tuesday, 0)
        self.assertEqual(config.wakeup_hour_wednesday, 7)
        self.assertEqual(config.wakeup_min_wednesday, 0)
        self.assertEqual(config.sleep_hour_wednesday, 22)
        self.assertEqual(config.sleep_min_wednesday, 0)
        self.assertEqual(config.wakeup_hour_thursday, 7)
        self.assertEqual(config.wakeup_min_thursday, 0)
        self.assertEqual(config.sleep_hour_thursday, 22)
        self.assertEqual(config.sleep_min_thursday, 0)
        self.assertEqual(config.wakeup_hour_friday, 7)
        self.assertEqual(config.wakeup_min_friday, 0)
        self.assertEqual(config.sleep_hour_friday, 22)
        self.assertEqual(config.sleep_min_friday, 0)
        self.assertEqual(config.wakeup_hour_saturday, 7)
        self.assertEqual(config.wakeup_min_saturday, 0)
        self.assertEqual(config.sleep_hour_saturday, 22)
        self.assertEqual(config.sleep_min_saturday, 0)
        self.assertEqual(config.wakeup_hour_sunday, 7)
        self.assertEqual(config.wakeup_min_sunday, 0)
        self.assertEqual(config.sleep_hour_sunday, 22)
        self.assertEqual(config.sleep_min_sunday, 0)

    def test_set_sleep_time(self):
        c = Client()
        response = c.post("/nabclockd/settings", {"sleep_time": "21:21"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, "nabclockd/settings.html")
        self.assertTrue("config" in response.context)
        config = Config.load()
        self.assertEqual(response.context["config"], config)
        self.assertEqual(config.chime_hour, True)
        self.assertEqual(config.wakeup_hour, 7)
        self.assertEqual(config.wakeup_min, 0)
        self.assertEqual(config.sleep_hour, 21)
        self.assertEqual(config.sleep_min, 21)
        self.assertEqual(config.wakeup_hour_monday, 7)
        self.assertEqual(config.wakeup_min_monday, 0)
        self.assertEqual(config.sleep_hour_monday, 22)
        self.assertEqual(config.sleep_min_monday, 0)
        self.assertEqual(config.wakeup_hour_tuesday, 7)
        self.assertEqual(config.wakeup_min_tuesday, 0)
        self.assertEqual(config.sleep_hour_tuesday, 22)
        self.assertEqual(config.sleep_min_tuesday, 0)
        self.assertEqual(config.wakeup_hour_wednesday, 7)
        self.assertEqual(config.wakeup_min_wednesday, 0)
        self.assertEqual(config.sleep_hour_wednesday, 22)
        self.assertEqual(config.sleep_min_wednesday, 0)
        self.assertEqual(config.wakeup_hour_thursday, 7)
        self.assertEqual(config.wakeup_min_thursday, 0)
        self.assertEqual(config.sleep_hour_thursday, 22)
        self.assertEqual(config.sleep_min_thursday, 0)
        self.assertEqual(config.wakeup_hour_friday, 7)
        self.assertEqual(config.wakeup_min_friday, 0)
        self.assertEqual(config.sleep_hour_friday, 22)
        self.assertEqual(config.sleep_min_friday, 0)
        self.assertEqual(config.wakeup_hour_saturday, 7)
        self.assertEqual(config.wakeup_min_saturday, 0)
        self.assertEqual(config.sleep_hour_saturday, 22)
        self.assertEqual(config.sleep_min_saturday, 0)
        self.assertEqual(config.wakeup_hour_sunday, 7)
        self.assertEqual(config.wakeup_min_sunday, 0)
        self.assertEqual(config.sleep_hour_sunday, 22)
        self.assertEqual(config.sleep_min_sunday, 0)

    def test_set_all(self):
        c = Client()
        response = c.post(
            "/nabclockd/settings",
            {
                "chime_hour": "false",
                "wakeup_time": "09:42",
                "sleep_time": "21:21",
                "wakeup_time_monday": "09:42",
                "sleep_time_monday": "21:21",
                "wakeup_time_tuesday": "09:42",
                "sleep_time_tuesday": "21:21",
                "wakeup_time_wednesday": "09:42",
                "sleep_time_wednesday": "21:21",
                "wakeup_time_thursday": "09:42",
                "sleep_time_thursday": "21:21",
                "wakeup_time_friday": "09:42",
                "sleep_time_friday": "21:21",
                "wakeup_time_saturday": "09:42",
                "sleep_time_saturday": "21:21",
                "wakeup_time_sunday": "09:42",
                "sleep_time_sunday": "21:21",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, "nabclockd/settings.html")
        self.assertTrue("config" in response.context)
        config = Config.load()
        self.assertEqual(response.context["config"], config)
        self.assertEqual(config.chime_hour, False)
        self.assertEqual(config.wakeup_hour, 9)
        self.assertEqual(config.wakeup_min, 42)
        self.assertEqual(config.sleep_hour, 21)
        self.assertEqual(config.sleep_min, 21)
        self.assertEqual(config.wakeup_hour_monday, 9)
        self.assertEqual(config.wakeup_min_monday, 42)
        self.assertEqual(config.sleep_hour_monday, 21)
        self.assertEqual(config.sleep_min_monday, 21)
        self.assertEqual(config.wakeup_hour_tuesday, 9)
        self.assertEqual(config.wakeup_min_tuesday, 42)
        self.assertEqual(config.sleep_hour_tuesday, 21)
        self.assertEqual(config.sleep_min_tuesday, 21)
        self.assertEqual(config.wakeup_hour_wednesday, 9)
        self.assertEqual(config.wakeup_min_wednesday, 42)
        self.assertEqual(config.sleep_hour_wednesday, 21)
        self.assertEqual(config.sleep_min_wednesday, 21)
        self.assertEqual(config.wakeup_hour_thursday, 9)
        self.assertEqual(config.wakeup_min_thursday, 42)
        self.assertEqual(config.sleep_hour_thursday, 21)
        self.assertEqual(config.sleep_min_thursday, 21)
        self.assertEqual(config.wakeup_hour_friday, 9)
        self.assertEqual(config.wakeup_min_friday, 42)
        self.assertEqual(config.sleep_hour_friday, 21)
        self.assertEqual(config.sleep_min_friday, 21)
        self.assertEqual(config.wakeup_hour_saturday, 9)
        self.assertEqual(config.wakeup_min_saturday, 42)
        self.assertEqual(config.sleep_hour_saturday, 21)
        self.assertEqual(config.sleep_min_saturday, 21)
        self.assertEqual(config.wakeup_hour_sunday, 9)
        self.assertEqual(config.wakeup_min_sunday, 42)
        self.assertEqual(config.sleep_hour_sunday, 21)
        self.assertEqual(config.sleep_min_sunday, 21)
