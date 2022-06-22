---
title: Navigation
---

# Navigation

QField offers navigation functionalities to help orient yourself in the field and accurately reach a given destination.

## Activating navigation 

Navigation is enabled when [a destination point has been set](#setting-a-destination-point) and positioning is active. When turned on, a set of navigation overlays - a destination marker, a navigation panel, and a navigation control button - appear over the map.

!![](../assets/images/navigation.png)

The navigation panel displays useful information such as the destination point coordinates as well as the current distance and bearing to destination.

To disable navigation, clear the destination point by tap and holding on the navigation control button located at the lower right corner.

## Setting a destination point
:material-tablet-android:{ .device-icon } Fieldwork

QField offers several methods to set a navigation destination point. A quick way is to simply tap and hold on any part of the map and select the *Set as Destination* action within the popped up menu.

!![](../assets/images/navigation-add-from-touch.png)

You can also set the navigation destination point by typing in specific coordinates in the search bar and tapping on the resulting flag navigation icon. You can also search for a specific feature and tap on the flag navigation icon which will also be present in the resulting list of features.

!![](../assets/images/navigation-search-bar.png)

Finally, you can also set a navigation destination point by opening the feature form menu and selecting the *Set Feature as Destination* action.

!![](../assets/images/navigation-destination-feature-form.png)

!!! note
    When the selected feature as destination has a line or polygon geometry, a point on the geometry's surface will be used to navigate to that feature.

## Auto tracking of current location and destination
:material-tablet-android:{ .device-icon } Fieldwork

QField allows for its map to automatically keep track of the current device location and destination and re-center the map extent around those two points.

To activate this auto tracking feature, you can simply tap on the positioning button and the navigation control button. Both buttons should show their auto tracking mode active by having their background color turn to blue and purple.

!![](../assets/images/navigation-auto-tracking.png)

This can be described as a simple *staking mode* functionality.
