import os
from django.shortcuts import render
from django.views.generic import TemplateView
from pytz import common_timezones
from .models import Config
from .nabclockd import NabClockd


class SettingsView(TemplateView):
    template_name = "nabclockd/settings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["config"] = Config.load()
        context["timezones"] = common_timezones
        context["current_timezone"] = self.get_system_tz()
        return context

    def post(self, request, *args, **kwargs):
        config = Config.load()
        if "chime_hour" in request.POST:
            config.chime_hour = request.POST["chime_hour"] == "true"
        if "wakeup_time" in request.POST:
            (hour, min) = self.parse_time(request.POST["wakeup_time"])
            config.wakeup_hour = hour
            config.wakeup_min = min
        if "sleep_time" in request.POST:
            (hour, min) = self.parse_time(request.POST["sleep_time"])
            config.sleep_hour = hour
            config.sleep_min = min
        if ("wakeup_time_monday") in request.POST:
            (hour, min) = self.parse_time(request.POST["wakeup_time_monday"])
            config.wakeup_hour_monday = hour
            config.wakeup_min_monday = min
        if ("sleep_time_monday") in request.POST:
            (hour, min) = self.parse_time(request.POST["sleep_time_monday"])
            config.sleep_hour_monday = hour
            config.sleep_min_monday = min
        if ("wakeup_time_tuesday") in request.POST:
            (hour, min) = self.parse_time(request.POST["wakeup_time_tuesday"])
            config.wakeup_hour_tuesday = hour
            config.wakeup_min_tuesday = min
        if ("sleep_time_tuesday") in request.POST:
            (hour, min) = self.parse_time(request.POST["sleep_time_tuesday"])
            config.sleep_hour_tuesday = hour
            config.sleep_min_tuesday = min
        if ("wakeup_time_wednesday") in request.POST:
            (hour, min) = self.parse_time(
                request.POST["wakeup_time_wednesday"]
            )
            config.wakeup_hour_wednesday = hour
            config.wakeup_min_wednesday = min
        if ("sleep_time_wednesday") in request.POST:
            (hour, min) = self.parse_time(request.POST["sleep_time_wednesday"])
            config.sleep_hour_wednesday = hour
            config.sleep_min_wednesday = min
        if ("wakeup_time_thursday") in request.POST:
            (hour, min) = self.parse_time(request.POST["wakeup_time_thursday"])
            config.wakeup_hour_thursday = hour
            config.wakeup_min_thursday = min
        if ("sleep_time_thursday") in request.POST:
            (hour, min) = self.parse_time(request.POST["sleep_time_thursday"])
            config.sleep_hour_thursday = hour
            config.sleep_min_thursday = min
        if ("wakeup_time_friday") in request.POST:
            (hour, min) = self.parse_time(request.POST["wakeup_time_friday"])
            config.wakeup_hour_friday = hour
            config.wakeup_min_friday = min
        if ("sleep_time_friday") in request.POST:
            (hour, min) = self.parse_time(request.POST["sleep_time_friday"])
            config.sleep_hour_friday = hour
            config.sleep_min_friday = min
        if ("wakeup_time_saturday") in request.POST:
            (hour, min) = self.parse_time(request.POST["wakeup_time_saturday"])
            config.wakeup_hour_saturday = hour
            config.wakeup_min_saturday = min
        if ("sleep_time_saturday") in request.POST:
            (hour, min) = self.parse_time(request.POST["sleep_time_saturday"])
            config.sleep_hour_saturday = hour
            config.sleep_min_saturday = min
        if ("wakeup_time_sunday") in request.POST:
            (hour, min) = self.parse_time(request.POST["wakeup_time_sunday"])
            config.wakeup_hour_sunday = hour
            config.wakeup_min_sunday = min
        if ("sleep_time_sunday") in request.POST:
            (hour, min) = self.parse_time(request.POST["sleep_time_sunday"])
            config.sleep_hour_sunday = hour
            config.sleep_min_sunday = min
        if "timezone" in request.POST:
            selected_tz = request.POST["timezone"]
            if selected_tz in common_timezones:
                self.set_system_tz(selected_tz)
        if "play_wakeup_and_sleep_sounds" in request.POST:
            config.play_wakeup_and_sleep_sounds = (
                request.POST["play_wakeup_and_sleep_sounds"] == "true"
            )
        if "settings_per_day" in request.POST:
            config.settings_per_day = (
                request.POST["settings_per_day"] == "true"
            )
        config.save()
        NabClockd.signal_daemon()
        context = self.get_context_data(**kwargs)
        return render(request, SettingsView.template_name, context=context)

    def parse_time(self, hour_str):
        [hour_str, min_str] = hour_str.split(":")
        return (int(hour_str), int(min_str))

    def get_system_tz(self):
        with open("/etc/timezone") as w:
            return w.read().strip()

    def set_system_tz(self, tz):
        if tz != self.get_system_tz():
            with open("/etc/timezone", "w") as w:
                w.write("%s\n" % tz)
                os.system(
                    f"/bin/ln -fs /usr/share/zoneinfo/{tz} /etc/localtime"
                )
