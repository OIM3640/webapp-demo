import math


class NoRealRootsError(Exception):
    """Exception raised when a quadratic equation has no real roots."""

    pass


def quadratic(a: float, b: float, c: float) -> tuple[float, float]:
    """
    Solve a quadratic equation of the form ax^2 + bx + c = 0.

    Parameters:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        tuple[float, float]: A tuple of two real roots if they exist.

    Raises:
        ValueError: If 'a' is zero.
        NoRealRootsError: If no real roots exist.
    """
    if a == 0:
        raise ValueError(
            "Coefficient 'a' must be nonzero for a valid quadratic equation."
        )

    discriminant = b**2 - 4 * a * c  # calculate the discriminant

    if discriminant >= 0:  # equation has solutions
        x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x_1, x_2
    else:
        raise NoRealRootsError("No real solutions exist for the given coefficients.")


def main():
    try:
        a = float(input("please enter a number:"))
        b = float(input("please enter a number:"))
        c = float(input("please enter a number:"))
        sol_1, sol_2 = quadratic(a, b, c)
        print(f"The two roots are: {sol_1}, {sol_2}.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except NoRealRootsError as nre:
        print(f"NoRealRootsError: {nre}")


if __name__ == "__main__":
    main()
