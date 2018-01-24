# Project SIGIA

TL;DR: Picked the wrong tool for the job(final uni project) but went through with it. (Still <3 Django though)


Project SIGIA is my final uni project, it's a massive if bloated data recollection webapp(?), it's main purpose it's to feed information
to the Uni's database that it currently lacks in any digital way. (hence all the apps.)

The main things it provides are:

1. A minimal dashboard for each location implemented via django-graphos.
    1. Besides the dashboard there will be:
        1. A PDF report available only to the dean of each faculty/unidad
        1. A PDF report available only to the director of each escuela(school)(report about each career) or departamento(department)(report about it's teachers)
1. A students app to keep track of their data, final project request approvals and final projects delivered (needed for several metrics, student DO NOT HAVE a user).
1. A professor/academic app, so professors can have their own profiles and keep them updated.
1. Related to the above, An academic app where professors can log in their activities to have them approved by their department's director
1. An inventory app, to "manage" all resources available to each location (I seriously tried to remove this requirement but alas...)


## Some Extra Info - Project Complications
Some of this information already exists on a database to which I have no access (a ...odd, to put it nicely,  old Oracle DB that it's going to someday hopefully going to be migrated to Postgres),
from which I'll duplicate the already existing data to this project's tables(the collected info will then be mirrored back to the oracle DB, which is the whole purpose of this thing).

* There are some weird hacks along the way as I needed to comform to the odd way to whole place is run. (Composite PKs, tables that are related yet had no columns assgined as FKs, and more...)
    * For example:
        * The code for a carrer is handled as such cod_sede - cod_unidad - cod_seccion - cod_carrera (seat_code - faculty_code - school_code - carreer_code). This makes it so
        01-24-01-01 is a career that belongs to school 01 in faculty 24 in seat 01, and 02-24-01-01 is the same except that it belongs to seat 02.
        * This all sounds nice and simple right? Except for the fact that only seat 01 handles the concept of multiple faculties and schools. Every other
         seat in the instituion behaves more like a branch with a single umbrella faculty, umbrella school and umbrella department, which isn't documented anywhere officially.
        * This ends up meaning that pretty much everyone(end users) on seats 02+ do not act like they belong to a particular location from seat 01.
        * Which demanded me to both keep the location codes AND at the same time group everyone under the same place. Hence the weird hacks.
        * I needed to keep the codes for queries to come from other places (that's someone else using my DB though [and their own misery] though).

* As for other complications:
    * There's some complicated permissions that can't be handle by the default authorization.
        * Essentially users can only see info from their location.
            1. Deans can check up on their faculty's PDF report
            1. School directors can check up on students on careers belonging to their school and PDF reports at the school or career level and approve students final projects.
            1. Department directors can approve professors activities and check up on the PDF report of their department.


Besides that everything is pretty much straightforward.

# Requirements

1. Python 3.5.2
1. See requirements.txt

# Setup
## To-do (reincorporate this managementement methods, left them in an old version of the app)
1. run makemigrations
1. run migrations
1. run load_initial_data
1. run load_locations
1. run load_students
1. run load_users

# To-do

#### Models
1. ~~Include Room models~~
1. ~~Include Item models~~
1. ~~Include Activities models~~

#### Views
1. ~~Include Room create view~~
1. ~~Include Item bulk-upload view~~ (Will be handled on a 1-by-1 basis, open to formset maybe?)
    * ~~Restrict file upload to .csv~~ (Only for initial upload, django-import-export will handle that)
1. Include list unapproved activities view.
1. Include rejected activities view.
1. Include rejected anteproyecto view.
#### Third-party apps
1. ~~Add django-import-export package for easier doing of the above.~~
1. ~~Create graphs using django-graphos~~
1. ~~Incorporate django-filter~~
1. ~~Incorporate django-autocomplete-light~~
1. Finish templates

## To-Do (can be done while running tests with users)

1. ~~Restrict users to modify data from their locations(be it their "seccion" or "carrera"s belonging to them) only~~
1. Create permissions (Who can see reports mostly)
1. Complete bulk creation management commands
    * Assign permission to groups
    * Create users
    * Assign users to group
1. Create pdf reports using reportlab or weasyprint
1. Do everything related to queries/mini-helpdesk app.

1. ~~Learn how to push to prod~~
1. ~~Separate settings between dev/prod~~

### Optional to-do

1. ~~Use django-tables2~~
1. Figure out Sphinx