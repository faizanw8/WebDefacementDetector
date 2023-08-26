# WebDefacementDetector
Monitor webpage integrity with a Python script. It fetches a page, compares DOM changes, and alerts if deviations exceed a % threshold. User-defined URL, check interval, and change % for alerts. Basic but adaptable.
 
This script prompts the user for the URL to monitor, the interval at which to check the page, and the change threshold that triggers an alert. It then fetches the page, extracts the DOM structure, compares it with the previous DOM, and triggers an alert if the change ratio exceeds the threshold. Keep in mind that this is a basic example and doesn't cover all possible scenarios and edge cases.
