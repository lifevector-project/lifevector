# 1. CORE APPLICATION CONCEPTS

`LifeVector` shall be built around the following concepts:

### Mission Statement

Defines the user's overall direction and provides a reference point during planning.

### Roles

A **role** represents an important area of responsibility or contribution in the user's life.

Examples include:

* Student
* Programmer
* Family Member
* Friend
* Personal Development

Roles provide the context in which goals are created and reviewed.

Every goal shall belong to a role. This allows the user to consider their responsibilities as a whole rather than focusing only on isolated tasks.

During Guided Weekly Planning, `LifeVector` shall encourage the user to review their active roles and consider whether each important area of responsibility is receiving appropriate attention, particularly through **Quadrant II** goals.

Each role has:

* `id`
* `name`
* `description`
* `sort_order`
* `status`

A newly created role is active by default.

An inactive role is retained in the database and preserves the history and role association of its existing goals, but it is not normally available when creating new goals.

Roles are therefore not merely categories for organizing tasks. They represent the **responsibilities and areas of life from which the user's goals originate**.

---


### Goals and Activities

A **goal** is something the user intends to achieve. It represents a desired outcome, objective,responsibility or a task.

A goal may exist independently of its:

* Priority classification
* Current-week selection
* Day allocation
* Exact schedule

Consequently, a goal can progress through planning stages without requiring all stages to be completed at once.

For example:

`Goal → Prioritized → Selected for Week → Allocated to Day → Scheduled`

A goal may therefore:

* exist without a priority classification;
* be classified without being selected for the current week;
* be selected for the week without being allocated to a particular day;
* be allocated to a day without an exact time;
* eventually receive an exact date and start time.

#### Activities and Subgoals

A goal may contain zero or more **activities** that contribute to achieving it. An activity is same as a subtask.

For example:

```text
Goal: Prepare for Physics Exam
    ├── Read Chapter 5
    ├── Solve Chapter 5 exercises
    └── Review formulas
```

Activities function as the actionable components of a goal.

The parent goal and its activities may be scheduled independently when appropriate.

When a goal or activity is assigned a specific date and time for execution, it is represented by a **scheduled activity** in the application's scheduling model.

For example:

```text
Goal:
    Prepare for Physics Exam

Activity:
    Read Chapter 5

Scheduled Activity:
    Read Chapter 5
    Monday, 5:00 PM – 6:00 PM
```

A goal does not have to contain activities, and neither a goal nor an activity has to be scheduled.

#### Goal Properties

A goal has, at minimum:

* Unique ID
* Role
* Title
* Optional description
* Priority classification
* Completion status
* Creation date
* Optional estimated duration
* Optional date/day allocation
* Optional exact start time
* Zero or more activities/subgoals

The goal's **priority** answers:

> *How important/urgent is this?*

Its **weekly selection** answers:

> *Does this deserve attention this week?*

Its **day allocation** answers:

> *Which day will I work on it?*

Its **exact schedule** answers:

> *When exactly will I do it?*

Keeping these concepts separate is fundamental to `LifeVector`.

#### Goal and Covey's Planning Concept

In accordance with Covey's **Put First Things First** approach, the application shall emphasize important activities—particularly **Quadrant II: important but not urgent**—before the user's calendar becomes filled with urgent demands.

The intended planning progression is therefore:

`Mission → Roles → Goals → Quadrant II Prioritization → Weekly Planning → Day Allocation → Scheduling`

The purpose is not simply to schedule more tasks. It is to help the user deliberately give time and attention to the responsibilities and goals that matter most.

---

### Priority Quadrants

Classify goals according to the Eisenhower/Covey urgency-importance framework:

| Value | Classification             |
| ----: | -------------------------- |
|   `0` | Unclassified               |
|   `1` | Urgent & Important         |
|   `2` | Not Urgent & Important     |
|   `3` | Urgent & Not Important     |
|   `4` | Not Urgent & Not Important |

### Weekly Priorities

Goals classified as important for the upcoming week, particularly Quadrants I and II, become candidates for weekly planning.

### Day Allocation

Assigns a weekly priority to a particular day without necessarily assigning an exact time.

### Scheduling

Assigns an exact start time and estimated duration.

### Planner

Provides the seven-day visual time grid through which day allocation and exact scheduling are performed.

### Guided Weekly Planning

Guides the user through the process of reconnecting with their mission, reviewing roles, prioritizing goals, estimating time, allocating goals to days, and finally scheduling them.

### Drag and Drop

Provides direct manipulation for operations such as:

* Changing a goal's priority quadrant
* Allocating a goal to a day
* Scheduling a goal at a particular time
* Changing an existing scheduled time
* Adjusting duration

### Lists and Tables

Used where appropriate for roles, goals, priorities, settings, and historical information.

### Stacked Interfaces

The application shall use a consistent navigation structure so that the major interfaces—TODAY, WEEK, ROLES, MATRIX, PLANNER, MISSION STATEMENT, and PREFERENCES—can be accessed without opening multiple independent application windows unnecessarily.

### Calendar Integration

The architecture should allow future integration with external calendars without making calendar integration a requirement for the core offline planner.

### Themes and Accessibility

The UI shall support light/dark themes and configurable font size. The interface should remain usable on smaller displays and with keyboard navigation.

---




# 2. TECH STACK

The initial implementation shall target:

**Linux**

The technology stack shall prioritize:

* Offline/local-first operation
* Low system-resource requirements
* Maintainability
* Modern desktop UI
* Clear separation of application logic from platform-specific functionality
* Future portability to Android and Windows

## 2.1 Core Technologies

### Database

**SQLite**

### Programming Language

**Python**

### Framework

**Flet**


### Version Controling System

**Git**

### Project Management System

**uv**

### Linter and formatter

**Ruff**


# 3. ARCHITECTURAL PRINCIPLE

The application shall maintain a clear separation between:

```text
UI / Presentation
        ↓
Application / Business Logic
        ↓
Data Access
        ↓
SQLite Database
```

Platform-specific services shall be accessed separately:

```text
Application
    ↓
Platform Integration Layer
    ├── Linux
    ├── Android (future)
    └── Windows (future)
```

The core concepts of **roles, goals, activities, priorities, weekly planning, day allocation, and scheduling** shall not depend on Linux-specific APIs.

This architecture shall allow the initial Linux application to remain lightweight while providing a practical path toward future Android and Windows versions.



# SPECIFICATION:

# 1. WELCOME Wizard Interface

The **WELCOME Wizard** is displayed the first time the user opens `LifeVector`. Its purpose is to guide the user through the initial configuration of the application according to their preferences.

### 1.1 Wizard Stages

1. **Welcome** — Introduction to `LifeVector`.
2. **Mission Statement** — Optionally create a personal mission statement.
3. **Roles** — Add the user's initial roles.
4. **Default Role** — Select the default role for new goals.
5. **Week Settings** — Configure the first day of the week.
6. **Planning Day** — Choose the day on which weekly planning is performed.
7. **Day Hours** — Set the beginning and ending hours of the user's day.
8. **Appearance** — Choose the theme and font size.
9. **Finish** — Confirm that the initial setup is complete.

### 1.2 Navigation

* **NEXT** moves to the next stage.
* **BACK** returns to the previous stage.
* **SKIP SETUP** exits the wizard and retains the application's default preferences.
* The wizard should preserve entered values when moving between stages.
* On completion, the configured preferences are saved and the main application interface is displayed.


## 2. Navigation Bar

`LifeVector` shall provide a vertical navigation bar on the left side of every interface. Its design should be inspired by the Activity Bar in Visual Studio Code.

The navigation bar is the primary graphical method for navigating between the application's interfaces.

### 2.1 Displaying Interface Shortcuts

The navigation bar shall display shortcuts for interfaces in the `interfaces` table of the `LifeVector` database that meet the following conditions:

* `is_active = 1`

Examples of interfaces include:

* TODAY
* WEEK
* ROLES
* TIME MANAGEMENT MATRIX
* PLANNER

The shortcuts shall be displayed in ascending order of `sort_order`, starting with the lowest value.

The navigation bar shall display no more than six interface shortcuts. The PREFERENCES option is excluded from this limit.

If more than six interfaces meet the eligibility conditions, the application shall display the six eligible interfaces with the lowest `sort_order` values.

### 2.2 Preferences Shortcut

A gear icon shall always appear at the bottom of the vertical navigation bar. Selecting this icon shall open the PREFERENCES interface.

The PREFERENCES icon is not included in the six-shortcut limit.

### 2.3 Opening an Interface

Selecting an interface shortcut shall open its corresponding interface.

### 2.4 Removing a Shortcut

The user shall be able to remove an interface shortcut from the navigation bar through the bar's context menu by selecting **Remove**.

Removing a shortcut shall set that interface's `is_active` property to `0`. 

---

## 3. TODAY Interface

The TODAY interface shall display scheduled activities for the current date, organized under a tab bar containing two tabs: **PENDING** and **COMPLETED**.

TODAY shall be the default interface displayed when the application launches. When TODAY is opened, the **PENDING** tab shall be selected by default.

### 3.1 PENDING Tab

The PENDING tab shall display scheduled activities that meet both of the following conditions:

* `start_date = CURRENT_DATE`
* `status = not_completed`

### 3.2 COMPLETED Tab

The COMPLETED tab shall display scheduled activities that meet both of the following conditions:

* `start_date = CURRENT_DATE`
* `status = completed`

Each completed entry should display relevant information, such as its title, role, and completion date, when that information is available.

### 3.3 Completing and Reopening

Each entry shall provide a checkbox icon.

* Selecting the checkbox on the PENDING tab shall set `status = completed` and record the completion date. The entry shall move to the COMPLETED tab.
* Selecting the checkbox on the COMPLETED tab shall set `status = not_completed` and clear the completion date. The entry shall move back to the PENDING tab.

### 3.4 Empty State

If a tab has no entries to display, it shall show an appropriate empty state.

---

## 4. WEEK Interface

The WEEK interface shall display scheduled activities for the current week, organized under the same tab bar as the TODAY interface: **PENDING** and **COMPLETED**.

When WEEK is opened, the **PENDING** tab shall be selected by default.

`CURRENT_WEEK` shall be determined by the week-calculation function defined in Section 13, which returns the start and end dates of the current week.

### 4.1 PENDING Tab

The PENDING tab shall display scheduled activities that meet both of the following conditions:

* the scheduled date falls within `CURRENT_WEEK`
* `status = not_completed`

### 4.2 COMPLETED Tab

The COMPLETED tab shall display scheduled activities that meet both of the following conditions:

* the scheduled date falls within `CURRENT_WEEK`
* `status = completed`

### 4.3 Completing and Reopening, and Empty State

Completing, reopening, and empty-state behavior shall be identical to Sections 3.3 and 3.4.

---


## 5. CONTEXT MENU

A context menu shall be available for supported items when the user invokes the platform’s context-menu action, such as right-clicking an item.

The available operations shall depend on the selected item and the active interface. The application shall not display an operation that is unavailable or invalid for that item.

### 5.1 Goal Context Menu

For a goal, the context menu shall provide:

* **Edit:** Open the Add/Edit Goal interface with the selected goal’s current information.
* **Remove:** Remove the goal from active use, using the application’s defined non-destructive removal method.
* **Mark as Completed:** Mark the goal as completed, where applicable.

If the selected goal has scheduled activities, the  removing or completing the goal also affects those activities. 

### 5.2 Role Context Menu

For a role, the context menu shall provide:

* **Edit:** Open the role editor with the selected role’s current information.
* **Remove:** Set the role’s `is_active` property to `0`.

Removing a role shall not permanently delete it or its associated goals. Inactive roles shall remain visible in the ROLES interface but shall not be available for selection as a default role or for creating new goals.

If a role has associated goals, the application shall preserve those goals and their role association when the role is deactivated.

### 5.3 Navigation Shortcut Context Menu

For an interface shortcut in the navigation bar, the context menu shall provide **Remove**.

Selecting **Remove** shall set the corresponding interface’s `is_active` property to `0`.

The shortcut shall disappear from the navigation bar. The user shall be able to restore it through the Navigation settings in PREFERENCES.

The PREFERENCES shortcut shall not provide a Remove operation.

---

## 6. ADD TASK BUTTON

A plus icon shall be available on every interface. Its exact position shall be determined during UI design.

The plus icon shall perform an action appropriate to the currently active interface. It shall not always create a goal.

Examples:

* **TODAY:** Open the Add/Edit Goal interface to create a goal.
* **WEEK:** Open the weekly-planning workflow.
* **ROLES:** Open the Add Role interface.
* **TIME MANAGEMENT MATRIX:** Open the Add/Edit Goal interface to create a goal.
* **PLANNER:** Open the appropriate activity or scheduling interface.

The application shall provide an accessible label or tooltip describing the action of the plus icon on the current interface.

---

## 7. ROLES interface

The ROLES interface shall display all roles, including active and inactive roles.

Roles shall be displayed in ascending order of `sort_order`, with the lowest value appearing first.

Each role entry shall clearly indicate whether the role is active or inactive.

### 7.1 Adding a Role

Selecting the plus icon on the ROLES interface shall open the Add Role interface. The Add Role interface can also be opened using Add Role operation from ROLES interface's context menu

The user shall be able to enter the role’s required information as mentioned-above and save the role to the database.

### 7.2 Deactivating a Role

The role context menu shall include a **Deactivate** operation.

Selecting **Deactivate** shall set `is_active = 0`. The role shall remain in the database and continue to appear in the ROLES interface as inactive.

The application shall preserve goals associated with the role. Deactivating a role shall not permanently delete the role or its goals.

---

## 8. MISSION STATEMENT interface

The MISSION STATEMENT interface shall display the user’s current mission statement.

The interface shall provide a graphical way such as through the context menu or through specific action button to create or edit the mission statement. Saving changes shall update the stored mission statement.

If no mission statement has been entered, the interface shall display an appropriate empty state and provide an action to create one.

---


## 10. TIME MANAGEMENT MATRIX

The TIME MANAGEMENT MATRIX interface shall contain two main elements:

1. **Unsorted Goals**
2. **TIME MANAGEMENT MATRIX board**

### 10.1 Unsorted Goals

The Unsorted Goals section shall display every role and its associated goals where:

* `priority_quadrant = 0`
* 'status = not_completed'

Goals shall be grouped under their respective roles.

The section shall include goals associated with active roles. The inactive roles are hidden.

### 10.2 TIME MANAGEMENT MATRIX Board

The eisenhower board called TIME MANAGEMNT MATRIX shall contain four quadrants. Each quadrant shall represent a priority category.

| `priority_quadrant` | Quadrant name              |
| ------------------: | -------------------------- |
|                 `0` | Unclassified               |
|                 `1` | Urgent & Important         |
|                 `2` | Not Urgent & Important     |
|                 `3` | Urgent & Not Important     |
|                 `4` | Not Urgent & Not Important |

The four numbered quadrants shall be displayed as a two-by-two board:

* **Urgent & Important:** upper-left
* **Not Urgent & Important:** upper-right
* **Urgent & Not Important:** lower-left
* **Not Urgent & Not Important:** lower-right

The Unclassified category (`priority_quadrant = 0`) shall be represented by the Unsorted Goals section, not by a fifth quadrant on the board.

### 10.3 Moving Goals Between Categories

The user shall be able to drag a goal from the Unsorted Goals section into any quadrant.

The user shall also be able to drag a goal from one quadrant to another.

When a goal is dropped into a quadrant, the application shall immediately update its `priority_quadrant` value to the value assigned to that quadrant.

Moving a goal back to the Unsorted Goals section shall set `priority_quadrant = 0`.

The application shall save each change to the database. If saving fails, the UI shall restore the goal to its previous location and inform the user.

Dragging shall not change the goal’s role, title, completion status, or scheduled activities.

---

## 11. PREFERENCES interface

The PREFERENCES interface shall provide the following settings. Every setting is
stored as an individual key-value pair as described in Section 11.6.

### 11.1 Appearance

#### 11.1.1 Theme

The user shall be able to choose between:

* Light (`theme = 0`)
* Dark (`theme = 1`)

The selected theme shall be applied throughout the application.

#### 11.1.2 Font Size

The user shall be able to select a supported font size. The application shall provide
a defined set of size options and apply the selected size throughout the interface.
The selection is stored in the `font_size` preference.

### 11.2 Week Settings

#### 11.2.1 First Day of the Week

The user shall be able to select the first day of the week from a list containing all
seven days. The selection is stored in the `day_starting_week` preference.

The selected day shall determine the start and end of the week used by the WEEK
interface and weekly planning.

#### 11.2.2 Guided Weekly Planning Helper

A toggle shall enable or disable the Guided Weekly Planning Helper. The selection is
stored in the `helper` preference.

When enabled, the application shall offer the guided weekly-planning workflow at the
configured planning time.

When disabled, the application shall not automatically initiate or prompt the user to
begin guided weekly planning.

#### 11.2.3 Weekly Planning Day

The user shall be able to select the day on which they would like to plan their week.
The selection is stored in the `planning_day` preference and is used by the Guided
Weekly Planning Helper when it is enabled.

### 11.3 Day and Hour Settings

#### Day Starts At

The user shall be able to set the start of their day using the format `HH:MM:SS`.
This setting updates the `time_starting_day` preference.

#### Day Ends At

The user shall be able to set the end of their day using the format `HH:MM:SS`.
This setting updates the `time_ending_day` preference.

The application shall validate both values as valid times. The end time must be later
than the start time.

### 11.4 Goal Settings

#### 11.4.1 Default Role

The user shall be able to select a default role from a list of active roles. The
selection is stored in the `default_role` preference as a role `id`.

Only active roles shall be available for selection.

If the currently selected default role is deactivated, the application shall remove
the `default_role` preference or ask the user to select another active role.

#### 11.4.2 Default Duration

The user shall be able to set a default duration using the format `HH:MM:SS`. The
selection is stored in the `default_duration` preference.

The value shall represent an estimated duration, not a time of day. It must be valid
and greater than zero.

#### 11.4.3 Default Start Interface

The user shall be able to select a default start interface from a dropdown list. The
selection is stored in the `default_interface` preference.

The list shall contain active interfaces. The selected interface shall be displayed
when the application launches.

If the selected interface is later deactivated, the application shall fall back to a
valid active interface, with TODAY as the default fallback.

### 11.5 System Integration (Advanced, optional, later)

#### 11.5.1 Run in Background

A toggle shall enable or disable running the application in the background after its
main window is closed. Stored in the `run_in_background` preference.

#### 11.5.2 Run on Startup

A toggle shall enable or disable launching the application automatically when the
user signs in. Stored in the `startup_integration` preference.

The application shall apply this setting only where the operating system supports it.

#### 11.5.3 Clock Format

The user shall be able to select one of the following clock formats:

* 12-hour
* 24-hour

The selection is stored in the `clock_format` preference. The selected format shall be
used when displaying times throughout the application. Stored times shall use a
consistent internal format independent of this display preference.

### 11.6 Preference Storage

The application shall store user preferences using Flet's `ft.SharedPreferences` as
individual key-value pairs. Preferences shall not be stored in the SQLite database.

| Key                   | Type    | Default        | Notes                                      |
| --------------------- | ------- | -------------- | ------------------------------------------ |
| `theme`               | integer | `0`            | `0` = Light, `1` = Dark                    |
| `font_size`           | integer | `14`           |                             |
| `day_starting_week`   | string  | `"MONDAY"`     |                                            |
| `planning_day`        | string  | `"SUNDAY"`     |                                            |
| `helper`              | boolean | `true`         |                               |
| `time_starting_day`   | string  | `"08:00:00"`   | `HH:MM:SS`                                 |
| `time_ending_day`     | string  | `"22:00:00"`   | `HH:MM:SS`                                 |
| `mission_statement`   | string  | `""`           | See Section 11.9                           |
| `default_role`        | integer | not set        | A role `id`; absent means no default role  |
| `default_duration`    | string  | `"00:15:00"`   | `HH:MM:SS`                                 |
| `default_interface`   | string  | `"TODAY"`      |                              |
| `startup_integration` | boolean | `false`        |                               |
| `run_in_background`   | boolean | `false`        |                               |
| `clock_format`        | integer | `24`           | `12` or `24`                  |
| `setup_completed`     | boolean | `false`        | Set to `true` when the WELCOME Wizard ends or is skipped 

### 11.7 Default Preferences

The application shall initialize missing preferences with their specified default
values.

Existing user preferences shall not be overwritten when the application starts.

If a preference is missing or contains an invalid value, the application shall use its
corresponding default value and correct the stored value.

### 11.8 Preference Removal and Reset

The application shall support removing individual preferences when required.

The application shall also support resetting all preferences to their default values.

Resetting preferences shall not remove unrelated application data or user-generated
content.

### 11.9 Preferences and the Database

Preferences that reference database records (`default_role`) are not protected by
foreign keys. The application shall therefore validate such a value against the
database before using it, and shall remove the preference if the record no longer
exists or is inactive.

---

## 12. INPUT VALIDATION AND ERROR HANDLING

The application shall validate user input before saving it to the database.

### 12.1 General Validation

* Required fields shall not be empty.
* Text fields shall be checked for values that contain only whitespace.
* Numeric values shall be within their defined ranges.
* Dropdown values shall correspond to valid options.
* Invalid input shall not be saved.
* Validation messages shall identify the field and explain how to correct the value.
* The application shall preserve the user’s entered values when validation fails.

### 12.2 Time Validation

Values entered in `HH:MM:SS` fields shall:

* Contain exactly three numeric components.
* Use hours from `00` through `23`.
* Use minutes and seconds from `00` through `59`.

For duration fields, the value shall be greater than `00:00:00`. The application shall define a maximum supported duration.

### 12.3 Database Validation

The application shall validate values before writing them to the database and use database constraints where appropriate.

For example:

* `priority_quadrant` shall be one of `0`, `1`, `2`, `3`, or `4`.
* Boolean settings shall contain only valid boolean values.
* A default role shall reference an active role_id from the roles table in the LifeVector database.
* A default start interface shall reference an active interface id from the interfaces table of LifeVector database.
* `sort_order` shall be a positive integer.

If a database operation fails, the application shall not leave the interface in a state that falsely indicates the change was saved.

---

## 13. WEEK CALCULATION

The WEEK interface shall use a consistent week-calculation function.

The function shall determine the start and end dates of the current week using:

* The current local date.
* The user’s configured first day of the week.

`CURRENT_WEEK` shall refer to the date range beginning on the configured first day of the current week and ending immediately before the next week begins.

The WEEK interface shall display scheduled activities whose scheduled date falls within this range and whose status is `NONE`.

The application should use date-range comparisons rather than relying only on a week number. This avoids ambiguity around week numbering at the beginning and end of a calendar year.

**Implementation requirement:** Provide a function that returns the start date and end date of the current week. Use that range to retrieve the WEEK interface’s scheduled activities.


## 14. PLANNER

           MON        TUE        WED
        ┌────────┬──────────┬─────────┐
Day     │        │ Read Ch7 │ Exercise│
Plans   │        │ Assignment│        │
        ├────────┼──────────┼─────────┤
08:00   │        │          │         │
09:00   │        │          │         │
10:00   │        │          │         │
...

The planner is the primary scheduling interface of LifeVector.

It has two main elements:
* The seven-day time grid
* List of week's priorities

The week's priorities list should:
* display goals in a list which have the following properties:
 * priority_quadrant = 1 or priority_quadrant = 2

Seven-day time grid
The planner displays the currently selected week as a seven-day time grid.

Layout:

* The planner contains seven columns, one for each day of the selected week.
* Each column has a header containing:

  * a visual indicator for the current day;
  * the date;
  * the abbreviated day name

* Example: `TODAY_SYMBOL 7 Thu`

* There is a small area under each day's header and above the time table 
  called "Day priorities Area" that represents goals which yet have no scheduled time but
  have been allocated a particular day
* The vertical axis represents time.
* The first visible time is determined by `time_starting_day`.
* The last visible time is determined by `time_ending_day`.
* The planner contains time rows corresponding to the configured day range.
* The planner should initially scroll to, or otherwise centre the view around, 
the current time when viewing the current week.

A scheduled goal is displayed as a visual block within the planner.

The position of a goal in the time table represents its scheduled:

* day;
* time.

But, a goal in the "Day priorities Area" only has scheduled:
* day

The size of the block represents its estimated duration.

Already scheduled goals are displayed automatically in their corresponding day
and time positions under the following rules.
 * If a goal is scheduled for a particular day but no time is provided then it appears 
 in the "Day priorities Area"
*  If a goal is already scheduled for a particular day and time then it appears in its corresponding
   day and time

Goals should retain their role and priority information while being displayed in 
the planner.

The planner supports drag-and-drop scheduling.

When an unscheduled goal from the week's priorities list is dragged into a day/time 
position:

* its `date` is set to the selected day;
* its `time` is set to the selected start time;
* it becomes scheduled for that time.

but if it dragged into "Day priorities Area" then:
* its 'date' is set to the selected day;
* no change to 'time' propertiy occurs

When an existing scheduled goal is dragged:

* dragging horizontally changes its scheduled day;
* dragging vertically changes its start time.

The interface should provide clear visual feedback indicating where the goal will be placed.

The duration of a scheduled goal can be changed directly from the planner.

* Dragging the bottom edge of a goal downward increases its estimated duration.
* Dragging the bottom edge upward decreases its estimated duration.
* The corresponding `estimated_duration` value is updated automatically.
* The duration must remain within valid limits.

The planner should prevent or clearly indicate invalid overlaps where appropriate.

A goal behaves as an independent object within the planner.

The user can:

* select a goal;
* open its edit interface;
* mark it as completed;
* move it;
* resize its duration;
* open its context menu.

Clicking the goal itself opens the goal-edit interface, while clicking its completion 
checkbox changes its completion status.

The planner normally opens to the current week.

The user should be able to navigate to:

* previous week;
* current week;
* next week;
* another selected week.

The definition of the first day of the week must respect the user's `day_starting_week` 
preference.

The calculation of the week number/date range should use a reliable date/calendar 
implementation rather than relying on manually calculated week numbers.


GUIDED WEEKLY PLAANING HELPER
The Guided Weekly Planning feature helps the user deliberately plan the upcoming week 
before scheduling individual activities. This feature is enabled by default.

If 'helper' = 1 from preferences then:
A banner should be activated automatically on the Today interface when user
configured `planning_day` arrives, The banner should state 
    Sunday
    Your weekly planning is due.
    [Plan Week] [Later]

while also being accessible manually from the application.

The whole process is guided by a wizard being displayed at the bottono of the screen that has:
 * Instructions/tips 
 * NEXT / FINISH button
 * SKIP button
 * EXIT PLANNING button

The workflow consists of the following stages.

Stage 0 — Reconnect to mission statement and Roles
The weekly planning wizard first displays the user's mission statement if any so the 
user can read/review it. 

After reviewing the mission statement the user clicks NEXT where user is taken to
the roles page where user can reconnect to their roles/responsibilities

Clicking on NEXT one more time starts stage 1

Stage 1 — Review and Prioritize
1. The user is taken to 'Time Management Matrix' interface of the app
2. The user assigns them to the appropriate quadrant of the Time Management Matrix

The user should deliberately select the goals that deserve attention during the upcoming week.

The planner should encourage the user to select at least one Quadrant II goal for each 
active role where appropriate.

The user clicks on next being displayed at the botton of the screen in order to move the 
next stage

Stage 2 — Estimate Duration
The user is taken to the set duration interface where the user specifies or confirms 
each weekly prioritized tasks estimated duration in minutes.

When duration for all goals having property priority_quadrant = 1 or 2 are estimated or the user click
next from where the third stage starts

Stage 3 — Allocate to Days

The application takes the user to the "planner" interface where goals are displayed 
in the weekly priorities list.

The user transfers goals from the weekly priorities list into specific days by 
dragging and dropping them into that day's "Day priorities Area".

At this stage the user decides **which day** the activity should be performed.

The user does not necessarily need to assign an exact time yet.

Stage 4 — Schedule

On the same "planner"interface the user then drags a goal from that day's "Day priorities Area"
onto a specific time position

The result is a concrete weekly schedule.

The objective is to ensure that the user's **most important responsibilities receive 
intentional time during the week**.

This feature can be disabled from the PREFERENCE interface

### 15. Add Goal/Role and Edit Goal

The `add_goal` and `edit_goal` interfaces shall use the same goal-entry menu.

When the menu is opened using `edit_goal`, the fields shall be pre-populated with the goal's existing information. The user can modify any editable field and save the changes.

When the menu is opened using `add_goal`, the fields shall initially be empty or contain their configured default values. After the user provides the required information and selects **Add**, a new goal shall be created and stored in the database.

## 15. Goal Fields

The Add/Edit Goal interface shall be used to create new goals and modify existing goals.

The interface shall be platform-independent at the application-logic level so that the same goal model and business rules can later be reused on other platforms such as Android and Windows.

### 15.1 Title — Required

A single-line text field shall allow the user to enter or edit the goal title.

The title:

* Must not be empty.
* Must not consist solely of whitespace.
* Shall be trimmed of unnecessary leading and trailing whitespace before being saved.

### 15.2 Description — Optional

A multi-line text field shall allow the user to enter additional information about the goal.

The description may be left empty.

### 15.3 Date — Optional

The user may assign a date to the goal.

When the date field is selected, the interface shall provide a built-in date picker from which the user can select a date.

If no date is selected, the goal remains undated.

A date entered in this field represents the **goal's assigned date**. It does not, by itself, indicate that the goal has been assigned a specific start time.

The application shall preserve the distinction between:

* a goal having an assigned date;
* a goal being allocated to a particular day during weekly planning; and
* a goal/activity having an exact scheduled time.

### 15.4 Time — Optional

The user may assign a specific start time to the goal.

The interface shall provide a suitable time picker or time input.

A time shall only represent an exact scheduled start time when an associated date exists.

If the user enters a time without a date, the application shall automatically use the current/selected date **only if this behavior has been explicitly configured as the application's standard behavior**. Otherwise, the application shall reject the time and inform the user that a date must first be selected.

**Implementation decision:** For consistency and to avoid silently creating unintended schedules, the application shall require a date before accepting a time.

Therefore:

> `Time != NULL` → `Date != NULL`

A time without a date shall be considered invalid.

### 15.5 Role — Required

A dropdown/select field shall contain all active roles defined by the user.

The user must assign every goal to a role.

When creating a new goal, the application's configured **Default Role** shall be pre-selected when a valid active default role exists.

If no default role exists, the user shall be required to select a role manually.

Inactive roles shall not be available for assigning to new goals.

Existing goals associated with a role that later becomes inactive shall retain their original role association.

### 15.6 Duration — Optional

The user may specify the estimated duration of the goal.

The duration shall be stored internally as an integer number of minutes.

Examples include:

* `15` minutes
* `30` minutes
* `60` minutes
* `90` minutes
* `120` minutes

The interface may provide commonly used duration presets while also allowing the user to enter a custom duration.

If the user does not provide a duration, the application's configured **Default Duration** shall be used.

A duration must be greater than zero.

The application shall distinguish between:

* **duration** — how long the user expects the goal/activity to take; and
* **start time** — when the goal/activity is scheduled to begin.

A duration does not require a start time.

### 15.7 Subgoals

A goal may contain zero or more subgoals.

Each subgoal shall have, at minimum:

* `title`
* `status` / completion state

Subgoals shall be displayed beneath their parent goal.

Each subgoal may independently be:

* Added
* Edited
* Reordered
* Marked as completed
* Marked as incomplete
* Removed

The database shall preserve the relationship between each subgoal and its parent goal.

Completing all subgoals shall **not** automatically mark the parent goal as completed by default.

If automatic parent completion is implemented in the future, it shall be controlled by an explicit Preferences setting.

A subgoal shall not exist independently of its parent goal.

### 15.8 Add / Save

When creating a new goal, the primary action shall be **Add**.

When editing an existing goal, the primary action shall be **Save**.

Before performing either operation, the application shall validate all required fields and applicable optional fields.

If validation succeeds:

* `add_goal` shall create a new goal.
* `edit_goal` shall update the existing goal.

If validation fails:

* The database shall not be modified.
* The invalid field shall be identified.
* An appropriate validation message shall be displayed.
* The user's entered values shall be preserved.

### 15.9 Close / Cancel

The interface shall provide a **Close/Cancel** action.

Selecting Close/Cancel shall close the Add/Edit Goal interface without saving unsaved changes.

If the user has modified any field, the application may display a confirmation such as:

> Unsaved changes will be lost. Continue?

The user shall then be able to either:

* Continue closing and discard the changes; or
* Return to the editor.

### 15.10 Shorthand Goal Entry

The application shall optionally support shorthand entry for rapidly creating or editing a goal.

The shorthand syntax shall allow the user to specify supported goal properties in a single text input.

Basic form:

`TITLE @TIME DURATIONm DATE`

Examples:

`Study Physics @18:00 60m`

`Read Chapter 5 @20:00 45m`

The shorthand parser shall identify supported components and use them to populate the corresponding fields in the Add Goal interface.

At minimum, the shorthand syntax shall support:

* Title
* Time
* Duration
* Date

The exact date syntax shall be standardized by the application.

For example, a future implementation may support:

`Study Physics @18:00 60m tomorrow`

or:

`Study Physics @18:00 60m 2026-09-19`

The parser shall not silently interpret ambiguous input in a way that could create an unintended schedule.

Invalid or ambiguous components shall result in an appropriate validation message where necessary.

Shorthand entry shall be an alternative input method only. It shall ultimately produce the same goal data structure as entering the equivalent information through the normal Add/Edit Goal interface.

### 15.11 Editing an Existing Goal

When editing an existing goal, the interface shall populate all applicable fields with the goal's current values.

Changes shall not be written to the database until the user selects **Save**.

If the user closes the interface without saving, the original goal shall remain unchanged.

### 15.12 Goal Information vs. Scheduling

The Add/Edit Goal interface shall primarily manage **goal information**.

Goal creation and scheduling shall remain conceptually separate operations.

The application's workflow may therefore be understood as:

`Create Goal → Assign Role → Classify Priority → Select for Week → Allocate to Day → Schedule Exact Time`

These stages do not necessarily have to occur at the same time.

For example:

* A goal may exist without a date.
* A goal may have an assigned date without an exact start time.
* A goal may be selected for a week without being assigned to a particular day.
* A goal may be allocated to a day without having an exact start time.
* A scheduled goal/activity may have both a date and an exact start time.

The Add/Edit Goal interface may provide date, time, and duration fields as a convenience. However, the underlying application architecture shall maintain the conceptual distinction between **goal information**, **weekly/day allocation**, and **exact scheduling**.

Where the Planner performs scheduling-specific operations, the Add/Edit Goal interface shall not duplicate or bypass the Planner's scheduling rules.

### 15.13 Validation Rules

The following rules shall apply before a goal is saved:

| Field         | Validation                                                            |
| ------------- | --------------------------------------------------------------------- |
| Title         | Required; must not be empty or whitespace-only                        |
| Description   | Optional                                                              |
| Date          | Optional; must be a valid date when provided                          |
| Time          | Optional; requires a date                                             |
| Role          | Required; must reference a valid active role when creating a new goal |
| Duration      | Optional; must be greater than zero when provided                     |
| Subgoal title | Required when a subgoal is created                                    |
| Priority      | Must be a valid `priority_quadrant` value                             |

The application shall reject invalid data before sending it to the database.

Database constraints shall also be used where appropriate so that invalid data cannot be stored through an alternative application path.

---