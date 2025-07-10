---
title: Troubleshoots
tx_slug: documentation_how-to_troubleshoot
---


## Troubleshooting in QField

When encountering issues or unexpected behavior in QField, the application provides a set of tools to help you diagnose and report problems. This guide will walk you through how to use these tools to troubleshoot effectively.

### Accessing the Troubleshooting Tools

To access the troubleshooting and logging tools within QField:

1. Open any project in the QField app.
2. Tap the hamburger menu icon (three horizontal lines) in the top-left corner to reveal the side panel.
3. Tap the three-dotted menu button.
4. Select **Message Log** from the menu.

!![](../assets/images/accessing_message_log.png,300px)

This will open the main screen for all troubleshooting utilities.

### Understanding the Message Log

The **Message Log** are condensed in the troubleshooting section. It displays a real-time log of events, warnings, and errors that occur during your QField session.

- **Reviewing Issues:** If you notice any problems with your project, such as layers not loading or features not saving correctly, the Message Log is the first place to check. It often contains specific error messages that can help you or the QField developers pinpoint the cause of the problem.
- **Copying Messages:** To get more details or to share an error message, tap on a specific entry in the log. This will copy it to your device's clipboard. This is useful when reporting an issue.

!![](../assets/images/copy_logs_to_clipboard.png,300px)

### Advanced Troubleshooting

For more complex issues, QField provides advanced tools to gather more detailed information about your device and project configuration.

#### Profiling Application Performance

The **Log runtime profile** button captures a snapshot of the application's performance at that moment. This includes information about your current project.

**When to use it:** If you are experiencing slow performance, lagging, or freezing, generating a runtime profile can provide valuable data to you and the developers to understand how QField is interacting with your project and layers.

!![](../assets/images/log_runtime_profiler.png,300px)

#### Submitting a Bug Report

The most direct way to get help from the developers is to send them the application logs.

- **Send the application log:** This button packages the detailed application log files and allows you to send them directly to the QField development team. When you send the logs, you will be prompted to add a description of the issue, more details are helpful.

**Best practices for sending logs:**

- **Provide Context:** Clearly and concisely describe the problem you are experiencing. Include the steps you took that led to the issue.
- **Reference Existing Issues:** If you have already opened a discussion or a bug report on the community, include the link in your message. This helps the developers connect your log files to the appropriate report.

!![](../assets/images/send_application_log.png,300px)

### Managing the Log

- **Clearing the Log:** The **Clear message log** button will erase all current messages in the log. This is helpful when you want to isolate a specific issue. By clearing the log before you perform an action that causes a problem, you can ensure that the subsequent log messages are relevant to that specific issue.

### Contributing to QField's Improvement

You can help improve the stability and performance of QField by enabling the **Send anonymized metrics** option.

By turning this on, you allow the QField team to collect non-personally identifiable data about how the app is used and where it might be encountering problems on a wider range of devices and scenarios.
This information is crucial for identifying and fixing bugs and for making informed decisions about future development priorities.
Your privacy is respected, and no personal data is collected.

!![](../assets/images/send_anonymized_metrics.png,300px)
