# 2 December proposal meetings: booking setup

Use one appointment-schedule URL in the public course book. The scheduling service should send each student a separate calendar invitation and video link. Do not post individual meeting URLs on the public site.

## Recommended setup: NYU Google Calendar

1. On a computer, sign in to your NYU Google Calendar and select **Create → Appointment schedule**.
2. Title it **Final research-design memo meeting**. Offer **15-minute appointments** on **Wednesday 2 December 2026, 9:30 a.m.–12:00 p.m. Eastern**. Ten students can book within that window; the final 15 minutes of class remain available if a meeting runs over. If enrollment exceeds ten, add another availability window.
3. Restrict availability to this date, check your calendar for conflicts, and set the booking window so students can reserve a slot before 2 December.
4. Choose **Google Meet** as the location. Require a name and email address; ask for the student's project title only if useful. Add a description reminding them to submit the final memo before their appointment and bring an input–operation–output example.
5. Save. Under **Booking pages**, copy the link for this appointment schedule. Test it in a private browser window, confirm that the intended slots appear, and make one test reservation to check that the confirmation includes a video link. Cancel the test reservation.
6. Add the booking URL to `coursebook/weeks/session13.qmd` in the **Book your meeting** section, replacing the sentence that says the link will be added. Render the course book and publish the update.

Google's current instructions: [create an appointment schedule](https://support.google.com/calendar/answer/10729749) and [copy its booking-page link](https://support.google.com/calendar/answer/10733297).

If meetings must use Zoom, use a Calendly booking page connected to your NYU Zoom account, if available. Alternatively choose **None/to be specified later** as the Google Calendar location, then add a separate Zoom meeting to each booked calendar event. Avoid a shared Zoom URL for confidential individual consultations.
