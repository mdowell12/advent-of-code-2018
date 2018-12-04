from datetime import datetime
import re


def read_input_file(f):
    with open(f, 'r') as input:
        return input.read().strip().split('\n')


def most_likely_sleeper(raw_logs):
    logs = _parse_and_sort_logs(raw_logs)
    # Nested dict, keyed at top level by Guard ID
    # which maps to a dict mapping minute -> number times
    # minute was occupied by sleep
    minutes_slept = {}
    
    current_guard = None
    sleep_start = None

    for log in logs:
        if log.action == Log.BEGIN:
            current_guard = log.guard_id
            if current_guard not in minutes_slept:
                minutes_slept[current_guard] = {}
            continue

        if log.action == Log.SLEEP:
            sleep_start = log.timestamp
            continue

        if log.action == Log.WAKE:
            minutes = _calculate_minutes_sleeping(sleep_start, log.timestamp)
            for minute in minutes:
                if minute not in minutes_slept[current_guard]:
                    minutes_slept[current_guard][minute] = 1
                else:
                    minutes_slept[current_guard][minute] += 1

            continue

        raise Exception("Unrecognized action found: " + log.action)


    strat_1 = _calculate_most_likely_1(minutes_slept)
    strat_2 = _calculate_most_likely_2(minutes_slept)

    return strat_1, strat_2


def _calculate_most_likely_1(minutes_slept):
    # Find the top guard by total minutes slept
    top_guard, top_guard_minutes = sorted(minutes_slept.items(), key=lambda x: sum(x[1].values()), reverse=True)[0]
    top_minute = _top_minute_for_guard(top_guard_minutes)

    return top_guard * top_minute


def _calculate_most_likely_2(minutes_slept):
    _, top_guard, top_minute = sorted([(f, g, m) for g in minutes_slept for m, f in minutes_slept[g].items()], reverse=True)[0]
    return top_guard * top_minute
    

def _top_minute_for_guard(guard_minutes):
    top = sorted(guard_minutes.items(), key=lambda x: x[1], reverse=True)[0]

    return top[0] if top else None


def _calculate_minutes_sleeping(start, end):
    return range(start.minute, end.minute)


def _parse_and_sort_logs(logs):
    parsed = []
    for log in logs:
        parsed_log = Log.parse(log)
        parsed.append(parsed_log)

    return sorted(parsed, key=lambda x: x.timestamp)


class Log(object):
    BEGIN = "BEGIN"
    SLEEP = "SLEEP"
    WAKE = "WAKE"

    TIMESTAMP_PATTERN = re.compile(r'\d+-\d+-\d+\s\d+:\d+')
    GUARD_ID_PATTERN  = re.compile(r'#\d+')
    ACTION_PATTERN    = re.compile(r'[a-z][a-z,\s]+$')

    ACTION_MAP = {
        'begins shift': BEGIN,
        'falls asleep': SLEEP,
        'wakes up': WAKE,
    }

    def __init__(self, action, timestamp, guard_id=None):
        self.action = action
        self.timestamp = timestamp
        self.guard_id = guard_id

    @staticmethod
    def parse(raw_log):
        timestamp = datetime.strptime(Log.TIMESTAMP_PATTERN.search(raw_log).group(), '%Y-%m-%d %H:%M')
        action = Log.ACTION_MAP[Log.ACTION_PATTERN.search(raw_log).group()]

        guard_match = Log.GUARD_ID_PATTERN.search(raw_log)
        guard_id = int(guard_match.group()[1:]) if guard_match is not None else None

        return Log(action, timestamp, guard_id=guard_id)

    def __repr__(self):
        return "%s Guard: %s Action: %s" % (str(self.timestamp), self.guard_id, self.action)


if __name__ == "__main__":
    import sys
    f = sys.argv[1]
    unsorted_logs = read_input_file(f)

    strat_1, strat_2 = most_likely_sleeper(unsorted_logs)
    print "Most likely sleeper result (strategy 1):", strat_1
    print "Most likely sleeper result (strategy 2):", strat_2

