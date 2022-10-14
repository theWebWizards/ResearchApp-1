import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import create_db, get_migrate
from App.main import create_app
from App.controllers import ( create_Author, get_all_users_json, get_all_users )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    create_db(app)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 
publication_cli = AppGroup('publication', help='Publication object commands')

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("email", default="rob@email.com")
@click.argument("fullname", default="rob robing")
@click.argument("credentials", default="student")
def create_user_command(username, password, fullname, email, credentials):
    create_Author(username, password, fullname, email, credentials)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli


@publication_cli.command("create", help="create a publication")
#@click.Argument()
@click.argument("title", default="title")
@click.argument("PublicationContent", default="computers are cool")
@click.argument("AuthorName", default="rob robing")
@click.argument("AuthorCredentials", default="student")
@click.argument("CategoryInfo", default="technology")
@click.argument("PublicationID", default= 1)
def create_publication_command(title, PublicationContent, AuthorName, AuthorCredentials, CategoryInfo, AuthorID):

    CreatePublication(title, PublicationContent, AuthorName, AuthorCredentials, CategoryInfo, AuthorID)
    print(f'{Publication} created!')

app.cli.add_command(publication_cli)


'''
Generic Commands
'''

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)