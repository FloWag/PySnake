export workdir=$(pwd)

echo "adding ${workdir} to PYTHONPATH ..."
export PYTHONPATH=$PYTHONPATH:$workdir
echo "success!"