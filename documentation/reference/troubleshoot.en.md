---
title: Troubleshoot
tx_slug: documentation_how-to_troubleshoot
---

# How to troubleshoot

When encountering issues or unexpected behavior in QField, the application provides a set of tools to help you diagnose and report problems.
This guide will walk you through how to use these tools to troubleshoot effectively.

## Official QFieldCloud Status Page

The official [QFieldCloud Status](https://status.qfield.cloud/)<!-- markdown-link-check-disable-line -->
Page provides real-time information on the service's operational status.

You can use the status page to check for:

- **Current System Status:** See if all services are running normally.
- **Ongoing Incidents:** Get details on any active issues the team is working to resolve.
- Scheduled Maintenance: Find out about planned maintenance that might temporarily affect service availability.

This page can quickly tell you if the problem you're experiencing is part of a wider issue.

In the event of a service disruption or degraded performance, an incident banner will pop-up on the top of your QFieldCloud admin dashboard and be permanently displayed until the incidence has been resolved.
The banner will provide a brief description of the issue, a timestamp, and a link to the status page for more comprehensive information.

!![](../assets/images/qfc_incident_banner.png,800px)

## How to troubleshoot in QField

To access the troubleshooting and logging tools within QField:

1. Open your project in QField.
2. Tap the menu (☰) on the top-left corner to reveal the side "Dashboard".
3. Tap the 3-dotted menu *(⋮)* button.
4. Select **Message Log**.

!![](../assets/images/accessing_message_log.png,300px)

This will open the main screen for all troubleshooting utilities.

## Understanding the Message Log

The **Message Log** displays a real-time log of events, warnings, and errors that occur while QField is active.

- **Reviewing Issues:** If you notice any problems with your project (not all layers within the project are loading or features are not saved correctly) the Message Log is the first place to check.
It often contains specific error messages that can help to identify the cause of the problem.
- **Copying Messages:** To get more details or to share an error message, tap on the according entry in the log.
This will copy the message directly to the clipboard of your device.

!![](../assets/images/copy_logs_to_clipboard.png,300px)

## Advanced Troubleshooting

For more complex issues, QField provides additional tools to gather more detailed information about your device and the configuration of a specific project.

### Application Performance

The **Log runtime profile** button captures a snapshot of the application's performance at that moment.
This includes information about your current project.

**When to use it:** If you are experiencing slow performance, lagging, or freezing, generating a runtime profile can provide valuable data to you and the developers to understand how QField is interacting with your project and layers.

!![](../assets/images/log_runtime_profiler.png,300px)

### Submit a Bug Report

To easily receive support from the QField development team is by sending the application logs of your device.

- **Send the application log:** This button packages the detailed application log files and directly sends them to the QField development team.
When you send the logs, you will be asked to add a description of the issue.

- **Provide Context:** Please describe the problem you are experiencing providing as much context as possible.
Include a step by step description of what you did until the issue occurred.
Do not forget to mention the version of QField, QFieldSync and QGIS that you were using.
- **Reference Existing Issues:** If you have already opened a discussion or a bug report on the [community's platform](https://github.com/opengisch/QField/issues), include the link in your message.
This helps the developers to link your log files to the appropriate report.

!![](../assets/images/send_application_log.png,300px)

### Log Management

- **Clearing the Log:** The **Clear message log** button will erase all current messages in the log.
This is helpful when you want to isolate a specific issue.
By clearing the log before you perform an action that causes a problem, you can ensure that the subsequent log messages are relevant to that specific issue.

### Contribution to QField

You can help to improve the stability and performance of QField by enabling the **Send anonymized metrics** option.

By turning this on, you allow the QField team to collect data about how the app is used and where it might be encountering problems on a wider range of devices and scenarios.
Sending these metrics does not include any personal information.
This information is crucial for identifying and fixing bugs and for making informed decisions about future development priorities.

!![](../assets/images/send_anonymized_metrics.png,300px)
