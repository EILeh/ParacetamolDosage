"""
Paracetamol Dosage
Writer of the program: EILeh
"""

def calculate_dose(weight, time, total_doze_24):
    """
    Reads the user inputs and counts how much paracetamol should a person take.
    :param weight: Person's weight
    :param time: Time that has past since previous doze.
    :param total_doze_24: The doze that the person has taken in last 24 hours.
    :return: The amount of paracetamol that user should take.
    """

    dose_per_weight = 15
    dose_per_kg = weight * dose_per_weight
    max_amount = 4000

    # If six or more hours has passed.
    if time >= 6:

        # If user haven't taken a doze in a last 24 hours then the amount that
        # can be taken is dose_per_kg.
        if total_doze_24 == 0:
            the_amount_of_paracetamol = dose_per_kg

        # The doze that user has taken in last 24 hours is dose_per_kg then the
        # amount that can be taken is dose_per_kg.
        elif total_doze_24 == dose_per_kg:
            the_amount_of_paracetamol = dose_per_kg

        # The amount that can be taken is the total_doze_24 minus max_amount.
        else:
            the_amount_of_paracetamol = max_amount - total_doze_24

    # If less than six hours has passed, then user can't take any doze.
    else:
        the_amount_of_paracetamol = 0


    return the_amount_of_paracetamol

def main():

    weight = int(input("Patient's weight (kg): "))

    time = int(input("How much time has passed from the previous dose "
                     "(full hours): "))
    total_doze_24 = int(input("The total dose for the last 24 hours (mg): "))

    paracetamol = calculate_dose(weight, time, total_doze_24)

    print(f"The amount of Parasetamol to give to the patient: {paracetamol} ")

if __name__ == "__main__":
    main()
