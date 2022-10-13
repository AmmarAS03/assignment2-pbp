
## Describe the difference between asynchronous programming with synchronous programming.

Synchronous: 
It is known as a blocking architecture and is ideal for programming reactive systems. As a single-thread model, it follows a strict set of sequences, which means that operations are performed one at a time, in perfect order. While one operation is being performed, other operations’ instructions are blocked. The completion of the first task triggers the next, and so on.
To illustrate how synchronous programming works, think of a telephone. During a phone call, while one person speaks, the other listens. When the first person finishes, the second tends to respond immediately.
Asynchronous: 
Asynchronous programming conversely, is a multithreaded model that’s most applicable to networking and communications. Asynchronous is a non-blocking architecture, which means it doesn’t block further execution while one or more operations are in progress.
With asynchronous programming, multiple related operations can run concurrently without waiting for other tasks to complete. During asynchronous communication, parties receive and process messages when it’s convenient or possible to do so, rather than responding immediately upon receipt.
Texting is an asynchronous communication method. One person can send a text message and the recipient can respond at their leisure. In the meantime, the sender may do other things while waiting for a response.
Sources: https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/

## When Implementing Javascript and AJAX, there is an application in the paradigms of Event-Driven Programming. Describe the reasoning for those paradigms and state some examples of its application.

The event-driven is a programming paradigm where the flow of the program is determined by events like user actions (mouse clicks, key presses), sensor outputs, and message passing from other programs or threads. Asynchronous models are those that include the idea of event-driven programming. We have only worked with sequential or parallel execution paradigms up to this point. The foundation of event-driven programming is an event loop that constantly scans for recently happened events. The operation of event-driven programming depends on events. Once an event has looped, it chooses what to do and how to execute it.
Sources: https://www.tutorialspoint.com/differentiate-between-event-driven-paradigm-and-algorithmic-paradigms

## Describe the implementation of asynchronous programming in AJAX.
AJAX licenses web applications (and browsers) to send and retrieve data from servers asynchronously – from behind the scenes. With AJAX, browsers and other web application parsers do not need to refresh a page and interfere with the display and behavior of that page every time data is manipulated or updated. By dissociating the presentation layer from the interchange layer, AJAX permits web pages and applications to dynamically alter database contents without the need to reload the entire page.
Sources: https://www.nerd.vision/post/ajax-the-asynchronous-programming-paradigm-for-the-asynchronous-mind
