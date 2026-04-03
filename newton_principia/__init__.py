"""Newton's Principia — derivation of freefall acceleration."""

from gaia.lang import claim, question, setting

# ── Setting ──
near_earth_surface = setting(
    r"Near the Earth's surface: $r \approx R_\oplus$, "
    r"gravitational acceleration can be treated as uniform."
)
near_earth_surface.label = "near_earth_surface"

# ── Empirical foundations ──
kepler_third_law = claim(
    r"Kepler's third law (1619): $T^2 \propto a^3$ for planetary orbits."
)
kepler_third_law.label = "kepler_third_law"

second_law = claim(r"Newton's second law: $\vec{F} = m_i \vec{a}$.")
second_law.label = "second_law"

third_law = claim(r"Newton's third law: $\vec{F}_{AB} = -\vec{F}_{BA}$.")
third_law.label = "third_law"

pendulum_experiment = claim(
    r"Newton's pendulum experiments: all materials have the same period "
    r"to within $1/1000$, implying $m_i \propto m_g$."
)
pendulum_experiment.label = "pendulum_experiment"

# ── Derivation chain ──
inverse_square_force = claim(
    r"Inverse-square law: $F \propto r^{-2}$ for circular orbits.",
    given=[kepler_third_law, second_law],
)
inverse_square_force.label = "inverse_square_force"

law_of_gravity = claim(
    r"Universal gravitation: $F = G\,m_1 m_2 / r^2$.",
    given=[inverse_square_force, third_law],
)
law_of_gravity.label = "law_of_gravity"

mass_equivalence = claim(
    r"Inertial mass equals gravitational mass: $m_i = m_g$.",
    given=[pendulum_experiment, second_law, law_of_gravity],
)
mass_equivalence.label = "mass_equivalence"

freefall_acceleration = claim(
    r"Freefall acceleration: $g = GM_\oplus / R_\oplus^2 \approx 9.8\,\text{m/s}^2$, "
    r"independent of mass.",
    given=[second_law, law_of_gravity, mass_equivalence],
    background=[near_earth_surface],
)
freefall_acceleration.label = "freefall_acceleration"

# ── Question ──
ep_question = question(
    r"Why does $m_i = m_g$ exactly? Einstein's equivalence principle (1907)."
)
ep_question.label = "ep_question"

__all__ = [
    "kepler_third_law", "second_law", "third_law", "pendulum_experiment",
    "inverse_square_force", "law_of_gravity", "mass_equivalence", "freefall_acceleration",
]
