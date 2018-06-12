def get_clock_in_out():
  worker={}
  while True:
    name = input ("Please enter the workers name\n>>")
    clock_in = int(input(f"Enter the {name}'s clock in time (24 hrs) \n>>"))
    clock_out = int(input(f"Enter the {name}'s clock out time (24 hrs) \n>>"))
    if clock_in > 24 or clock_out > 24:
      print("Please enter the info again, since you entered an invalid time (>24Hrs)")
      continue
    worker[name]={'clockin':clock_in,'clockout':clock_out}
    continue_or_not = input(f"Do you want to continue entering another worker details (y/n)? ")
    if continue_or_not == 'n':
      break
  return worker

def print_worker_details(worker):
  for name, time in worker.items():
    clockout = time['clockout']
    clockin = time['clockin']
    total_hours_worked = clockout - clockin if clockout > clockin else 24 - (clockin - clockout)
    print(f"Name : {name}\tClock In : {clockin}:00\tClock Out : {clockout}:00\tTotal Hours : {total_hours_worked} hours")

def main():
  workers = get_clock_in_out()
  print_worker_details(workers)

if __name__ == '__main__':
  main()
  
    