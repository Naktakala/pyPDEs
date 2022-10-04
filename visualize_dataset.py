import os
import sys

import numpy as np
import matplotlib.pyplot as plt

from os.path import splitext

from utils import get_dataset
from utils import get_hyperparams

from readers import NeutronicsDatasetReader

from pyROMs.pod import POD_MCI


def plot_power_span(
        problem: str,
        study: int,
        mode: str = "TOTAL",
        logscale: bool = False,
        filename: str = None
) -> None:
    """
    Plot the bounding power profiles as a function of time.

    Bounding does not imply the minimum and maximum of parameter values.
    In some instances, a parameter may be inversely correlated to reactor
    power. Bounding in this case implies the minimum and maximum powers.

    Parameters
    ----------
    problem : {'Sphere3g', 'InfiniteSlab', 'TWIGL', 'LRA'}
    study : int
    mode : {'TOTAL', 'PEAK', 'AVERAGE'}, default 'TOTAL'
    logscale : bool, default False
    filename : str, default None.
        A location to save the plot to, if specified.
    """
    if mode not in ["TOTAL", "PEAK", "AVERAGE"]:
        raise ValueError(f"{mode} is not a valid mode name.")

    ##################################################
    # Get the data
    ##################################################

    data = get_dataset(problem, study)

    powers = []
    for s, simulation in enumerate(data):
        if mode == "TOTAL":
            if problem == "LRA":
                P = simulation.powers.max()
            else:
                P = simulation.powers[-1]
        elif mode == "PEAK":
            if problem == "LRA":
                P = simulation.peak_power_densities.max()
            else:
                P = simulation.peak_power_densities[-1]
        else:
            if problem == "LRA":
                P = simulation.average_power_densities.max()
            else:
                P = simulation.average_power_densities[-1]
        powers.append(P)

    P_max, P_min = max(powers), min(powers)
    d = (P_max - P_min) / (0.5 * (P_max + P_min))
    power_type = "Peak" if problem == "LRA" else "Final"
    print(f"\n{power_type} Power % Difference:\t{d * 100.0:.3g}")

    d = P_max/P_min - 1.0
    print(f"{power_type} Min-Max % Difference:\t{d * 100.0:.3g}\n")

    ##################################################
    # Plot the bounding cases
    ##################################################

    plt.figure()
    plt.xlabel("Time")
    plt.ylabel("Power" if mode == "TOTAL" else
               "Peak Power Density" if mode == "PEAK" else
               "Average Power Density")

    argmin = int(np.argmin(powers))
    argmax = int(np.argmax(powers))
    for i, s in enumerate([argmax, argmin]):
        simulation = data[s]

        # Get appopriate power quantity
        if mode == "TOTAL":
            P = simulation.powers
        elif mode == "PEAK":
            P = simulation.peak_power_densities
        else:
            P = simulation.average_power_densities

        # Setup plotter
        plotter = plt.semilogy if logscale else plt.plot
        style = '-*b' if i == 0 else '-or'
        label = "Max" if i == 0 else "Min"
        plotter(data.times, P, style, label=f"{label}", ms=3.0)

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    if filename is not None:
        base, ext = splitext(filename)
        plt.savefig(f"{base}.pdf")


def plot_temperature_span(
        problem: str,
        study: int,
        mode: str = "PEAK",
        logscale: bool = False,
        filename: str = None
) -> None:
    """
    Plot the bounding temperature profiles as a function of time.

    Bounding does not imply the minimum and maximum of parameter values.
    In some instances, a parameter may be inversely correlated to the
    fuel temperature. Bounding in this case implies the minimum and
    maximum temperatures.

    Parameters
    ----------
    problem : {'Sphere3g', 'InfiniteSlab', 'TWIGL', 'LRA'}
    study : int
    mode : {'PEAK', 'AVERAGE'}, default 'PEAK'
    logscale : bool, default False
    filename : str, default None.
        A location to save the plot to, if specified.
    """
    if mode not in ["PEAK", "AVERAGE"]:
        raise ValueError(f"{mode} is not a valid mode name.")

    ##################################################
    # Get the data
    ##################################################

    data = get_dataset(problem, study)

    tempratures = []
    for s, simulation in enumerate(data):
        if mode == "PEAK":
            T = simulation.peak_fuel_temperatures.max()
        else:
            T = simulation.average_fuel_temperatures.max()
        tempratures.append(T)

    T_max, T_min = max(tempratures), min(tempratures)
    d = (T_max - T_min) / (0.5 * (T_max + T_min))

    print(f"\n{mode.capitalize()} "
          f"Temperature % Difference:\t{d * 100.0:.3f}\n")

    ##################################################
    # Plot the bounding cases
    ##################################################

    plt.figure()
    plt.xlabel("Time")
    plt.ylabel("Peak Fuel Temperature (K)" if mode == "PEAK" else
               "Average Fuel Temperature (K)")

    argmin = int(np.argmin(tempratures))
    argmax = int(np.argmax(tempratures))
    for i, s in enumerate([argmax, argmin]):
        simulation = data[s]

        # Get appopriate power quantity
        if mode == "PEAK":
            T = simulation.peak_fuel_temperatures
        else:
            T = simulation.average_fuel_temperatures

        # Setup plotter
        plotter = plt.semilogy if logscale else plt.plot
        style = '-*b' if i == 0 else '-or'
        label = "Max" if i == 0 else "Min"
        plotter(data.times, T, style, label=f"{label}", ms=3.0)

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    if filename is not None:
        base, ext = splitext(filename)
        plt.savefig(f"{base}.pdf")


if __name__ == "__main__":

    if len(sys.argv) < 3:
        msg = "Invalid command line arguments. "
        msg += "A problem name and study number must be provided."
        raise AssertionError(msg)

    problem_name = sys.argv[1]
    study_num = int(sys.argv[2])

    reader = get_dataset(problem_name, study_num)
    X = reader.create_2d_matrix(None)
    Y = reader.parameters

    hyperparams = get_hyperparams(problem_name)
    hyperparams["svd_rank"] = 5
    pod = POD_MCI(**hyperparams)

    pod.fit(X.T, Y)

    base = "/Users/zhardy/Documents/Journal Papers/POD-MCI/figures"

    if problem_name == "Sphere3g":
        base = f"{base}/Sphere3g/rom"
        fname = f"{base}/power_span.pdf"
        plot_power_span(problem_name, study_num, filename=fname)

        fname = f"{base}/svd.pdf"
        pod.plot_singular_values(show_rank=True, filename=fname)

        fname = f"{base}/coeffs.pdf"
        pod.plot_coefficients(filename=fname)

        pod.print_summary()

    plt.show()