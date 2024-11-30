class FitnessTracker:
    def __init__(self):
        self.workouts = []
        self.calories_burned = 0

    def add_workout(self, workout, calories):
        self.workouts.append((workout, calories))
        self.calories_burned += calories

    def get_total_calories_burned(self):
        return self.calories_burned

    def display_workouts(self):
        if not self.workouts:
            print("No workouts recorded yet.")
        else:
            print("Workouts:")
            for i, (workout, calories) in enumerate(self.workouts, start=1):
                print(f"{i}. {workout} - {calories} calories")


def main():
    tracker = FitnessTracker()

    while True:
        print("\nFitness Tracker Menu:")
        print("1. Add Workout")
        print("2. Display Workouts")
        print("3. Display Total Calories Burned")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            workout = input("Enter the workout: ")
            calories = int(input("Enter the calories burned: "))
            tracker.add_workout(workout, calories)
            print("Workout added successfully.")
        elif choice == "2":
            tracker.display_workouts()
        elif choice == "3":
            print("Total calories burned:", tracker.get_total_calories_burned())
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()