
PYTHON_ENV="env_miw3"
echo $PYTHON_ENV
echo $VIRTUAL_ENV

if [[ $VIRTUAL_ENV == *$PYTHON_ENV* ]]  ; 
then 
echo "party"; 
else
#deactivate
source ~/MakeAIWork3/env_miw3/Scripts/activate
fi

# python setup install