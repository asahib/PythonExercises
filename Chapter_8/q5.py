def workout_coach(lift_name,wt):
  print("Time to", lift_name, wt,"pounds! You got this!")

def main():
  # sys.setExecutionLimit(120000) # keep program from timing out
  lifts = ["squat", "bench", "deadlift"]
  for lift in lifts:
    weight = 10
    user_input = "Yes"
    while user_input =='Yes' or user_input == 'yes':
      if lift == "bench" and weight > 200:
        break
      else:
        workout_coach(lift, weight)
        weight += 10
        user_input = input("Keep doing the " + lift + "? Enter yes for the next set.")

if __name__ == "__main__":
  main()
