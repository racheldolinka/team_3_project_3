class Caregiver: #basic caregiver class
  def __init__(self, name):
    self.name = name
    self.availability = {}
  def set_availability(self, date, shift, avail_status):
    if date not in self.availability:
            self.availability[date] = {}
        self.availability[date][shift] = avail_status    
#function to generate html calendar
def generate_schedule(caregivers, year, month):
  calen = calendar.monthcalendar(year, month)
# start the HTML calendar structure
    html_calendar = "<html><body><h2>Caregiver Schedule for {}/{}<h2><table border='1'>"
    html_calendar += "<tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr>"    for week in cal:
        
# generate the table rows (one for each week in the month)
#html calendar generated with AI
    for week in calen:
        html_calendar += "<tr>"
        for day in week:
            if day == 0:
                html_calendar += "<td></td>"  # Empty cell for days outside of the current month
            else:
                date_str = f"{year}-{month:02d}-{day:02d}"  # Format the date as YYYY-MM-DD
                current_date = date(year, month, day)  # Create a date object for checking availability
                caregivers_for_day = get_caregivers_for_day(caregivers, current_date)  # Get caregivers for the day
                html_calendar += f"<td>{date_str}<br>{caregivers_for_day}</td>"
        html_calendar += "</tr>"
    # end calendar
    html_calendar += "</table></body></html>"
    return html_calendar
    #end of AI generated html
#helper to get caregivers for each calendar day
def get_caregivers_for_day(caregivers, date_str):
  caregivers_assigned = []#empty list of assigned caregivers
  for caregiver in caregivers: #iterate through 
    if caregiver.availability.get(date_str) and caregiver.availability[date_str].get('AM') == 'available':
        caregivers_assigned.append(f"{caregiver.name} (AM)")#caregiver gets appended to list if avail_status == available
    if caregiver.availability.get(date_str) and caregiver.availability[date_str].get('PM') == 'available':
        caregivers_assigned.append(f"{caregiver.name} (PM)")#caregiver gets appended to list if avail_status == available
    # if no caregivers are assigned, return "No assignment", else return the list of caregivers
  return "<br>".join(caregivers_assigned) if caregivers_assigned else "No assignment"    

# Example usage of generating the HTML calendar
if __name__ == "__main__":
    #define caregivers
    caregiver1 = Caregiver("John Doe")
    caregiver2 = Caregiver("Jane Smith")
    
    #set caregiver availability
    caregiver1.set_availability(date(2024, 11, 19), 'AM', 'available')
    caregiver1.set_availability(date(2024, 11, 19), 'PM', 'unavailable')
    caregiver1.set_availability(date(2024, 11, 20), 'AM', 'available')
    
    caregiver2.set_availability(date(2024, 11, 19), 'AM', 'unavailable')
    caregiver2.set_availability(date(2024, 11, 19), 'PM', 'available')
    caregiver2.set_availability(date(2024, 11, 20), 'AM', 'available')
    
    # list of caregivers
    caregivers = [caregiver1, caregiver2]

# generate calendar for nov 2024
    html_calendar = generate_html_calendar(caregivers, 2024, 11)
    
    # write calendar to html file
    with open("care_schedule_november.html", "w") as file:
        file.write(html_calendar)
