import pytz
import datetime

county = "Europe/Moscow"

tz_to_display = pytz.timezone(county)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(county, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

for x in pytz.all_timezones:
    print(x)

print("=" * 50)
for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names[x])

for x in sorted(pytz.country_names):
    print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x, "No time zone defined")))

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]))
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")