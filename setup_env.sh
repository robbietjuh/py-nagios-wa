#!/bin/sh
# Sets up a basic environment for the package to run in

# Check whether an environment has already been set up
if [ -d env ];
then
    # Create a new virtualenv
    echo "Setting up a new virtualenv..."
    virtualenv env

    if [ $? -ne 0 ];
    then
        echo
        echo "Could not set up a new environment."
        echo "Please check that you have virtualenv installed."
        exit 1
    fi

    # Activate the virtualenv
    echo "Activating the new virtualenv..."
    source env/bin/activate

    # Install the required packages
    echo "Installing requirements..."
    pip install -r requirements.txt

    if [ $? -ne 0 ];
    then
        echo
        echo "Could not install requirements."
        echo "Please check that you have pip installed."
    fi

    # And done! :-)
    echo
    echo "Done! :-)"
    exit 0
fi

# Nothing left to do!
echo "The virtualenv is already set up. Nothing to do!"
echo "NB. To reinstall the environment, rm -r ./env and rerun the script."
exit 0