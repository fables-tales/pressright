#include <ApplicationServices/ApplicationServices.h>

int main() {
CGEventRef event1, event2, event3, event4;
event1 = CGEventCreateKeyboardEvent (NULL, (CGKeyCode)124, true);
event4 = CGEventCreateKeyboardEvent (NULL, (CGKeyCode)124, false);
CGEventTapLocation loc =    kCGSessionEventTap;
CGEventPost(loc, event1);
CGEventPost(loc, event4);
return 0;
}
