import operator
import re

class Statistics:

    def __init__(self, file, initial_pattern, pattern_positions, details):
        self.details = details
        self.file = file
        self.conntrack_lines = []
        self.statistics = {}
        self.set_lines = {}
        self.pattern_positions = pattern_positions
        self.initial_pattern = initial_pattern

    def read_file(self, file):
        with open(file, 'r') as conntrack_file:
            for conntrack_line in conntrack_file:
                self.conntrack_lines.append(conntrack_line.replace("\n", ""))
        self.set_lines = set(self.conntrack_lines)

    def count_occurrences(self, positions):
        for line in self.set_lines:
            pattern = self.initial_pattern + ".*"
            pieces = line.split()
            for p in positions:
                pattern += pieces[p] + ".*"
            count = 0
            for conntrack_line in self.conntrack_lines:
                check = re.search(pattern, conntrack_line)
                if check is not None:
                    count += 1
            if self.details:
                self.statistics[line] = count
            else:
                self.statistics[pattern] = count
        return

    def process(self):
        self.read_file(self.file)
        self.count_occurrences(self.pattern_positions)
        return self.statistics


def connection_state_stats():
    connection_state = [3]

    stats = Statistics(file, initial_pattern, connection_state, False)
    sorted_x = sorted(stats.process().items(), key=operator.itemgetter(-1), reverse=True)
    print("Count\t Connection State")
    print("-" * 80)
    for item in sorted_x:
        state, counter = item
        state = state.replace(initial_pattern, "")
        state = str(state).replace(".*", "")
        print(" " + str(counter), "\t", str(state))
    print()


def duplicate_connection():
    connection_state = [3, 4, 5, 7]

    stats = Statistics(file, initial_pattern, connection_state, False)
    sorted_x = sorted(stats.process().items(), key=operator.itemgetter(-1), reverse=True)
    print("Count\t\tConnection")
    print("-" * 80)
    for item in sorted_x:
        state, counter = item
        state = state.replace(initial_pattern, "")
        state = str(state).replace(".*", " ")
        print(str(counter), "\t\t", str(state))


file = "conntrackL"
initial_pattern = "^tcp"
connection_state_stats()
duplicate_connection()
