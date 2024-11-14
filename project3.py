from datetime import datetime
from collections import defaultdict

#creates the caregiver class and sets the payrate 
class Caregiver:
    def __init__(self, name, pay_rate=20):
        self.name = name
        self.pay_rate = pay_rate
        self.scheduled_hours = defaultdict(int)

    #allows administrator to add hours for all the caregivers
    def add_hours(self, hours, week_start_date):
        self.scheduled_hours[week_start_date] += hours

    #calculates the weekly pay for each caregiver
    def weekly_pay(self, week_start_date):
        return self.scheduled_hours[week_start_date] * self.pay_rate

#creates the schedule class
class Schedule:
    def __init__(self):
        self.caregivers = []

    #adds a caregiver to the schedule
    def add_caregiver(self, caregiver):
        self.caregivers.append(caregiver)

    #generates the weekly pay report for the caregivers
    def generate_pay_report(self, week_start_date):
        report = f"Weekly Pay Report - Week Starting {week_start_date.strftime('%Y-%m-%d')}\n"
        report += "-" * 40 + "\n"
        
        #calculates their total pay
        total_pay = 0
        for caregiver in self.caregivers:
            weekly_pay = caregiver.weekly_pay(week_start_date)
            report += f"Caregiver: {caregiver.name}\n"
            report += f"  Hours: {caregiver.scheduled_hours[week_start_date]} hrs\n"
            report += f"  Pay: ${weekly_pay:.2f}\n\n"
            total_pay += weekly_pay

        #combines the pay of all caregivers to keep track of finances
        report += "-" * 40 + "\n"
        report += f"Total Weekly Pay of All Caregivers: ${total_pay:.2f}\n"
        return report

#the execution code
caregiver1 = Caregiver("Jane Doe")
caregiver2 = Caregiver("John Smith")

#a default week start date
week_start_date = datetime(2024, 1, 1)

#adds the caregiver hours to the schedule
caregiver1.add_hours(36, week_start_date)
caregiver2.add_hours(24, week_start_date)

#adds the caregivers to the schedule
schedule = Schedule()
schedule.add_caregiver(caregiver1)
schedule.add_caregiver(caregiver2)

#creates the payreport
pay_report = schedule.generate_pay_report(week_start_date)
print(pay_report)
