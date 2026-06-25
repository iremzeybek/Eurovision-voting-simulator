import random

POINTS = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]


class Song:
    def __init__(self):
        self.vocals = random.randint(60, 100)
        self.staging = random.randint(60, 100)
        self.originality = random.randint(60, 100)
        self.catchiness = random.randint(60, 100)

    def jury_score(self):
        return (
            self.vocals * 0.40
            + self.originality * 0.35
            + self.staging * 0.25
        )

    def televote_score(self):
        return (
            self.staging * 0.45
            + self.catchiness * 0.35
            + self.originality * 0.20
        )


class Country:
    def __init__(self, name):
        self.name = name
        self.song = Song()
        self.jury_points = 0
        self.tele_points = 0

    @property
    def total_points(self):
        return self.jury_points + self.tele_points

    def reset_points(self):
        self.jury_points = 0
        self.tele_points = 0


COUNTRY_NAMES = [
    "Sweden",
    "Italy",
    "France",
    "Spain",
    "Germany",
    "Ukraine",
    "Finland",
    "Norway",
    "Greece",
    "Turkey",
    "Netherlands",
    "Poland",
    "Serbia",
    "Portugal",
    "Croatia",
    "Belgium",
    "Austria",
    "Switzerland",
    "Ireland",
    "Czechia"
]

countries = [Country(name) for name in COUNTRY_NAMES]

biases = {
    ("Greece", "Turkey"): 6,
    ("Turkey", "Greece"): 6,
    ("Norway", "Sweden"): 4,
    ("Sweden", "Norway"): 4,
}


def rank_for_jury(voter, contestants):

    ranking = []

    for target in contestants:

        if voter.name == target.name:
            continue

        score = target.song.jury_score()

        score += random.uniform(-5, 5)

        bias = biases.get(
            (voter.name, target.name),
            0
        )

        score += bias

        ranking.append(
            (target, score)
        )

    ranking.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return ranking


def rank_for_televote(contestants):

    ranking = []

    for country in contestants:

        score = country.song.televote_score()

        score += random.uniform(-10, 10)

        ranking.append(
            (country, score)
        )

    ranking.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return ranking


def jury_voting(contestants):

    for voter in contestants:

        ranking = rank_for_jury(
            voter,
            contestants
        )

        max_awards = min(
            len(POINTS),
            len(ranking)
        )

        for i in range(max_awards):

            country = ranking[i][0]

            country.jury_points += POINTS[i]


def televoting(contestants):

    ranking = rank_for_televote(
        contestants
    )

    max_awards = min(
        len(POINTS),
        len(ranking)
    )

    for i in range(max_awards):

        country = ranking[i][0]

        country.tele_points += POINTS[i]


def print_scoreboard(
    contestants,
    title
):

    ordered = sorted(
        contestants,
        key=lambda x: x.total_points,
        reverse=True
    )

    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)

    for place, country in enumerate(
        ordered,
        start=1
    ):

        print(
            f"{place:>2}. "
            f"{country.name:<12} "
            f"Total:{country.total_points:>4} "
            f"Jury:{country.jury_points:>4} "
            f"Tele:{country.tele_points:>4}"
        )


print("=" * 65)
print("EUROVISION SONG CONTEST SIMULATOR")
print("=" * 65)

random.shuffle(countries)

semi1 = countries[:10]
semi2 = countries[10:]

print("\nRunning Semi Final 1...")

jury_voting(semi1)
televoting(semi1)

semi1_results = sorted(
    semi1,
    key=lambda x: x.total_points,
    reverse=True
)

qualifiers1 = semi1_results[:5]

print_scoreboard(
    semi1,
    "SEMI FINAL 1 RESULTS"
)

print("\nQualified:")

for country in qualifiers1:
    print("-", country.name)

print("\nRunning Semi Final 2...")

jury_voting(semi2)
televoting(semi2)

semi2_results = sorted(
    semi2,
    key=lambda x: x.total_points,
    reverse=True
)

qualifiers2 = semi2_results[:5]

print_scoreboard(
    semi2,
    "SEMI FINAL 2 RESULTS"
)

print("\nQualified:")

for country in qualifiers2:
    print("-", country.name)

grand_final = qualifiers1 + qualifiers2

for country in grand_final:
    country.reset_points()

print("\nRunning Grand Final...")

jury_voting(grand_final)
televoting(grand_final)

print_scoreboard(
    grand_final,
    "GRAND FINAL RESULTS"
)

winner = max(
    grand_final,
    key=lambda x: x.total_points
)

print("\n" + "=" * 65)
print(f"🏆 WINNER: {winner.name}")
print("=" * 65)

print("\nWINNING SONG STATISTICS")
print("-" * 30)

print(
    f"Vocals:      {winner.song.vocals}"
)

print(
    f"Staging:     {winner.song.staging}"
)

print(
    f"Originality: {winner.song.originality}"
)

print(
    f"Catchiness:  {winner.song.catchiness}"
)